from __future__ import with_statement

import re

from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataFloat, XSDataString


class EDPluginRBins(EDPluginExecProcessScript):
    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setRequiredToHaveConfiguration(True)

        # from max's script
        # start: /Table of resolution bins a/
        self.start_re = re.compile('Table of resolution bins a')
        # relevant line: /(\S+)\s+--\s+(\S+)/)
        self.relevant_re = re.compile('(\S+)\s+--\s+(\S+)')

    def configure(self):
        EDPluginExecProcessScript.configure(self)

    def preProcess(self):
        EDPluginExecProcessScript.preProcess(self)

        data_input = self.getDataInput()
        self.high = data_input.high
        self.low = data_input.low

        self.addInputLine('RESOLUTION_SHELLS= %s %s' % (self.low, self.high))

    def checkParameters(self):
        data_input = self.getDataInput()
        self.checkMandatoryParameters(data_input.high, 'high')
        self.checkMandatoryParameters(data_input.low, 'low')

    def process(self):
        EDPluginExecProcessScript.process(self)

    def postProcess(self):
        # parse our output
        outfile = self.getScriptLogFileName()
        result = list()
        with open(outfile, 'r') as out:
            # have we encountered the start of the table yet?
            started = False
            for line in out:
                if self.start_re.match(line) is not None:
                    started = True
                    continue
                # we're parsing
                if started:
                    match = self.relevant_re.match(line)
                    if match is not None:
                        result.append(match.group(2))
        # we're done
