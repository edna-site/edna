from __future__ import with_statement
import re
from EDVerbose import EDVerbose
from EDPluginExecProcessScript import EDPluginExecProcessScript
from XSDataAutoproc import XSDataMatthewsCoeffOut, XSDataMatthewsCoeffIn
from XSDataCommon import XSDataFloat, XSDataString


# from max's xds_fullrun.pl:
#/opt/pxsoft/bin/matthews_coef <<FFF\n";
#print MAT "CELL $cell\n";
#print MAT "SYMM $symm\n";
#print MAT "NRES 200\n";
#print MAT "AUTO\n";
#print MAT "END\nFFF\n";
#close MAT;


class EDPluginSolveContent(EDPluginExecProcessScript):
    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        # the 3 regexpes used to parse the output, from max's script
        self.start_re = re.compile('Nmol\/asym  Matthews Coeff  \%solvent       P\(tot\)')
        self.good_re = re.compile('\S+\s+\S+\s+(\S+)\s+(\S+)')
        self.bad_re = re.compile('System')
        self.setXSDataInputClass(XSDataMatthewsCoeffIn)

    def checkParameters(self):
        data_input = self.getDataInput()
        for param in ['a', 'b', 'c', 'alpha', 'beta', 'gamma', 'symm']:
            self.checkMandatoryParameters(getattr(data_input, param),
                                          param)

    def preProcess(self):
        EDPluginExecProcessScript.preProcess(self)
        data_input = self.getDataInput()
        symm = data_input.symm
        cell = "CELL %s %s %s %s %s %s" % (data_input.a,
                                           data_input.b,
                                           data_input.c,
                                           data_input.alpha,
                                           data_input.beta,
                                           data_input.gamma)
        self.addListCommandExecution(cell)
        self.addListCommandExecution("SYMM %s" % symm)
        self.addListCommandExecution("NRES 200")
        self.addListCommandExecution("AUTO")

    def postProcess(self):
        # parse the output, the code's not very good looking
        # maybe rewrite the parsing without using regexpes
        outfile = self.getScriptLogFileName()
        best_p = 0
        best_sol = None
        with open(outfile, 'r') as out:
            # have we seen the start of the table we seek yet?
            started = False
            for line in out:
                if not started:
                    # see if our table is beginning yet
                    if self.start_re.match(line): started = True
                    continue
                else:
                    # try parsing the line as a table line
                    m = self.good_re.match(line)
                    bad = self.bad_re.match(line)
                    if m is not None and bad is None:
                        p = float(m.group(1))
                        if p > best_p:
                            best_p = p
                            best_sol = m.group(2)
        # we found what we were looking for
        if best_sol is not None:
            self.dataOutput = XSDataMatthewsCoeffOut(best_p=XSDataFloat(best_p),
                                                     best_sol=XSDataString(best_sol))
