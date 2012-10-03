#!/usr/bin/env python
# QSubDriver.py
#
#   Copyright (C) 2006 CCLRC, Graeme Winter
#
#   This code is distributed under the BSD license, a copy of which is 
#   included in the root directory of this package.
#
# 16th June 2006
# 
# A Driver implementation to work with sun grid engine clusters via the 
# "qsub" shell command. This is based on ScriptDriver. This works like...
#
# > qsub -cwd process-lrem.sh
# Your job 1871 ("process-lrem.sh") has been submitted.
# 
# Applicability: Linux with Sun Grid Engine
# 
# How This Works
# --------------
# 
# qsub to get the job id, then repeated qstat calls to find out what's 
# happening with this job. Raise exception if it looks like something has
# gone wrong (e.g. all of the queues are disabled or something.)
# 
# To find out when this has finished, keep calling qstat -j job_id
# until the following is seen:
# 
# Following jobs do not exist: 164459
#
# The rest of the Driver stuff can then follow.
# 
# This class has been deprecated. See SunGridEngineClusterDriver.
# 

import os
import subprocess
import time
import random

from DefaultDriver import DefaultDriver
from DriverHelper import script_writer

class QSubDriver(DefaultDriver):

    def __init__(self):

        if os.name != 'posix':
            raise RuntimeError, 'os "%s" not supported' % os.name
        
        DefaultDriver.__init__(self)

        self._script_command_line = []
        self._script_standard_input = []

        self._script_name = self._name

        self._script_status = 0

        # this is opened by the close() method and read by output
        # from self._script_name.xout
        
        self._output_file = None

        return

    def set_name(self, name):
        return self.setName(name)

    def setName(self, name):
        '''Set the name to something sensible.'''
        self._script_name = name
        
        return

    def start(self):
        '''This is pretty meaningless in terms of running things through
        scripts...'''
        
        for c in self._command_line:
            self._script_command_line.append(c)

    def check(self):
        '''NULL overloading of the default check method.'''
        return True

    def check_sge_errors(self, sge_stderr_list):
        '''Check through the standard error from Sun Grid Engine
        for indications that something went wrong...'''

        for o in sge_stderr_list:
            if 'command not found' in o:
                missing_program = o.split(':')[2].strip()
                raise RuntimeError, 'executable "%s" missing' % \
                      missing_program

    def _input(self, record):
        self._script_standard_input.append(record)

        return

    def _output(self):
        return self._output_file.readline()

    def _status(self):
        return self._script_status

    def close(self):
        '''This is where most of the work will be done - in here is
        where the script itself gets written and run, and the output
        file channel opened when the process has finished...'''

        script_writer(self._working_directory,
                      self._script_name,
                      self._executable,
                      self._working_environment,
                      self._script_command_line,
                      self._script_standard_input)

        # this will return almost instantly, once the job is in
        # the queue
        pipe = subprocess.Popen(['qsub', '-V', '-cwd',
                                 '%s.sh' % self._script_name],
                                cwd = self._working_directory,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE)

        # this will get all of the output as a tuple (stdout, stderr)
        stdout, stderr = pipe.communicate()

        # check the standard error
        if len(stderr) > 0:
            # something probably went wrong
            if 'error opening' in stderr:
                raise RuntimeError, 'executable "%s" does not exist' % \
                      stdout.split('\n')[0].split(':')[0].replace(
                    'error opening ', '')

        # probably everything is ok then

        # the job id etc go to the standard output
        job_id = stdout.split('\n')[0].split()[2]

        # now have a while loop watching this job id via qstat -j

        while True:
            pipe = subprocess.Popen(['qstat', '-j', '%s' % job_id],
                                    cwd = self._working_directory,
                                    stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE)

            stdout, stderr = pipe.communicate()

            if 'Following jobs do not exist' in stderr:
                # then the job has finished
                break

            # sleep for 10 seconds
            time.sleep(10)

        # the following files may have some interesting contents - despite
        # the fact that all of the output was supposed to be piped to
        # the standard output...

        # oh - just looked. in the DriverHelper.script_writer method
        # the output is simply piped > not 2>&1 - which means that the
        # standard error output will appear below...

        sge_stdout = os.path.join(self._working_directory,
                                  '%s.sh.o%s' % (self._script_name,
                                                 job_id))

        sge_stderr = os.path.join(self._working_directory,
                                  '%s.sh.e%s' % (self._script_name,
                                                 job_id))

        # check the standard error file for any indications that
        # something went wrong running this job...

        error_output = open(sge_stderr, 'r').readlines()
        self.check_sge_errors(error_output)

        # it's nearly impossible to get the return status from qsub
        # so don't bother
        self._script_status = 0

        # set this up for reading the "standard output" of the job.
        self._output_file = open(os.path.join(self._working_directory,
                                              '%s.xout' % self._script_name),
                                 'r')

        # at this stage I should delete the sge specific files defined
        # above to be tidy...

        try:
            os.remove(sge_stdout)
            os.remove(sge_stderr)
        except Exception:
            # something wrong with this deletion?
            pass

        return

    def kill(self):
        '''This is meaningless...'''

        pass

    
if __name__ == '__main__':
    # Then run a simple test

    d = QSubDriver()

    d.set_executable('ExampleProgram')
    d.start()
    d.close()

    while True:
        line = d.output()

        if not line:
            break

        print line.strip()

