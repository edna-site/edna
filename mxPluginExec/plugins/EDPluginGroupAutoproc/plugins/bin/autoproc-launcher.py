#!/usr/bin/env python
# vim: expandtab:tabstop=4:softtabstop=4:ai
# input data model
#input_file : XSDataFile
#res_override : XSDataFloat optional #//cutoffs #completeness_cutoff : XSDataFloat optional #isig_cutoff : XSDataFloat optional
#r_value_cutoff : XSDataFloat optional
#cc_half_cutoff : XSDataFloat optional
#
#data_collection_id : XSDataInteger optional
#detector_max_res : XSDataFloat optional
#low_resolution_limit : XSDataFloat optional

# called this way
# xdsproc.pl -path /data/id23eh2/inhouse/opid232/20100209/mxschool/process -mode before -datacollectID 666783


import sys
import os
from stat import S_IRWXU, S_IXGRP, S_IRGRP, S_IXOTH, S_IROTH, S_IRUSR, S_IWUSR
import os.path
import tempfile
import subprocess
import time

import logging
from logging.handlers import HTTPHandler
import socket

import xdscfgparser

# this is where the edna autoproc tree resides on the disk
EDNA_PATH='/scisoft/edna-autoproc/'
# This is where the config file is
CONFIG_PATH='/scisoft/edna-autoproc/mxPluginExec/conf/XSConfiguration_ESRF.xml'
# This is where to send logging message through HTTP (my machine with a custom
# webserver for now.) If None, don't send stuff over HTTP
HTTP_LOG_URL=None

# this hack is present in the current script on the beamline so this value is
# not set anywhere else
os.environ['EDNA_SITE'] = 'ESRF_ISPyB'

# we'll poll the filesystem for the first image. Here are two values for the
# inter-poll (hahaha) time and total waiting time
WAIT_RESOLUTION = 20
WAIT_TIMEOUT = 1200

# XDS.INP creation is now asynchronous in mxcube, so it may not be here yet
# when we're started
WAIT_XDS_TIMEOUT = 20
WAIT_XDS_RESOLUTION = 5

def _template_to_image(fmt, num):
    # for simplicity we will assume the template to contain only one
    # sequence of '?' characters. max's code uses a regexp so this
    # further restrict the possible templates.
    start = fmt.find('?')
    end = fmt.rfind('?')
    if start == -1 or end == -1:
        # the caller test for the file existence and an empty path
        # does not exist
        return ''
    prefix = fmt[:start]
    suffix = fmt[end+1:]
    length = end - start + 1

    # this is essentially the python format string equivalent to the
    # template string
    fmt_string = prefix + '{0:0' + str(length) + 'd}' + suffix

    return fmt_string.format(num)

# setup the HTTP log handling
log = logging.getLogger()
log.setLevel(logging.DEBUG)
if HTTP_LOG_URL is not None:
    log.addHandler(HTTPHandler(HTTP_LOG_URL, '/'))

# do the arg parsing by hand since neither getopt nor optparse support
# single dash long options.

args = sys.argv[1:]

if (len(args) % 2) != 0:
    logging.error('the argument list is not well formed (odd number of args/options)')
    sys.exit()

options = dict()
for x in range(0, len(args), 2):
    options[args[x]] = args[x+1]

path = options['-path']
input_file = os.path.join(path, 'XDS.INP')
nres = options.get('-residues')
spacegroup = options.get('-sg')
cell = options.get('-cell')

# parse the input file to find the first image
xds_appeared = False
wait_xds_start = time.time()
logging.debug('Waiting for XDS.INP file')
while not xds_appeared and time.time() - wait_xds_start < WAIT_XDS_TIMEOUT:
    if os.path.exists(input_file):
        xds_appeared = True
        logging.debug('XDS.INP file is there')
    else:
        time.sleep(WAIT_XDS_RESOLUTION)
if not xds_appeared:
    logging.error('XDS.INP file ({0}) failed to appear after {1} seconds'.format(input_file, WAIT_XDS_TIMEOUT))
    sys.exit(1)

cfg = xdscfgparser.parse_xds_file(input_file)
last_image = file_template = None
try:
    last_image = cfg['DATA_RANGE='][1]
    file_template = cfg['NAME_TEMPLATE_OF_DATA_FRAMES='][0]
except IndexError, KeyError:
    logging.warning("""Could not get all the required information (first image number and file template)
from the input file {0}""".format(input_file))

if last_image is not None and file_template is not None:
    # we have all the info to wait for the file

    #the file template is relative to the path passed to the script with the -path option
    file_template = os.path.abspath(os.path.join(path, file_template))
    fullpath = _template_to_image(file_template, int(last_image))
    logging.info('Waiting for last frame {0}'.format(fullpath))
    t0=time.time()
    appeared = False
    while time.time() - t0 < WAIT_TIMEOUT and not appeared:
        if os.path.exists(fullpath):
            appeared = True
        else:
            #print 'File not there, waiting {0}s'.format(WAIT_RESOLUTION)
            time.sleep(WAIT_RESOLUTION)
    if not appeared:
        logging.error("The last image (path: {0}) failed to appear after {1} seconds".format(fullpath, WAIT_TIMEOUT))
        sys.exit(1)
else: # not enough info to wait for file
    sys.exit(1)

# Once we get there the first frame's on disk, so proceed as usual

output_file = tempfile.NamedTemporaryFile(suffix='.xml',
                                          prefix='edna-autoproc-results-',
                                          dir=path,
                                          delete=False)
# we only want the filename
output_path = output_file.name
output_file.close()
os.chmod(output_path, S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH)

input_template = '''<?xml version="1.0"?>
<XSDataAutoprocInput>
  <input_file>
    <path>
      <value>{input_file}</value>
    </path>
  </input_file>
  <data_collection_id>
    <value>{dcid}</value>
  </data_collection_id>
  <output_file>
    <path>
      <value>{output_path}</value>
    </path>
  </output_file>
{nres_fragment}
{spacegroup_fragment}
{cell_fragment}
</XSDataAutoprocInput>
'''

if nres is not None:
    nres_fragment = """  <nres>
    <value>{0}</value>
  </nres>""".format(nres)
else:
    nres_fragment = ""

if spacegroup is not None:
    spacegroup_fragment = """  <spacegroup>
    <value>{0}</value>
  </spacegroup>""".format(spacegroup)
else:
    spacegroup_fragment = ''

if cell is not None:
    cell_fragment = """  <unit_cell>
    <value>{0}</value>
  </unit_cell>""".format(cell)
else:
    cell_fragment = ''

# the other parameters are not used right now
input_dm = input_template.format(input_file=input_file,
                                 dcid=options['-datacollectionID'],
                                 output_path=output_path,
                                 nres_fragment=nres_fragment,
                                 cell_fragment=cell_fragment,
                                 spacegroup_fragment=spacegroup_fragment)

# we now need a temp file in the data dir to write the data model to
dm_file = tempfile.NamedTemporaryFile(suffix='.xml',
                                      prefix='edna-autoproc-input-',
                                      dir=path,
                                      delete=False)
dm_path = dm_file.name
dm_file.file.write(input_dm)
dm_file.close()
os.chmod(dm_path, S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH)

# we also need some kind of script to run edna-plugin-launcher
script_file = tempfile.NamedTemporaryFile(suffix='.sh',
                                          prefix='edna-autoproc-launcher-',
                                          dir=path,
                                          delete=False)
script_template = '''#!/bin/sh
export EDNA_SITE=ESRF

cd {path}
/opt/pxsoft/tools/python/v2.6.6_20110210/centos5-x86_64/bin/python {edna_path}/kernel/bin/edna-plugin-launcher.py --inputFile {dm_path} --conf {config_path} --execute EDPluginControlAutoproc --debug
'''

script_file.file.write(script_template.format(path=path, dm_path=dm_path, edna_path=EDNA_PATH, config_path=CONFIG_PATH))
script_path = script_file.name
os.chmod(script_path, S_IRWXU|S_IXGRP|S_IRGRP|S_IXOTH|S_IROTH)


# now that everything's in place we need to call oarsub
#command_line = ['oarsub', '-p', 'private_node=\'MX\'', '-d', path, script_path]
#command_line = ['oarsub', '-p', 'private_node=\'MX\'', '-l', 'core=6,walltime=0:30:0', '-d', path, script_path]

# this is horrible
command_line = 'nohup ssh -f mxnice {script_path} 2>&1 > /dev/null &'.format(script_path=script_path)
logging.debug('going to run "{0}"'.format(command_line))
code = subprocess.call(command_line, shell=True)
logging.debug('the command returned {0}'.format(code))
