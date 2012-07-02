
# input data model
#input_file : XSDataFile
#res_override : XSDataFloat optional
#//cutoffs
#completeness_cutoff : XSDataFloat optional
#isig_cutoff : XSDataFloat optional
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
import os.path
import tempfile
import subprocess

# this is where the edna autoproc tree resides on the disk
EDNA_PATH='~opid23/edna-autoproc/'

# this hack is present in the current script on the beamline so this value is
# not set anywhere else
os.environ['EDNA_SITE'] = 'ESRF_ISPyB'


# do the arg parsing by hand since neither getopt nor optparse support
# single dash long options.

args = sys.argv[1:]

if (len(args) % 2) != 0:
    print 'the argument list is not well formed (odd number of args/options)'
    sys.exit()

options = dict()
for x in range(0, len(args), 2):
    options[args[x]] = args[x+1]

path = options['-path']
input_file = os.path.join(path, 'XDS.INP')

output_file = tempfile.NamedTemporaryFile(suffix='.xml',
                                          prefix='edna-autoproc-results-',
                                          dir=path,
                                          delete=False)
# we only want the filename
output_path = output_file.name
output_file.close()

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
</XSDataAutoprocInput>
'''

# the other parameters are not used right now
input_dm = input_template.format(input_file=input_file,
                                 dcid=options['-dataCollectionID'],
                                 output_path=output_path)

# we now need a temp file in the data dir to write the data model to
dm_file = tempfile.NamedTemporaryFile(suffix='.xml',
                                      prefix='edna-autoproc-input-',
                                      dir=path,
                                      delete=False)
dm_path = dm_file.name
dm_file.file.write(input_dm)
dm_file.close()

# we also need some kind of script to run edna-plugin-launcher
script_file = tempfile.NamedTemporaryFile(suffix='.sh',
                                          prefix='edna-autoproc-launcher-',
                                          dir=path,
                                          delete=False)
script_template = '''#!/bin/sh
export EDNA_SITE=ESRF
/opt/pxsoft/tools/python/v2.6.6_20110210/centos5-x86_64/bin/python {edna_path}/kernel/bin/edna-plugin-launcher.py --inputFile={dm_path} --execute=EDPluginControlAutoproc
'''

script_file.file.write(script_template.format(dm_path=dm_path, edna_path=EDNA_PATH))
script_path = script_file.name

# now that everything's in place we need to call oarsub
command_line = ['oarsub', '-p', 'private_node=\'MX\'', '-d', path, script_path]
print 'going to run "{0}"'.format(' '.join(command_line))
code = subprocess.call(command_line)
print 'return code:', code
