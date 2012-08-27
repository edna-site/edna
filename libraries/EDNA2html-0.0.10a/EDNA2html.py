#     EDNA2html.py: report output from EDNA MX Characterisation runs
#     Copyright (C) Diamond 2010 Peter Briggs
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#
########################################################################
#
# EDNA2html.py
#
########################################################################

"""EDNA2html: report output from EDNA MX Characterisation runs"""

__cvs_id__ = "$Id: EDNA2html.py,v 1.130 2010/04/29 16:16:47 pjb93 Exp $"
__version__ = "0.0.10a"

#######################################################################
# Import modules that this module depends on
#######################################################################
import xml.sax
import sys
import os
import shutil
import subprocess
import time
import Magpie
import Canary
import Jackdaw

#######################################################################
# Module constants
#######################################################################

# EDNA2html error codes
NO_ERROR = 0
RUN_BASENAME_DIR_NOT_FOUND = 1
CHARACTERISATION_DIR_NOT_FOUND = 2
UNDETERMINED_XML_PREFIX = 3
INCOMPLETE_EDNA_RUN_DATA = 4

# Rotation axis display name
ROTATION_AXIS_NAME = "omega"

#######################################################################
# Class definitions
#######################################################################

# Bootstrap class for getting help text
#
class Help:
    """Class for storing and retrieving help text

    This is an initial version which stores help text in class
    attributes, which can then be referenced by the main program
    as required when generating tool-tip help.

    By default returns the text stored against attributes to be
    used as tool-tip help. However if 'show_names' is set to True
    on initialisation then instead the names of the requested
    attribute will be returned - this provides a mechanism for
    identifying which placeholders are used in the output document.

    The tool tip text is read from the external 'tool_tip_file'."""
    def __init__(self, tool_tip_file, show_names=False):
        self.__show_names = show_names
        self.__value = dict()
        self.__load_from_file(tool_tip_file)

    def __getattr__(self, attr):
        """Internal: return value of an undefined attribute"""
        if self.__show_names:
            if self.__value.has_key(attr):
                return "Placeholder name: " + str(attr)
            else:
                return "Undefined name: " + str(attr)
        else:
            try:
                return self.__value[attr]
            except KeyError:
                return "Undefined name: " + str(attr)

    def __load_from_file(self, tool_tip_file):
        """Read and store tool tip data from external file"""
        if not tool_tip_file: return
        print "Reading tool tip text from " + str(tool_tip_file) + ".."
        f = open(tool_tip_file, 'r')
        for line in f:
            line = line.strip()
            # Skip comment lines
            try:
                if line[0] == '#': continue
            except IndexError:
                pass
            # Skip blank lines
            if not line: continue
            # Deal with remaining lines
            # These should be of the format placeholder: text
            try:
                i = line.index(':')
                key = line[:i].strip()
                value = line[i + 1:].strip().strip("\"")
                # Store the extracted key/value pair
                self.__value[key] = value
            except IndexError:
                print "Bad line: " + line
                print "Skipped"
                continue
        f.close
        print "..done"
        return

# Simple XML node tree
#
class SimpleXMLNode:
    """Simple representation of a node in an XML tree

    SimpleXMLNode represents a basic node in an XML tree, with the
    tree being constructed by adding child nodes as required.

    Nodes have a name (except for a 'root' node, which doesn't need
    a name) and may also have an associated value. They don't have
    any other attributes.

    A root node is created using e.g.:

    tree = SimpleXMLNode()

    and nodes are added using e.g.:

    new_node = tree.addNode('new_node')"""

    def __init__(self, name=None):
        """Create a new SimpleXMLNode

        Optional parameter 'name' specifies an associated name
        for the SimpleXMLNode, which can used to look up the
        node when it is a subnode of another SimpleXMLNode object
        (see e.g. the 'childNodeNames' and 'findNode' methods
        for examples)."""
        self.__name = name
        self.__children = []
        self.__value = None
        self.__hasValue = False
        return

    def __len__(self):
        """Return the number of child nodes"""
        return len(self.__children)

    def __str__(self):
        """Return string representation of the node

        If the node has an associated value then return this as
        a string, otherwise return a string representation of the
        node name."""
        if self.__hasValue:
            return str(self.__value)
        else:
            return "<SimpleXMLNode instance: " + str(self.__name) + ">"

    def __float__(self):
        """Return node value as a float

        If the node has an associated value then convert this to
        a float and return it. An uncaught exception will be raised
        if the conversion is not possible.

        Returns a ValueError exception if no value is associated
        with the node."""
        if self.__hasValue:
            return float(self.__value)
        else:
            raise ValueError, "No value attached to '" + str(self.__name) + "'"

    def __int__(self):
        """Return node value as an integer

        If the node has an associated value then convert this to an
        integer and return it.

        The conversion is 2-part: first the value is converted to a
        float, and then to an integer. Any exceptions raised by these
        operations are not caught.

        Returns a ValueError exception if no value is associated with
        the node."""
        if self.__hasValue:
            return int(self.__float__())
        else:
            raise ValueError, "No value attached to '" + str(self.__name) + "'"

    def __iter__(self):
        """Return an iterator object for this node
        
        Returns a single-element list containing a reference to
        the node object.

        This supplied to allow a single node object to be used in a
        for ... in loop in place of a list of nodes, without requiring
        the calling application to include code to handle these two
        different cases.

        For example: if 'node' is an SimpleXMLNode object then

        for child in node.subnode:
        ...

        should always work, whether there is only one child 'subnode'
        (in which 'node.subnode' will be a SimpleXMLNode object),
        or several (in which case 'node.subnode' will be a list of
        SimpleXMLNode objects)."""
        return iter([self])

    def __getattr__(self, attr):
        """Return child nodes called 'attr'

        This implements the functionality:

        subnodes = node.subnodes

        Depending on the number of child nodes matching the name
        'attr'

        - return a SimpleXMLNode object if there is only one
          matching child node
        - return a list of SimpleXMLNode objects if there are
          more than one matching child nodes
        - return an empty list if there are no matching child
          nodes."""
        children = []
        for child in self.__children:
            if child.getNodeName() == attr:
                children.append(child)
        if len(children) == 0:
            raise AttributeError, \
                "No children called '" + \
                str(attr) + \
                "' for node '" + \
                str(self.__name) + "'"
        elif len(children) == 1:
            return children[0]
        else:
            return children

    def addNode(self, name):
        """Create a new subnode for this node

        Create and return a SimpleXMLNode object called 'name'
        which is also a subnode of this node object."""
        if not name:
            raise ValueError, "addNode: invalid 'name'"
        node = SimpleXMLNode(name)
        self.__children.append(node)
        return node

    def getNodeName(self):
        """Return the name associated with this node object"""
        return self.__name

    def setValue(self, value):
        """Set the value associated with the node object"""
        self.__hasValue = True
        self.__value = value

    def getValue(self):
        """Return the value previously associated with the node object"""
        return self.__value

    def childNodeNames(self):
        """Return a list of all the child node names"""
        names = []
        for child in self.__children:
            names.append(child.getNodeName())
        return names

    def childNodes(self):
        """Return the list of the SimpleXMLNode child objects"""
        return self.__children

    def findNode(self, name):
        """Retrieve the child node called 'name'

        Search the child nodes for the first node which matches
        'name'. If none of the immediate child nodes match then
        search each of their children, and so on.

        Returns the first match located, or else None if no
        match is found.

        Note: this method is really only recommended for situations
        where there is only one expected match."""
        for child in self.childNodes():
            if child.getNodeName() == name:
                return child
        for child in self.childNodes():
            node = child.findNode(name)
            if node != None:
                return node
        return None

# EDNAXMLHandler class
#
class EDNAXMLHandler(xml.sax.ContentHandler):
    """Generic handler for SAX parsing of EDNA XML files"""

    def __init__(self):
        """Create a new EDNAXMLHandler"""
        self.__context = [SimpleXMLNode()]
        self.__characters = []
        return

    def startElement(self, tag, attrs):
        # Deal with context
        last_node = self.__context[-1]
        self.__context.append(last_node.addNode(tag))
        # Set up to collect "value"
        if tag == "value":
            self.__characters = []
        return

    def endElement(self, tag):
        current_node = self.__context[-1]
        # Set the value
        if tag == "value":
            current_node.setValue(''.join(self.__characters))
            self.__characters = []
        # Deal with context
        if current_node.getNodeName() == tag:
            self.__context = self.__context[0:-1]
        return

    def characters(self, data):
        self.__characters.append(data)
        return

    def getSimpleXMLNodeTree(self):
        return self.__context[0]


# EDNALogData class
#
class EDNALogData:
    """Extract and store data from the EDNA MX log file

    Given a log file name, the EDNALogData object will automatically
    attempt to parse the log into sections and then extract specific
    data from each of those sections.

    Once initialised the calling application can retrieve the data
    by fetching the Magpie.Magpie processors for each log section.
    Further data can be extracted by requesting the Magpie.Data
    objects from each of the processors."""

    def __init__(self, log_file):
        """Create a new EDNALogData object

        'log_file' is the name and path to the log file of interest."""
        # Flag toggling verbose output from processing
        self.__verbose = False
        # Process the log file with Magpie
        self.__log = self.__parseLog(log_file)
        # Process and store the individual sections
        self.integration = self.__parseIntegration()
        self.strategy = self.__parseStrategy()
        self.errors = self.__parseError()

    def __parseLog(self, log_file):
        """Parse an EDNA log file using Magpie"""
        log = Magpie.Magpie(verbose=self.__verbose)
        # Add patterns to capture the different sections
        #
        # 'integration' pattern: matches all lines starting with
        # "Integration : MOSFLM :"
        log.addPattern('integration', "Integration : MOSFLM :(.*)", ['line'])
        #
        # 'strategy_best' pattern: matches all lines starting with
        # "Strategy : Best :"
        log.addPattern('strategy_best', "Strategy : Best :(.*)", ['line'])
        #
        # 'error' pattern: matches all lines starting e.g.
        # "20100422-193826  [ERROR]:"
        log.addPattern('error', "[0-9]+-[0-9]+[ \t]+\[ERROR\]:(.*)", ['message'])
        # Process the log file
        log.processFile(log_file)
        # Return populated Magpie processor
        return log

    def __parseIntegration(self):
        """Parse the section of the EDNA log for integration"""
        # Define a new processor to process this section
        integration = Magpie.Magpie(verbose=self.__verbose)
        #
        # 'image_range' block: matches block of text starting with e.g.
        # "Image directory     : /home/pjb/Diamond/xia2_data/demo"
        # and ending with e.g.
        # "Rotation axis end   :  1.0 [degrees]"
        integration.defineBlock('image_range',
                                "Image directory",
                                "Rotation axis end")
        #
        # 'statistics' block: matches block of text starting with e.g.
        # "Number of fully recorded reflections          :   477"
        # and ending with e.g.
        # "Number of bad reflections                     :     0"
        integration.defineBlock('statistics',
                                "Number of fully recorded reflections",
                                "Number of bad reflections")
        #
        # 'i_over_sigma' block: matches block of text starting with e.g.
        # "RMS spot deviation                            : 0.028 [mm]"
        # and ending with e.g.
        # "Average I/sigma at highest resolution         :   2.2"
        integration.defineBlock('i_over_sigma',
                                "RMS spot deviation",
                                "Average I/sigma at highest resolution")
        #
        # 'analysis_by_resolution' pattern: matches lines of the form:
        # "Res (Ang)    4.06   2.87   2.35   2.03   1.82   1.66   1.54  Overall"
        integration.addPattern('analysis_by_resolution',
                               "Res \(Ang\)(.*)",
                               ['bins'])
        #
        # 'analysis_fully_recorded' block: matches block of text starting e.g.
        # "Profile fitted fully recorded:"
        # and ending with e.g.
        # " <I/sigma>   76.4   88.5   50.1   29.7   17.3    7.5    5.7    2.2"
        integration.defineBlock('analysis_fully_recorded',
                                "Profile fitted fully recorded",
                                "I/sigma", include_flag=Magpie.EXCLUDE_START)
        #
        # 'analysis_partials' block: matches block of text starting e.g.
        # "Profile fitted partials:"
        # and ending with e.g.
        # " <I/sigma>   76.4   88.5   50.1   29.7   17.3    7.5    5.7    2.2"
        integration.defineBlock('analysis_partials',
                                "Profile fitted partials",
                                "I/sigma", include_flag=Magpie.EXCLUDE_START)
        # Reprocess
        integration.processText(self.__reassembleLogText('integration'))
        return integration

    def __parseStrategy(self):
        """Parse the section of the EDNA log for the strategy from BEST"""
        # Define a new processor to process this section
        strategy = Magpie.Magpie(verbose=self.__verbose)
        #
        # 'sweep' pattern: matches text of the form e.g.
        # "SWEEP 1:"
        # (It captures the sweep number from BEST)
        strategy.addPattern('sweep',
                            "SWEEP ([0-9]+):",
                            ['number'])
        #
        # 'resolution_reasoning' pattern: matches text of the form e.g.
        # "Resolution reasoning          : Resolution limit is set by ..."
        # (It captures the reasoning from BEST)
        strategy.addPattern('resolution_reasoning',
                            "Resolution reasoning +: (.*)$",
                            ['reasoning'])
        #
        # 'subwedges' block: matches block of text starting e.g.
        # "  N |  Phi_start |  N.of.images | Rot.width |  Exposure | ..."
        # and ending with a blank line
        # (It captures the information on the subwedges in the strategy)
        strategy.defineBlock('subwedges',
                             "  N | ", "",
                             include_flag=Magpie.EXCLUDE)
        #
        # 'collection_plan' block: matches block of text starting e.g.
        # "Attenuation                   :    1.0"
        # and ending with e.g.
        # "Ranking resolution            :   2.56 [A]"
        # (It captures the details of the collection plan)
        strategy.defineBlock('collection_plan',
                             "Attenuation", "Ranking resolution")
        #
        # Alternatively: match block of text starting e.g.
        # "Transmission                  : 23.947"
        # and ending with e.g.
        # "Ranking resolution            :   1.41 [A]"
        strategy.defineBlock('collection_plan',
                             "Transmission", "Ranking resolution")
        # 'predicted_stats' block: matches block of text starting e.g.
        # "Predicted statistics:"
        # and ending with e.g.
        # "Multiplicity                  :    3.1"
        # (It captures the basic predicted statistics for the strategy)
        strategy.defineBlock('predicted_stats',
                             "Predicted statistics:", "Multiplicity",
                             include_flag=Magpie.EXCLUDE_START)
        # 'statistics' block: matches block of text starting e.g.
        # "Statistics according to the plan:"
        # and ending with a blank line
        # (It captures the predicted statistics by resolution bin)
        strategy.defineBlock('statistics',
                             "Statistics according to the plan:", "",
                             include_flag=Magpie.EXCLUDE)
        # Reprocess
        strategy.processText(self.__reassembleLogText('strategy_best'))
        # Return the populated Magpie processor
        return strategy

    def __parseError(self):
        """Fetch any error messages found in the log file"""
        errors = []
        for error in self.__log['error']:
            errors.append(error['message'])
        return errors

    def __reassembleLogText(self, section):
        """Reassemble the lines for a section of EDNA log file

        This is a utility function that reassembles individual lines
        from a log that have been captured as data items in a Magpie.Magpie
        processor, and joins them together into a single block of text
        for reprocessing."""
        lines = []
        for data in self.__log[section]:
            lines.append(data['line'])
        text = '\n'.join(lines).strip('\n')
        return text

# EDNARunBuilder class
#
class EDNARunBuilder:
    """Create and populate an EDNARun object

    EDNARunBuilder is a utility class which should be used to create
    new EDNARun objects and populate them from the XML and log file
    output of an EDNA MX characterisation run.

    Typical usage:

    edna_run = EDNARunBuilder().setRunBasename(basename).EDNARun()"""

    def __init__(self):
        """Create a new EDNARunBuilder object"""
        self.__edna_run = EDNARun()
        self.__run_basename = None
        self.__input_xml_file = None
        self.__output_xml_file = None
        self.__log_file = None
        return

    def setRunBasename(self, run_basename):
        """Set the run basename for an EDNA run

        The run basename is the name of the top-level EDNA
        output directory. This method uses this to automatically
        determine the XML and log file names and other details
        of the EDNA run."""
        # Ensure it's an absolute path
        self.__run_basename = os.path.abspath(run_basename)
        self.__edna_run.run_basename = self.__run_basename
        # Check that the basename refers to a real directory
        if not os.path.isdir(self.__run_basename):
            print "*** ERROR ***"
            print "Directory " + str(run_basename) + " not found"
            self.__edna_run.error_code = RUN_BASENAME_DIR_NOT_FOUND
            self.__run_basename = None
            return self
        # Check the characterisation directory exists
        if not self.getCharacterisationDir():
            print "*** ERROR ***"
            print "Unable to locate Characterisation subdirectory"
            self.__edna_run.error_code = CHARACTERISATION_DIR_NOT_FOUND
            return self
        # Determine the prefix for input/output XML files
        edna_xml_prefix = self.getXmlPrefix()
        if not edna_xml_prefix:
            print "*** ERROR ***"
            print "Unable to determine the XML file prefix."
            self.__edna_run.error_code = UNDETERMINED_XML_PREFIX
            return self
        else:
            print "EDNA XML file prefix: " + str(edna_xml_prefix)
        # Set the data file names
        characterisation_dir = self.getCharacterisationDir()
        self.setInputXML(os.path.join(characterisation_dir,
                                      edna_xml_prefix + "dataInput.xml"))
        self.setOutputXML(os.path.join(characterisation_dir,
                                       edna_xml_prefix + "dataOutput.xml"))
        self.setLogFile(self.__run_basename + ".log")
        return self

    def setInputXML(self, input_xml_file):
        self.__input_xml_file = input_xml_file
        return self

    def setOutputXML(self, output_xml_file):
        self.__output_xml_file = output_xml_file
        return self

    def setLogFile(self, log_file):
        self.__log_file = log_file
        return self

    def getCharacterisationDir(self):
        """Determine the EDNA Characterisation subdirectory name

        Requires that the base name for the run has already been
        supplied, and tests all possible subdirectory names until
        a match is found.

        Returns the characterisation directory, or None if there is
        no match.

        NB Add new subdirectory names to the list of names to be
        tested."""
        # Can't operate without a run basename
        if not self.__run_basename: return None
        # Loop over all subdurectories
        for root, dirs, files in os.walk(self.__run_basename):
            if os.path.basename(root) == "Characterisation":
                characterisation_dir = root
                break
        if os.path.isdir(characterisation_dir):
            return characterisation_dir
#         Loop over possible subdir names
#        for subdir in ("EDPluginControlCCP4iv1_1",
#                       "ControlCCP4iv1_1",
#                       "ControlInterfacev1_2"):
#            characterisation_dir = os.path.join(self.__run_basename,
#                                                subdir,
#                                                "Characterisation")
#            if os.path.isdir(characterisation_dir):
#                return characterisation_dir
        # Didn't find a match
        return None

    def getXmlPrefix(self):
        """Determine the prefix for the EDNA XML files

        Requires that the base name for the run has already been
        supplied, and tests all possible prefixes until a match is
        found with the input XML file.

        (NB The match is tried against the input XML file because
        the output XML might not
        
        NB Add new prefixes to the list of prefixes to be tested."""
        # Can't operate without a characterisation directory
        characterisation_dir = self.getCharacterisationDir()
        if not characterisation_dir: return None
        # Loop over possible prefixes
        for prefix in ("EDPluginControlCharacterisationv1_1_",
                       "ControlCharacterisationv1_1_",
                       "ControlCharacterisationv12_",
                       "ControlCharacterisationv1_2_",
                       "ControlCharacterisationv1_3_"):
            if os.path.isfile(os.path.join(characterisation_dir,
                                           prefix + "dataInput.xml")):
                return prefix
        # Didn't find a match
        return None

    def __getAdditionalFiles(self):
        """Internal: collect additional files from the EDNA run

        Scans the characterisation subdirectories and stores the file
        names for additional files (mostly log files) in the EDNARun
        object."""
        # Acquire characterisation directory
        characterisation_dir = self.getCharacterisationDir()
        print "*** Collecting additional log files"
        characterisation_dir = self.getCharacterisationDir()
        if not characterisation_dir:
            # Warn and bail out
            print "*** WARNING no characterisation directory found"
            print "    Cannot acquire additional log files"
            return
        print "    Characterisation directory: " + str(characterisation_dir)
        #
        # Labelit distl logs
        #
        # Note that there can be multiple logs, so we need
        # to list the Labelit.distl directory, look for matching
        # names and then extract a trailing "index" in order
        # to build the full path for each of the files
        labelit_distl_dir = os.path.join(characterisation_dir,
                                       "Indexing", "ControlImageQualityIndicatorsv1_0")
        if os.path.isdir(labelit_distl_dir):
            for dirn in os.listdir(labelit_distl_dir):
                for integration_prefix in ("LabelitDistlv1_1-",):
                    if str(os.path.basename(dirn)).\
                           startswith(integration_prefix):
                        index = str(os.path.basename(dirn)).split('-')[1]
                        labelit_distl_log = os.path.join(labelit_distl_dir,
                                                              dirn,
                                                              integration_prefix + \
                                                              index + ".log")
                        if os.path.isfile(labelit_distl_log):
                            print "    Labelit.distl log: " + \
                                  str(labelit_distl_log)
                            self.__edna_run.labelit_distl_logs.append(
                                labelit_distl_log)
            # Finally: sort the list of Labelit.distl logs into order
            if len(self.__edna_run.labelit_distl_logs):
                self.__edna_run.labelit_distl_logs.sort()
            else:
                print "    *** NO LABELIT DISTL LOGS FOUND ***"
        # Mosflm indexing log
        mosflm_indexing_log = None
        for log in (os.path.join(characterisation_dir,
                                 "Indexing",
                                 "EDPluginControlIndexingMOSFLMv10",
                                 "EDPluginMOSFLMIndexingv10",
                                 "EDPluginMOSFLMIndexingv10.log"),
                    os.path.join(characterisation_dir,
                                 "Indexing",
                                 "ControlIndexingMOSFLMv10",
                                 "MOSFLMIndexingv10",
                                 "MOSFLMIndexingv10.log"),
                    os.path.join(characterisation_dir,
                                 "Indexing",
                                 "MOSFLMIndexingv10",
                                 "MOSFLMIndexingv10.log")):
            if os.path.isfile(log):
                mosflm_indexing_log = log
                print "    Mosflm indexing log: " + str(mosflm_indexing_log)
                self.__edna_run.mosflm_indexing_log = mosflm_indexing_log
                break
        if not mosflm_indexing_log:
            print "    Mosflm indexing log: *** NOT FOUND ***"
        # Labelit indexing log
        labelit_indexing_log = None
        log = os.path.join(characterisation_dir,
                                 "IndexingLabelit",
                                 "LabelitIndexingv1_1",
                                 "LabelitIndexingv1_1.log")
        if os.path.isfile(log):
            labelit_indexing_log = log
            print "    Labelit indexing log: " + str(labelit_indexing_log)
            self.__edna_run.labelit_indexing_log = labelit_indexing_log
        if not labelit_indexing_log:
            print "    Labelit indexing log: *** NOT FOUND ***"
        #
        # Mosflm integration logs
        #
        # Note that there can be multiple logs, so we need
        # to list the Integration directory, look for matching
        # names and then extract a trailing "index" in order
        # to build the full path for each of the files
        integration_dir = os.path.join(characterisation_dir,
                                       "Integration")
        for dirn in os.listdir(integration_dir):
            for integration_prefix in ("EDPluginMOSFLMIntegrationv10-",
                                       "MOSFLMIntegrationv10-"):
                if str(os.path.basename(dirn)).\
                       startswith(integration_prefix):
                    index = str(os.path.basename(dirn)).split('-')[1]
                    mosflm_integration_log = os.path.join(integration_dir,
                                                          dirn,
                                                          integration_prefix + \
                                                          index + ".log")
                    if os.path.isfile(mosflm_integration_log):
                        print "    Mosflm integration log: " + \
                              str(mosflm_integration_log)
                        self.__edna_run.mosflm_integration_logs.append(
                            mosflm_integration_log)
        # Finally: sort the list of Mosflm integration logs into order
        if len(self.__edna_run.mosflm_integration_logs):
            self.__edna_run.mosflm_integration_logs.sort()
        else:
            print "    *** NO MOSFLM INTEGRATION LOGS FOUND ***"
        #
        # Raddose
        raddose_log = None
        for log in (os.path.join(characterisation_dir,
                                 "Strategy",
                                 "EDPluginRaddosev10",
                                 "EDPluginRaddosev10.log"),
                    os.path.join(characterisation_dir,
                                 "Strategy",
                                 "Raddosev10",
                                 "Raddosev10.log")):
            if os.path.isfile(log):
                raddose_log = log
                print "    Raddose log: " + str(raddose_log)
                self.__edna_run.raddose_log = raddose_log
                break
        if not raddose_log:
            print "    Raddose log: *** NOT FOUND ***"
        #
        # Best
        best_log = None
        for log in (os.path.join(characterisation_dir,
                                 "Strategy",
                                 "EDPluginBestv1_2",
                                 "best.log"),
                    os.path.join(characterisation_dir,
                                 "Strategy",
                                 "Bestv1_2",
                                 "best.log")):
            if os.path.isfile(log):
                best_log = log
                print "    Best log: " + str(best_log)
                self.__edna_run.best_log = best_log
                break
        if not best_log:
            print "    Best log: *** NOT FOUND ***"
        best_plots = None
        for plotfile in (os.path.join(characterisation_dir,
                                      "Strategy",
                                      "EDPluginBestv1_2",
                                      "EDPluginBestv1_2_plots.mtv"),
                         os.path.join(characterisation_dir,
                                      "Strategy",
                                      "Bestv1_2",
                                      "Bestv1_2_plots.mtv")):
            if os.path.isfile(plotfile):
                best_plots = plotfile
                print "    Best plots: " + str(best_plots)
                self.__edna_run.best_plots = best_plots
                break
        if not best_plots:
            print "    Best plots: *** NOT FOUND ***"
        return

    def EDNARun(self):
        """Return the populated EDNARun object

        'input_xml_file' is the name of the input XML data file used
        in the EDNA MX characterisation run, while 'output_xml_file'
        and 'log_file' are the XML and log output files respectively."""
        # Make a new EDNARun object
        print "==== Extracting information from EDNA run ===="
        # Process the supplied files and build intermediate data structures
        input_xml = None
        output_xml = None
        output_log = None
        if self.__input_xml_file:
            print "Input XML : " + str(self.__input_xml_file)
            if os.path.isfile(self.__input_xml_file):
                self.__edna_run.data_input_xml = self.__input_xml_file
                input_xml = parseEDNAXML(self.__input_xml_file)
            else:
                print "*** WARNING input XML file not found"
        if self.__output_xml_file:
            print "Output XML: " + str(self.__output_xml_file)
            if os.path.isfile(self.__output_xml_file):
                self.__edna_run.data_output_xml = self.__output_xml_file
                output_xml = parseEDNAXML(self.__output_xml_file)
            else:
                print "*** WARNING output XML file not found"
        if self.__log_file:
            print "Log file  : " + str(self.__log_file)
            if os.path.isfile(self.__log_file):
                self.__edna_run.log_file = self.__log_file
                output_log = EDNALogData(self.__log_file)
            else:
                print "*** WARNING log file not found"
        # Populate with data from the supplied files
        if input_xml:
            try:
                self.setDiffractionPlan(input_xml)
                self.setSample(input_xml)
                self.__edna_run.input_xml_ok = True
            except Exception:
                # Some error extracting data from input XML
                print "*** WARNING exception raised when processing input XML"
                print "    Some data may be missing"
        if output_xml:
            try:
                self.setIndexingResultFromXML(output_xml)
                self.setIntegrationResults(output_xml)
                self.setStrategySweeps(output_xml)
                self.setPredictionImages(output_xml)
                self.setStrategyStatistics(output_xml)
                # Set data that can be deduced
                self.setOverallStrategyData()
                self.setImageTemplate()
                if self.__edna_run.has_data_collection and \
                       self.__edna_run.has_indexing_result and \
                       self.__edna_run.has_prediction_result and \
                       self.__edna_run.has_strategy_result:
                    self.__edna_run.output_xml_ok = True
            except Exception:
                # Some error extracting data from output XML
                print "*** WARNING exception raised when processing output XML"
                print "    Some data may be missing:"
                print "Data collection: ", self.__edna_run.has_data_collection
                print "Indexing results: ", self.__edna_run.has_indexing_result
                print "Prediction results: ", self.__edna_run.has_prediction_result
                print "Strategy results: ", self.__edna_run.has_strategy_result 
        # Get missing information from log file, if possible
        if output_log:
            try:
                # Error message?
                errors = self.getLogErrors(output_log)
                if errors:
                    self.__edna_run.log_errors = errors
                # Other data
                if self.__edna_run.has_strategy_result:
                    # Collect overlap from log file
                    self.setSubwedgeOverlapFromLog(output_log)
                if self.__edna_run.has_integration_result:
                    # Collect any missing integration stats from log file
                    self.setIntegrationStatsFromLog(output_log)
                self.__edna_run.log_file_ok = True
            except Exception:
                # Some error extracting data from output XML
                print "*** WARNING exception raised when processing output XML"
                print "    Some data may be missing"
        # Look for additional log files
        if self.__run_basename: self.__getAdditionalFiles()
        # Return the populated EDNARun object
        print "====== Finished extracting information ======="
        return self.__edna_run

    def setDiffractionPlan(self, xml_data):
        """Set diffraction plan parameters retrieved from XML data

        'input_data_xml' is a SimpleXMLNode tree derived from the
        EDNA input XML file. The information retrieved from the XML
        will be stored in the EDNARun object 'edna_run'."""
        # Lookup table to translate BEST input into English
        complexity_lookup = {"none": "Single wedge",
                             "min" : "Few sub-wedges",
                             "full": "Many sub-wedges" }
        # Locate the input data in the XML
        diffractionPlan = xml_data.findNode("diffractionPlan")
        if diffractionPlan:
            # Multiplicity
            try:
                # Latest version of EDNA MXv1
                self.__edna_run.diffraction_plan.multiplicity = \
                    float(diffractionPlan.aimedMultiplicity.value)
            except AttributeError:
                # May be an older version where "Multiplicity"
                # is spelt "Multyplicity"?
                try:
                    self.__edna_run.diffraction_plan.multiplicity = \
                       float(diffractionPlan.aimedMultyplicity.value)
                except AttributeError:
                    pass
            # I over sigma
            try:
                self.__edna_run.diffraction_plan.i_over_sigma = \
                    float(diffractionPlan.\
                              aimedIOverSigmaAtHighestResolution.value)
            except AttributeError:
                pass
            # BEST complexity
            try:
                complexity = complexity_lookup[
                    str(diffractionPlan.complexity.value)]
                self.__edna_run.diffraction_plan.best_complexity = complexity
            except AttributeError:
                pass
            # Resolution
            try:
                self.__edna_run.diffraction_plan.resolution = \
                    float(diffractionPlan.aimedResolution.value)
            except AttributeError:
                pass
            # Forced spacegroup
            try:
                self.__edna_run.diffraction_plan.forced_spacegroup = \
                    str(diffractionPlan.forcedSpaceGroup.value)
            except AttributeError:
                pass
            # Anomalous strategy
            try:
                if type(diffractionPlan.anomalousData.value) == int:
                    if int(diffractionPlan.anomalousData.value):
                        self.__edna_run.diffraction_plan.anomalous_data = True
                    else:
                        self.__edna_run.diffraction_plan.anomalous_data = False
                else:
                    if diffractionPlan.anomalousData.value.lower() == "true":
                        self.__edna_run.diffraction_plan.anomalous_data = True
                    else:
                        self.__edna_run.diffraction_plan.anomalous_data = False
                    
            except AttributeError:
                pass

    def setSample(self, xml_data):
        """Set the sample information retrieved from the input XML data"""
        sample = xml_data.findNode("sample")
        if sample:
            try:
                self.__edna_run.sample.susceptibility = \
                    float(sample.susceptibility.value)
            except AttributeError:
                # No radiation damage information input
                return
            try:
                chemical_composition = sample.chemicalComposition
                self.__edna_run.sample.description = "Specified protein"
            except AttributeError:
                # No "chemicalComposition" data
                self.__edna_run.sample.description = "Average protein"

    def setImageTemplate(self):
        print "Deriving image template from list of images"
        image_names = []
        for subwedge in self.__edna_run.integration_ranges:
            for image in subwedge.images:
                image_names.append(image.name)
        self.__edna_run.image_template = makeTemplateFromImageNames(image_names)
        print "=> Template: " + str(self.__edna_run.image_template)

    def setIndexingResultFromXML(self, xml_data):
        # Image template
        self.__edna_run.image_template = "[missing from XML]"
        # Find the appropriate XML node
        indexingResult = xml_data.findNode("indexingResult")
        if not indexingResult:
            print "*** ERROR in setIndexingResultFromXML"
            print "    No <indexingResult> XML node"
            print "    Unable to get indexing data from XML"
            return
        else:
            self.__edna_run.has_indexing_result = True
        # Loop over all the solutions and store each one
        for soln in indexingResult.solution:
            crystal = soln.crystal
            # Dirty fix for labelit indexing...
            penalty_value = None
            try:
                penalty_value = int(soln.penalty.value)
            except Exception:
                penalty_value = -1
            self.__edna_run.indexing_results.addSolution(
                int(soln.number.value),
                int(soln.penalty.value),
                str(crystal.spaceGroup.name.value),
                float(crystal.cell.length_a.value),
                float(crystal.cell.length_b.value),
                float(crystal.cell.length_c.value),
                float(crystal.cell.angle_alpha.value),
                float(crystal.cell.angle_beta.value),
                float(crystal.cell.angle_gamma.value))
        # Reverse the order of the indexing solutions
        # NB This assumes that the solutions were already stored in
        # penalty order
        self.__edna_run.indexing_results.solutions.reverse()
        # Store selected indexing solution
        selectedSolution = indexingResult.selectedSolution
        self.__edna_run.indexing_results.setSelectedSolution(
            int(selectedSolution.number.value),
            str(selectedSolution.crystal.spaceGroup.name.value),
            float(selectedSolution.crystal.cell.length_a.value),
            float(selectedSolution.crystal.cell.length_b.value),
            float(selectedSolution.crystal.cell.length_c.value),
            float(selectedSolution.crystal.cell.angle_alpha.value),
            float(selectedSolution.crystal.cell.angle_beta.value),
            float(selectedSolution.crystal.cell.angle_gamma.value))
        # Additional data: numbers of spots etc
        statistics = selectedSolution.statistics
        self.__edna_run.indexing_results.number_of_spots_used = \
            int(statistics.spotsUsed.value)
        self.__edna_run.indexing_results.number_of_spots_total = \
            int(statistics.spotsTotal.value)
        self.__edna_run.indexing_results.spot_deviation_positional = \
            float(statistics.spotDeviationPositional.value)
        # Dirty fix for labelit indexing...
        spot_deviation_angular = None
        try:
            spot_deviation_angular = float(statistics.spotDeviationAngular.value)
        except Exception:
            spot_deviation_angular = -1.0
        self.__edna_run.indexing_results.spot_deviation_angular = \
            float(statistics.spotDeviationAngular.value)
        self.__edna_run.indexing_results.beam_shift_x = \
            float(statistics.beamPositionShiftX.value)
        self.__edna_run.indexing_results.beam_shift_y = \
            float(statistics.beamPositionShiftY.value)
        # Mosaicity
        self.__edna_run.indexing_results.estimated_mosaicity = \
            float(selectedSolution.crystal.mosaicity.value)

    def setPredictionImages(self, xml_data):
        """Find and store the diffraction image data from the EDNA XML"""
        # Find the relevant nodes in the XML
        predictionResult = xml_data.findNode("predictionResult")
        if not predictionResult:
            print "*** ERROR in setPredictionImages"
            print "    No <predictionResult> XML node"
            print "    Unable to get prediction data from XML"
            return
        else:
            self.__edna_run.has_prediction_result = True
        if self.__edna_run.has_indexing_result:
            indexingResult = xml_data.findNode("indexingResult")
        else:
            print "*** WARNING indexing result is missing"
            print "    Unable to gather prediction image data"
        # Locate the original images
        for indexing_image in indexingResult.image:
            i = int(indexing_image.number.value)
            path = str(indexing_image.path.value)
            # Locate the matching prediction image
            jpeg = None
            for prediction_image in predictionResult.predictionImage:
                if int(prediction_image.number.value) == i:
                    jpeg = str(prediction_image.path.value)
                    break
            # Store data as part of an integration range also
            image_name = os.path.basename(path)
            print "Assigning " + image_name + " to an integration range..."
            for integration_range in self.__edna_run.integration_ranges:
                for image in integration_range.images:
                    if image_name == image.name:
                        print "Image belongs to range " + \
                            str(integration_range.image_start) + \
                            "-" + \
                            str(integration_range.image_end)
                        image.jpeg = jpeg
                        break
        # Finished
        return

    def setIntegrationResults(self, xml_data):
        # Create integrations/subwedges by looping over the
        # subwedges defined in the "dataCollection" block
        print "Fetching integration results from XML"
        data_collection = xml_data.findNode("dataCollection")
        if not data_collection:
            print "*** ERROR in setIntegrationResults"
            print "    No <dataCollection> XML node"
            print "    Unable to get integration data from XML"
            return
        else:
            self.__edna_run.has_data_collection = True
        # Get total number of subwedges and make entries for each
        subwedge_nodes = []
        for subWedge in data_collection.childNodes():
            if subWedge.getNodeName() == "subWedge":
                # Add an integration range
                integration_range = self.__edna_run.addIntegrationRange()
                subwedge_nodes.append(subWedge)
                # Assign explicit subwedge number
                integration_range.subwedge_number = int(subWedge.
                                                        subWedgeNumber.
                                                        value)
        print "Found " + str(len(subwedge_nodes)) + " subwedges"
        # Populate the integration ranges
        for subWedge in subwedge_nodes:
            # Populate the integration range
            subwedge_number = int(subWedge.subWedgeNumber.value)
            print "*** Populating integration range for subwedge " + \
                  str(subwedge_number)
            # Look up the integration range
            for int_range in self.__edna_run.integration_ranges:
                if subwedge_number == int_range.subwedge_number:
                    # Found matching subwedge number
                    integration = int_range
                    break
            # Locate details for this range
            goniostat = subWedge.experimentalCondition.goniostat
            rotation_axis_start = float(goniostat.rotationAxisStart.value)
            rotation_axis_end = float(goniostat.rotationAxisEnd.value)
            print "    Rotation range: " + \
                  str(rotation_axis_start) + \
                  "-" + \
                  str(rotation_axis_end)
            integration.rotation_axis_start = rotation_axis_start
            integration.rotation_axis_end = rotation_axis_end
            # Images included in the range
            for image in subWedge.childNodes():
                if image.getNodeName() == "image":
                    image_number = int(image.number.value)
                    image_path = str(image.path.value)
                    image_name = os.path.basename(image_path)
                    print "    Image " + \
                          str(image_number) + \
                          ": " + \
                          image_name + \
                          " (" + \
                          image_path + \
                          ")"
                    # Add to the integration range
                    integration.addImage(image_name,
                                         image_number,
                                         image_path,
                                         None)
            # Start/end images
            # NB images might not be in order so we need to check
            # all image numbers and look for min and max
            image_start = integration.images[0].number
            image_end = integration.images[0].number
            for image in integration.images:
                image_number = image.number
                if image_number < image_start:
                    image_start = image_number
                elif image_number > image_end:
                    image_end = image_number
            integration.image_start = image_start
            integration.image_end = image_end
            print "    (Image range " + \
                  str(image_start) + \
                  " to " + \
                  str(image_end) + \
                  ")"
            # Derive the image template
            image_names = []
            for image in integration.images:
                image_names.append(image.name)
            integration.image_template = \
                                       makeTemplateFromImageNames(image_names)
            print "    Derived template: " + integration.image_template
        # Get the statistics for each subwedge/range
        # Loop over the subwedges defined under "integrationResult"
        # and assign RMS spot deviations in turn
        i = 0
        integration_result = xml_data.findNode("integrationResult")
        if not integration_result:
            print "*** ERROR in setIntegrationResults"
            print "    No <integrationResult> XML node"
            print "    Unable to get integration data from XML"
            return
        else:
            self.__edna_run.has_integration_result = True
        for subWedgeResult in integration_result.childNodes():
            if subWedgeResult.getNodeName() == "integrationSubWedgeResult":
                # Internal counter for implicit subwedge number
                i += 1
                # Subwedge number
                try:
                    subwedge_number = int(subWedgeResult.subWedgeNumber.value)
                    print "*** Collecting statistics for subwedge " + \
                          str(subwedge_number)
                    # Look up the matching integration range
                    for int_range in self.__edna_run.integration_ranges:
                        if subwedge_number == int_range.subwedge_number:
                            # Found matching subwedge number
                            integration = int_range
                            break
                except AttributeError:
                    # Older XML doesn't have the subwedge number
                    subwedge_number = self.__edna_run.\
                                      integration_ranges[i].\
                                      subwedge_number
                    print "*** Collecting statistics for assumed subwedge " + \
                          str(subwedge_number) + \
                          " (" + str(i) + "'th subwedge)"
                    print "    (no explicit subwedge number found in XML)"
                integration = self.__edna_run.integration_ranges[i - 1]
                # Numbers of reflections
                # Note these might not be present in older XML files
                statistics = subWedgeResult.statistics
                try:
                    try:
                        integration.fully_recorded_reflns = int(statistics.
                                          numberOfFullyRecordedReflections.
                                          value)
                    except AttributeError:
                        # First version of XML was broken, "Recorded" was
                        # mispelt as "Recorderd" - try this instead
                        integration.fully_recorded_reflns = int(statistics.
                                          numberOfFullyRecorderdReflections.
                                          value)
                    integration.negative_reflns = int(statistics.
                                          numberOfNegativeReflections.
                                          value)
                    integration.overlapped_reflns = int(statistics.
                                         numberOfOverlappedReflections.
                                         value)
                    integration.partially_recorded_reflns = int(statistics.
                                         numberOfPartialReflections.
                                         value)
                    integration.bad_reflns = int(statistics.
                                         numberOfBadReflections.
                                         value)
                except AttributeError:
                    # Older XML doesn't have these defined
                    # Print a warning but otherwise ignore
                    print "    *** WARNING cannot find number of reflection statistics from XML"

                # RMS spot deviation
                integration.rms_spot_deviation = float(statistics.
                                                       RMSSpotDeviation.
                                                       value)
                # Binned data by resolution
                # Loop over statisticsPerResolutionBin
                for resoln in subWedgeResult.childNodes():
                    if resoln.getNodeName() == "statisticsPerResolutionBin":
                        # Get initial data items
                        max_resoln = float(resoln.maxResolution.value)
                        min_resoln = float(resoln.minResolution.value)
                        partials = resoln.profileFitted.partials
                        full = resoln.profileFitted.fullyRecorded
                        # New resolution bin in data structure
                        rbin = integration.addAnalysisResolnBin(max_resoln)
                        # Store data
                        rbin.n_fully_recorded = int(full.numberOfReflections.value)
                        rbin.i_fully_recorded = float(full.averageIntensity.value)
                        rbin.i_over_sigma_fully_recorded = float(full.averageIOverSigma.value)
                        rbin.n_partials = int(partials.numberOfReflections.value)
                        rbin.i_partials = float(partials.averageIntensity.value)
                        rbin.i_over_sigma_partials = float(partials.averageIOverSigma.value)
                # Check that some data was acquired
                if not integration.analysis_by_resoln:
                    # Older XML doesn't have these defined
                    print "    *** WARNING cannot find binned stats in XML"
                    continue
                # Test: report values
                print "               Fully recorded         Partials"
                print "     Resoln    N     <I> <I/sig>      N     <I> <I/sig>"
                for rbin in integration.analysis_by_resoln:
                    print "    % 4.2f % 6.0f % 7.0f % 7.1f % 6.0f % 7.0f % 7.1f" % \
                              (rbin.resolution,
                               rbin.n_fully_recorded,
                               rbin.i_fully_recorded,
                               rbin.i_over_sigma_fully_recorded,
                               rbin.n_partials,
                               rbin.i_partials,
                               rbin.i_over_sigma_partials)
                # Derive statistics
                # Overall I/sigma and I/sigma in highest resolution shell
                #
                # NB Overall I/sigma is derived by summing the average
                # I/sigma in each bin multiplied by the number of reflections
                # in that bin, then dividing the total by the total number
                # of reflections
                print "    Deriving I/sigma stats..."
                resoln_max = None
                i_over_sigma_highest_resoln_fulls = None
                i_over_sigma_highest_resoln_partials = None
                i_over_sigma_overall_fulls = 0.0
                i_over_sigma_overall_partials = 0.0
                n_reflns_fulls = 0
                n_reflns_partials = 0
                for rbin in integration.analysis_by_resoln:
                    # I/sigma in highest resolution bin
                    if not i_over_sigma_highest_resoln_fulls or \
                           rbin.resolution < resoln_max:
                        resoln_max = rbin.resolution
                        i_over_sigma_highest_resoln_fulls = \
                                            rbin.i_over_sigma_fully_recorded
                        i_over_sigma_highest_resoln_partials = \
                                            rbin.i_over_sigma_partials
                    # Overall I/sigma
                    i_over_sigma_overall_fulls += rbin. \
                                                  i_over_sigma_fully_recorded * \
                                                  rbin.n_fully_recorded
                    n_reflns_fulls += rbin.n_fully_recorded
                    i_over_sigma_overall_partials += rbin. \
                                                     i_over_sigma_partials * \
                                                     rbin.n_partials
                    n_reflns_partials += rbin.n_partials
                # Calculate means
                try:
                    i_over_sigma_overall_fulls = i_over_sigma_overall_fulls / \
                                                 n_reflns_fulls
                except ZeroDivisionError:
                    print "*** WARNING unable to calculate I/sigma overall"
                    print "    for fully recorded reflections."
                    print "    No fully recorded reflections?"
                    i_over_sigma_overall_fulls = None
                try:
                    i_over_sigma_overall_partials = \
                                               i_over_sigma_overall_partials / \
                                               n_reflns_partials
                except ZeroDivisionError:
                    print "*** WARNING unable to calculate I/sigma overall"
                    print "    for partially recorded reflections."
                    print "    No partially recorded reflections?"
                    i_over_sigma_overall_partials = None
                # Print the values for diagnostics
                print "    I/sigma (highest resolution): " + \
                      str(i_over_sigma_highest_resoln_fulls) + \
                      "\t" + \
                      str(i_over_sigma_highest_resoln_partials)
                print "    I/sigma (overall)           : " + \
                      str(i_over_sigma_overall_fulls) + \
                      "\t" + \
                      str(i_over_sigma_overall_partials)
                # Store the derived statistics
                integration.i_over_sigma_overall_fulls = \
                                                   i_over_sigma_overall_fulls
                integration.i_over_sigma_highest_resoln_fulls = \
                                            i_over_sigma_highest_resoln_fulls
                integration.i_over_sigma_overall_partials = \
                                            i_over_sigma_overall_partials
                integration.i_over_sigma_highest_resoln_partials = \
                                          i_over_sigma_highest_resoln_partials

    def setIntegrationStatsFromLog(self, log_data):
        # Attempt to extract data from the log file for statistics
        # that might be missing from older versions of the EDNA XML
        #
        # Test whether we need to collect any missing data
        missing_data = False
        for integration in self.__edna_run.integration_ranges:
            # Check for number of fully recorded reflections
            # as a test for whether the numbers of reflections
            # need to be collected
            if not integration.fully_recorded_reflns:
                missing_data = True
                break
            # Test number of bins as a test for collecting the
            # binned statistics
            if not integration.analysis_by_resoln:
                missing_data = True
                break
        # Bail if no data appears to be missing
        if not missing_data: return
        # The integration results in the log file are by blocks of
        # contiguous images as far as I can tell
        # Determine the number of blocks
        print "*** WARNING: fetching missing integration stats from log file"
        n_ranges = len(log_data.integration['image_range'])
        for i in range(0, n_ranges):
            print "=> Deriving statistics for range " + str(i + 1)
            integration = self.__edna_run.integration_ranges[i]
            # Extract and store data
            #
            # Number of reflections
            data = Magpie.Tabulator(str(
                    log_data.integration['statistics'][i]), ':')
            if not integration.fully_recorded_reflns:
                integration.fully_recorded_reflns = \
                int(data['Number of fully recorded reflections'][1])
            if not integration.partially_recorded_reflns:
                integration.partially_recorded_reflns = \
                int(data['Number of partials'][1])
            if not integration.overlapped_reflns:
                integration.overlapped_reflns = \
                int(data['Number of overlapped reflections'][1])
            if not integration.negative_reflns:
                integration.negative_reflns = \
                int(data['Number of reflections with negative intensity'][1])
            if not integration.bad_reflns:
                integration.bad_reflns = \
                int(data['Number of bad reflections'][1])
            #
            # I/sigma data etc
            data = Magpie.Tabulator(str(
                    log_data.integration['i_over_sigma'][i]), ':')
            if not integration.i_over_sigma_overall:
                integration.i_over_sigma_overall = \
                float(data['Average I/sigma overall'][1])
            if not integration.i_over_sigma_highest_resoln:
                integration.i_over_sigma_highest_resoln = \
                float(data['Average I/sigma at highest resolution'][1])
            # 
            # Analysis by resolution
            # Get resolution bins first
            if not integration.analysis_by_resoln:
                resoln_data = \
                     log_data.integration['analysis_by_resolution'][i]['bins']
                for resoln in resoln_data.split():
                    integration.addAnalysisResolnBin(resoln)
                # Data for fully recorded spots
                fulls_data = Magpie.Tabulator(str(
                    log_data.integration['analysis_fully_recorded'][i]), None)
                # Data for partially recorded spots
                partials_data = Magpie.Tabulator(str(
                    log_data.integration['analysis_partials'][i]), None)
                # Store all the data
                j = 0
                for bin in integration.analysis_by_resoln:
                    j += 1
                    bin.n_fully_recorded = fulls_data['Number'][j]
                    bin.i_fully_recorded = fulls_data['<I>'][j]
                    bin.i_over_sigma_fully_recorded = fulls_data['<I/sigma>'][j]
                    bin.n_partials = partials_data['Number'][j]
                    bin.i_partials = partials_data['<I>'][j]
                    bin.i_over_sigma_partials = partials_data['<I/sigma>'][j]
        # Finished with log file
        return

    def setStrategySweeps(self, xml_data):
        """Find and store the sweeps from the EDNA output XML"""
        # Each sweep corresponds to a collection plan
        print "Fetching collection plan from XML"
        strategy_result = xml_data.findNode("strategyResult")
        if not strategy_result:
            print "*** ERROR in setStrategySweeps"
            print "    No <strategyResult> XML node"
            print "    Unable to get strategy data from XML"
            return
        else:
            self.__edna_run.has_strategy_result = True
        for plan in strategy_result.childNodes():
            if plan.getNodeName() == "collectionPlan":
                sweep = self.__edna_run.strategy.addSweep()
                sweep.number = int(plan.collectionPlanNumber.value)
                print "*** Adding sweep " + str(sweep.number) + ".."
                # Add subwedges
                for subWedge in plan.collectionStrategy.childNodes():
                    if subWedge.getNodeName() == "subWedge":
                        subwedge = sweep.addSubwedge()
                        subwedge.number = int(subWedge.subWedgeNumber.value)
                        print "*** Adding subwedge " + str(subwedge.number) + ".."
                        # Over-ride value in the XML file
                        subwedge.rotation_axis = ROTATION_AXIS_NAME
                        # Get data for this subwedge
                        #
                        # Goniostat-related data
                        goniostat = subWedge.experimentalCondition.goniostat
                        subwedge.rotation_start = \
                            float(goniostat.rotationAxisStart.value)
                        subwedge.rotation_end = \
                            float(goniostat.rotationAxisEnd.value)
                        subwedge.rotation_width = \
                            float(goniostat.oscillationWidth.value)
                        # Beam-related data
                        beam = subWedge.experimentalCondition.beam
                        subwedge.exposure = float(beam.exposureTime.value)
                        subwedge.transmission = float(beam.transmission.value)
                        # Detector-related data
                        detector = subWedge.experimentalCondition.detector
                        subwedge.distance = float(detector.distance.value)
                        # Derive number of images per subwedge
                        print "    Deriving # of images for subwedge"
                        subwedge.number_of_images = \
                            int((subwedge.rotation_end - \
                                     subwedge.rotation_start) / \
                                    subwedge.rotation_width)
                # Do a check - should have at least one subwedge
                if not len(sweep.subwedges):
                    print "    *** ERROR in setStrategySweeps: no subwedges" + \
                          " found for sweep ***"
                else:
                    # Calculate total rotation range for the sweep
                    print "    Calculating total rotation range " + \
                          "and number of images for sweep"
                    sweep.total_number_of_images = 0
                    sweep_rotation_start = sweep.subwedges[0].rotation_start
                    sweep_rotation_end = sweep.subwedges[0].rotation_end
                    for subwedge in sweep.subwedges:
                        if subwedge.rotation_start < sweep_rotation_start:
                            sweep_rotation_start = subwedge.rotation_start
                        if subwedge.rotation_end > sweep_rotation_end:
                            sweep_rotation_end = subwedge.rotation_end
                        sweep.total_number_of_images += \
                            subwedge.number_of_images
                    sweep.total_rotation_range = \
                        sweep_rotation_end - sweep_rotation_start
        # Do a check - should have at least one sweep
        if not len(self.__edna_run.strategy.sweeps):
            print "*** ERROR in setStrategySweeps: no sweeps found ***"

    def getLogErrors(self, log_data):
        """Check for error messages from the log"""
        print "Checking for errors in the log"
        if not log_data.errors:
            print "No errors found"
        else:
            for error in log_data.errors:
                print "*** ERROR: " + str(error)
        return log_data.errors

    def setSubwedgeOverlapFromLog(self, log_data):
        """Find and store the subwedge strategy data from the EDNA log"""
        print "Adding overlap data to subwedges using log data"
        for i in range(0, len(self.__edna_run.strategy.sweeps)):
            # Locate the sweep
            for sweep in self.__edna_run.strategy.sweeps:
                if sweep.number == i + 1: break
            print "=> Sweep " + str(sweep.number) + ".."
            # Use a Tabulator to split up the "subwedges" data extracted
            # from the log file
            subwedge_data = Magpie.Tabulator(
                str(log_data.strategy['subwedges'][i]), '|')
            # Each row of tabulated data is a subwedge
            for data in subwedge_data:
                j = int(data[0])
                print "   Subwedge " + str(j)
                # Locate the subwedge
                for subwedge in sweep.subwedges:
                    if subwedge.number == j: break
                subwedge.overlap = data[6]
        return

    def setStrategyStatistics(self, xml_data):
        print "Fetching detailed statistics for each sweep from XML"
        nsweeps = len(self.__edna_run.strategy.sweeps)
        if not self.__edna_run.has_strategy_result:
            # The data is missing, warn and bail out
            print "*** WARNING already determined that this data is missing"
            print "    from the XML file - skipped"
            return
        strategy_result = xml_data.findNode("strategyResult")
        if nsweeps == 1:
            collection_plans = [strategy_result.collectionPlan]
        else:
            collection_plans = strategy_result.collectionPlan
        for i in range(0, nsweeps):
            # Each collection plan corresponds to a sweep
            print "=> Sweep " + str(i + 1) + ".."
            sweep = self.__edna_run.strategy.sweeps[i]
            plan = collection_plans[i]
            # Strategy summary
            strategy_summary = plan.strategySummary
            # Resolution reasoning
            sweep.resolution_reasoning = \
                str(strategy_summary.resolutionReasoning.value)
            print "   " + sweep.resolution_reasoning
            # Resolution
            sweep.resolution = float(strategy_summary.resolution.value)
            sweep.ranking_resolution = \
                float(strategy_summary.rankingResolution.value)
            # Total exposure and collection times
            sweep.total_exposure_time = \
                float(strategy_summary.totalExposureTime.value)
            sweep.total_data_collection_time = \
                float(strategy_summary.totalDataCollectionTime.value)
            # Predicted statistics
            sweep.predicted_stats.completeness = \
                float(strategy_summary.completeness.value) * 100.0
            sweep.predicted_stats.i_over_sigma = \
                float(strategy_summary.iSigma.value)
            sweep.predicted_stats.multiplicity = \
                float(strategy_summary.redundancy.value)
            # Statistics by resolution bin
            strategy_stats = plan.statistics
            stats = sweep.predicted_stats
            for resoln_bin in strategy_stats.resolutionBin:
                bin = stats.addData()
                bin.max_resolution = float(resoln_bin.maxResolution.value)
                bin.min_resolution = float(resoln_bin.minResolution.value)
                bin.completeness = float(resoln_bin.completeness.value) * 100.0
                bin.intensity = float(resoln_bin.averageIntensity.value)
                bin.sigma = float(resoln_bin.averageSigma.value)
                bin.i_over_sigma = float(resoln_bin.IOverSigma.value)
                # FIXME some bug with <I>/<sigma> not present in all bins?
                ##bin.average_i_over_average_sigma = float(
                ##    resoln_bin.averageIntensityOverAverageSigma.value)
                bin.rfactor = float(resoln_bin.rFactor.value)
                bin.overload = float(resoln_bin.percentageOverload.value)
                bin.redundancy = float(resoln_bin.redundancy.value)
            # Reset data for last (overall) bin
            bin = sweep.predicted_stats.resolution_bins[-1]
            bin.min_resolution = "Overall"
            bin.max_resolution = None
            # Overall I/sigma
            sweep.predicted_stats.i_over_sigma_overall = bin.i_over_sigma

    def setOverallStrategyData(self):
        """Set the overall data for each strategy

        Where a strategy consists of a single sweep, the overall
        data (completeness, multiplicity etc) are the same as the
        predicted statistics for that sweep.

        Where there are multiple sweeps, the overall data is taken
        from the highest resolution sweep."""
        # Check that the necessary data was already found
        if not self.__edna_run.has_strategy_result:
            print "*** WARNING unable to set overall strategy data"
            print "    The relevant data is missing from the XML"
            return
        # Locate the highest resolution sweep
        highest_resolution_sweep = None
        for sweep in self.__edna_run.strategy.sweeps:
            if not highest_resolution_sweep:
                highest_resolution_sweep = sweep
            else:
                if sweep.resolution < highest_resolution_sweep.resolution:
                    highest_resolution_sweep = sweep
        # Copy data from highest resolution sweep
        self.__edna_run.strategy.strategy_resolution = \
                        highest_resolution_sweep.resolution
        self.__edna_run.strategy.ranking_resolution = \
                        highest_resolution_sweep.ranking_resolution
        self.__edna_run.strategy.predicted_completeness = \
                        highest_resolution_sweep.predicted_stats.completeness
        self.__edna_run.strategy.predicted_i_over_sigma = \
                        highest_resolution_sweep.predicted_stats.i_over_sigma
        self.__edna_run.strategy.predicted_i_over_sigma_overall = \
                 highest_resolution_sweep.predicted_stats.i_over_sigma_overall
        self.__edna_run.strategy.predicted_multiplicity = \
                        highest_resolution_sweep.predicted_stats.multiplicity
        # Sum numbers of images and times etc across all sweeps
        self.__edna_run.strategy.total_number_of_images = 0
        self.__edna_run.strategy.total_exposure_time = 0.0
        self.__edna_run.strategy.total_data_collection_time = 0.0
        for sweep in self.__edna_run.strategy.sweeps:
            self.__edna_run.strategy.total_number_of_images += \
                        sweep.total_number_of_images
            self.__edna_run.strategy.total_exposure_time += \
                        sweep.total_exposure_time
            self.__edna_run.strategy.total_data_collection_time += \
                        sweep.total_data_collection_time
        # Finished
        return

# EDNARun class
#
class EDNARun:
    """Class representing an EDNA MX characterisation run"""
    def __init__(self):
        self.title = None
        self.run_basename = None
        # Input files
        self.data_input_xml = None
        self.data_output_xml = None
        # Status of the run
        self.has_data_collection = False
        self.has_indexing_result = False
        self.has_integration_result = False
        self.has_prediction_result = False
        self.has_strategy_result = False
        # Log files for each stage
        self.log_file = None
        self.mosflm_indexing_log = None
	self.labelit_indexing_log = None
        self.mosflm_integration_logs = []
        self.labelit_distl_logs = []
        self.raddose_log = None
        self.best_log = None
        self.best_plots = None
        # Actual data from the run
        self.diffraction_plan = DiffractionPlan()
        self.sample = Sample()
        self.indexing_results = IndexingResults()
        self.image_template = '[not set]'
        self.integration_ranges = []
        self.strategy = Strategy()
        # Internal flags indicating status
        self.input_xml_ok = False
        self.output_xml_ok = False
        self.log_file_ok = False
        self.error_code = NO_ERROR
        # Error messages detected in log file
        self.log_errors = None

    def addIntegrationRange(self):
        integration_range = IntegrationRange()
        self.integration_ranges.append(integration_range)
        return integration_range

    def isComplete(self):
        """Check whether the data in the  EDNARun object is complete"""
        return (self.input_xml_ok and self.output_xml_ok)

# DiffractionPlan class
#
class DiffractionPlan:
    """Class representing an EDNA MX characterisation diffraction plan"""
    def __init__(self):
        self.multiplicity = None
        self.i_over_sigma = None
        self.best_complexity = None
        self.resolution = None
        self.forced_spacegroup = None
        self.anomalous_data = None

# Sample class
#
class Sample:
    """Class representing the sample properties input into the EDNA MX run"""
    def __init__(self):
        self.description = "n/a"
        self.susceptibility = None

# Image class
#
class Image:
    """Class representing an image used in an EDNA MX characterisation"""
    def __init__(self, name, number, path, jpeg):
        self.name = name
        self.number = number
        self.path = path
        self.jpeg = jpeg

# IntegrationRange class
#
class IntegrationRange:
    """Class representing a range of images integrated together"""
    def __init__(self):
        self.subwedge_number = None
        self.image_directory = None
        self.image_template = None
        self.image_start = None
        self.image_end = None
        self.rotation_axis = ROTATION_AXIS_NAME
        self.rotation_axis_start = None
        self.rotation_axis_end = None
        self.fully_recorded_reflns = None
        self.partially_recorded_reflns = None
        self.overlapped_reflns = None
        self.negative_reflns = None
        self.bad_reflns = None
        self.rms_spot_deviation = None
        self.i_over_sigma_overall = None # NB redundant
        self.i_over_sigma_highest_resoln = None # NB redundant
        self.i_over_sigma_overall_fulls = None
        self.i_over_sigma_highest_resoln_fulls = None
        self.i_over_sigma_overall_partials = None
        self.i_over_sigma_highest_resoln_partials = None
        self.images = []
        self.analysis_by_resoln = []

    def addImage(self, name, number, path, jpeg):
        image = Image(name, number, path, jpeg)
        self.images.append(image)
        return image

    def addAnalysisResolnBin(self, resoln):
        new_bin = IntegrationAnalysisResolnBin()
        new_bin.resolution = resoln
        self.analysis_by_resoln.append(new_bin)
        return new_bin

class IntegrationAnalysisResolnBin:
    """Single resolution bin for analysis by resolution from integration step"""
    def __init__(self):
        self.resolution = None
        self.n_fully_recorded = None
        self.i_fully_recorded = None
        self.i_over_sigma_fully_recorded = None
        self.n_partials = None
        self.i_partials = None
        self.i_over_sigma_partials = None

# IndexingResults class
#
class IndexingResults:
    """Class representing indexing results from an EDNA MX characterisation"""
    def __init__(self):
        self.solutions = []
        self.selected_solution_number = None
        self.spacegroup = None
        self.cell_a = None
        self.cell_b = None
        self.cell_c = None
        self.cell_alpha = None
        self.cell_beta = None
        self.cell_gamma = None
        self.number_of_spots_used = None
        self.number_of_spots_total = None
        self.spot_deviation_positional = None
        self.spot_deviation_angular = None
        self.beam_shift_x_y = None
        self.beam_shift_x = None
        self.beam_shift_y = None
        self.estimated_mosaicity = None
    def addSolution(self, index, penalty, lattice, a, b, c, alpha, beta, gamma):
        soln = IndexingSolution(index, penalty, lattice, a, b, c, alpha, beta, gamma)
        self.solutions.append(soln)
        return soln
    def setSelectedSolution(self, index, spacegroup, a, b, c, alpha, beta, gamma):
        self.selected_solution_number = index
        self.spacegroup = spacegroup
        self.cell_a = a
        self.cell_b = b
        self.cell_c = c
        self.cell_alpha = alpha
        self.cell_beta = beta
        self.cell_gamma = gamma

# IndexingSolution class
#
class IndexingSolution:
    """Class representing an individual indexing solution"""
    def __init__(self, index, penalty, lattice, a, b, c, alpha, beta, gamma):
        self.index = index
        self.penalty = penalty
        self.lattice = lattice
        self.cell_a = a
        self.cell_b = b
        self.cell_c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

# Strategy class
#
class Strategy:
    """Represents a strategy result from an EDNA MX characterisation run"""
    def __init__(self):
        self.strategy_resolution = None
        self.ranking_resolution = None
        self.predicted_completeness = None
        self.predicted_i_over_sigma = None
        self.predicted_i_over_sigma_overall = None
        self.predicted_multiplicity = None
        self.total_number_of_images = None
        self.total_exposure_time = None
        self.total_data_collection_time = None
        self.sweeps = []

    def addSweep(self):
        sweep = StrategySweep()
        self.sweeps.append(sweep)
        return sweep

class StrategySweep:
    """Data collection sweep data from an EDNA MX characterisation run"""
    def __init__(self):
        self.number = None
        self.resolution_reasoning = None
        self.total_rotation_range = None
        self.total_number_of_images = None
        self.total_exposure_time = None
        self.total_data_collection_time = None
        self.resolution = None
        self.ranking_resolution = None
        self.predicted_stats = StrategyStatistics()
        self.subwedges = []

    def addSubwedge(self):
        subwedge = StrategySubwedge()
        self.subwedges.append(subwedge)
        return subwedge

class StrategySubwedge:
    """Subwedge from BEST in an EDNA MX characterisation run"""
    def __init__(self):
        self.number = None
        self.rotation_axis = ROTATION_AXIS_NAME
        self.rotation_start = None
        self.rotation_end = None
        self.rotation_width = None
        self.number_of_images = None
        self.exposure = None
        self.distance = None
        self.overlap = None
        self.transmission = None

class StrategyStatistics:
    """Predicted statistics from BEST in an EDNA MX characterisation run"""
    def __init__(self):
        self.completeness = None
        self.i_over_sigma = None
        self.i_over_sigma_overall = None
        self.multiplicity = None
        self.resolution_bins = []

    def addData(self):
        resolution_bin = StrategyStatisticsResolutionBin()
        self.resolution_bins.append(resolution_bin)
        return resolution_bin

# StrategyStatisticsResolutionBin class
#
class StrategyStatisticsResolutionBin:
    """Represents statistical data for a resolution bin for a strategy"""
    def __init__(self):
        self.max_resolution = None
        self.min_resolution = None
        self.completeness = None
        self.intensity = None
        self.sigma = None
        self.i_over_sigma = None
        self.average_i_over_average_sigma = None
        self.rfactor = None
        self.overload = None
        self.redundancy = None

# ErrorReporter class
#
class ErrorReporter:
    """Build the contents of an error report document and render to HTML

    The ErrorReporter class is used to generate an error page when no
    strategy output is available from any of the EDNA runs supplied to
    it."""

    def __init__(self, edna2htmldir, edna_html_dir, edna_runs):
        """Create a new ErrorReporter instance

        'edna2htmldir' is the path to the EDNA2html home directory,
        'edna_runs' is the list of populated EDNARun objects."""
        # Generate a document reporting the errors
        self.__doc = Canary.Document("EDNA2html: failure report")
        self.__doc.addStyle(os.path.join(edna2htmldir, "EDNA2html.css"),
                            Canary.INLINE)
        self.__doc.addPara(Canary.MakeImg(os.path.join(edna_html_dir,
                                                       "warning.png")) + \
                           " EDNA2html failed to complete successfully",
                           css_class="error")
        if len(edna_runs) == 0:
            # Failure mode: No runs supplied
            self.__doc.addPara("No runs were supplied")
        else:
            # Failure mode: No runs could be processed
            self.__doc.addPara(str(len(edna_runs)) + 
                               " run(s) were supplied but none " + \
                               "could be processed:")
            run_list = self.__doc.addList()
            # Loop over runs and write diagnostics
            for edna_run in edna_runs:
                diag = self.addFailureDiagnostics(edna_run)
                run_list.addItem(Canary.MakeLink(diag))
        # Add the footer (time, version numbers etc)
        addFooter(self.__doc)
        # Copy the warning icon
        CopyIcons(['warning.png'],
                  os.path.join(edna2htmldir, "icons"),
                  edna_html_dir)

    def addFailureDiagnostics(self, edna_run):
        """Add diagnostic section for a failed EDNA run

        'edna_run' is a populated EDNARun object from which the
        diagnostic information is taken."""
        title = os.path.basename(str(edna_run.run_basename))
        diag = self.__doc.addSection(title)
        diag.addCSSClass("failure_diagnostic")
        addEDNAFailureSummary(diag, edna_run, Help(None))
        return diag

    def renderFile(self, html_file):
        """Write the HTML error document to file"""
        self.__doc.renderFile(html_file)

#######################################################################
# Module Functions
#######################################################################

def version():
    """Return the version of the EDNA2html module"""
    return __version__

def parseEDNAXML(xml_file):
    """Parse an EDNA XML file and return a SimpleXMLNode tree

    Use a SAX parser with an EDNAXMLHandler object to create and
    return a SimpleXMLNode tree representing the XML file contents."""
    handler = EDNAXMLHandler()
    xml.sax.parse(open(xml_file), handler)
    return handler.getSimpleXMLNodeTree()

def makePortableFileCopy(source_file, target_dir):
    if not source_file: return source_file
    target_file = os.path.join(target_dir, os.path.basename(source_file))
    CopyFile(source_file, target_file)
    return target_file

def makeResizedImage(image_file_in, image_file_out, height, width):
    # Make a resized version of the supplied image file
    # using ImageMagick "convert"
    print "Making resized copy of .../" + os.path.basename(image_file_in)
    p = subprocess.Popen(["convert",
                          str(image_file_in),
                          "-resize",
                          str(width) + "x" + str(height),
                          str(image_file_out)])
    return p.wait()

def getImageDimensions(image):
    # Get the image height and width using ImageMagick "identify"
    # Returns a list with width and height
    print "Getting dimenions of .../" + os.path.basename(image)
    p = subprocess.Popen(["identify",
                          "-format",
                          "%wx%h",
                          str(image)],
                         stdout=subprocess.PIPE)
    p.wait()
    geometry = p.stdout.read().strip().split('x')
    return geometry

def convertTimeToMinutes(t):
    """Convert time from seconds into min:sec string format for display

    't' is a number of seconds; this function will return a string
    showing t as minutes and seconds in the format min:sec."""
    mins = int(t / 60.0)
    secs = t % 60.0
    return "%d:%04.1f" % (mins, secs)


def CopyFile(source, target):
    # Copy file 'source' to 'target'
    try:
        shutil.copy(source, target)
    except Exception:
        print "CopyFile: copy operation " + \
            str(source) + " -> " + str(target) + " failed"

def makeTemplateFromImageNames(image_names):
    # 'image_names' is an iterable which gives a list
    # of names of images
    # This function attempts to create a template name
    # by comparing the names that are supplied
    if len(image_names) == 1: return image_names[0]
    template = image_names[0]
    for image in image_names[1:]:
        new_template = ''
        for i in range(0, len(template)):
            if image[i] == template[i]:
                new_template += template[i]
            else:
                new_template += '#'
        template = new_template
    return template


def populateStrategySummaryTable(doc,
                                 summary_table,
                                 edna_html_dir,
                                 ranking_mode,
                                 edna_runs,
                                 strategy_folder_id,
                                 tab_ids):
    # Constuct the sortable table summarising the strategies
    # from each run
    #
    if len(edna_runs) > 1:
        # Build the framework for the sortable table 
        # This has the header with clickable links
        #
        # NB IF YOU CHANGE THE TEXT OF THE TABLE HEADERS HERE THEN
        # NOTE THAT YOU WILL ALSO NEED TO CHANGE THE TEXT IN THE
        # JAVASCRIPT CODE SWITCH STATEMENT FOR THE SORTABLE TABLE
        # TO FUNCTION - THE TEXT MUST MATCH EXACTLY
        js_cmd = "return sortTable(this);"
        summary_header = [Jackdaw.JavascriptLink("Run #", js_cmd),
                          Jackdaw.JavascriptLink("Predicted completeness (%)",
                                                 js_cmd),
                          Jackdaw.JavascriptLink("Predicted I/sigma", js_cmd),
                          Jackdaw.JavascriptLink("Predicted I/sigma (overall)",
                                                 js_cmd),
                          Jackdaw.JavascriptLink("Predicted multiplicity",
                                                 js_cmd),
                          Jackdaw.JavascriptLink("# of images", js_cmd),
                          Jackdaw.JavascriptLink("Total exposure time (min:sec)",
                                                 js_cmd),
                          Jackdaw.JavascriptLink("Total collection time (min:sec)",
                                                 js_cmd),
                          Jackdaw.JavascriptLink("Maximum resolution (A)",
                                                 js_cmd)]
        if ranking_mode:
            # Also display the ranking resolution
            summary_header.insert(1, Jackdaw.JavascriptLink(
                "Ranking resolution (A)", js_cmd))
    else:
        # Only one run so build the framework without links
        # (i.e. non-sortable table)
        summary_header = ["Run #",
                          "Predicted completeness (%)",
                          "Predicted I/sigma",
                          "Predicted I/sigma (overall)",
                          "Predicted multiplicity",
                          "# of images",
                          "Total exposure time (min:sec)",
                          "Total collection time (min:sec)",
                          "Maximum resolution (A)"]
        if ranking_mode:
            # Also display the ranking resolution
            summary_header.insert(1, "Ranking resolution (A)")
    # Also need description column?
    for edna_run in edna_runs:
        if edna_run.title:
            summary_header.append("Description")
            break
    summary_table.setHeader(summary_header)
    # Add tool tips to the summary table
    if len(edna_runs) > 1:
        summary_help = [help.sort_run_number,
                        help.sort_predicted_completeness,
                        help.sort_predicted_i_over_sigma,
                        help.sort_predicted_i_over_sigma_overall,
                        help.sort_predicted_multiplicity,
                        help.sort_total_number_of_images,
                        help.sort_total_exposure_time,
                        help.sort_total_collection_time,
                        help.sort_strategy_resolution,
                        help.strategy_description]
        if ranking_mode:
            summary_help.insert(1, help.sort_ranking_resolution)
    else:
        summary_help = [help.run_number,
                        help.predicted_completeness,
                        help.predicted_i_over_sigma,
                        help.predicted_i_over_sigma_overall,
                        help.predicted_multiplicity,
                        help.total_number_of_images,
                        help.total_exposure_time,
                        help.total_collection_time,
                        help.strategy_resolution,
                        help.strategy_description]
        if ranking_mode:
            summary_help.insert(1, help.ranking_resolution)
    summary_table.addHelpToHeader(summary_help)
    # Add an id to the table body element
    # (used in Javascript to reference the table)
    summary_table.setTBodyId("strategyData")

    # Make a Javascript file with the data for the strategies
    strategy_js_file = os.path.join(edna_html_dir, "strategy.js")
    strategy_js = open(strategy_js_file, "w")
    # Write name of tabbed folder
    strategy_js.write("setTabbedFolderId('%s');\n" % strategy_folder_id)
    # Write data for each strategy
    irun = 0
    for edna_run in edna_runs:
        irun += 1
        this_strategy = edna_run.strategy
        if len(this_strategy.sweeps) > 1:
            multi_sweep = Canary.JS_TRUE
        else:
            multi_sweep = Canary.JS_FALSE
        try:
            strategy_js.write("addStrategy(%d,%.2f,%.2f,%.2f,%.2f,%.2f,%d,%.2f,%.2f,%.2f,%s,%s,%s);\n" % \
                              (irun,
                               this_strategy.ranking_resolution,
                               this_strategy.predicted_completeness,
                               this_strategy.predicted_i_over_sigma,
                               this_strategy.predicted_i_over_sigma_overall,
                               this_strategy.predicted_multiplicity,
                               this_strategy.total_number_of_images,
                               this_strategy.total_exposure_time,
                               this_strategy.total_data_collection_time,
                               this_strategy.strategy_resolution,
                               multi_sweep,
                               "'" + str(edna_run.title) + "'",
                               tab_ids[irun - 1]))
        except Exception:
            print "*** Failed to add summary info to the sortable table"
            strategy_js.write("addFailedStrategy(%d,%s);\n" % \
                              (irun, tab_ids[irun - 1]))
    # Help for elements in each row
    strategy_js.write("setHelp('%s','%s');\n" % ('run', help.run_number))
    strategy_js.write("setHelp('%s','%s');\n" % ('ranking_resolution',
                                                 help.ranking_resolution))
    strategy_js.write("setHelp('%s','%s');\n" % ('completeness',
                                                 help.predicted_completeness))
    strategy_js.write("setHelp('%s','%s');\n" % ('ioversigma',
                                                 help.predicted_i_over_sigma))
    strategy_js.write("setHelp('%s','%s');\n" % ('ioversigmaoverall',
                                                 help.predicted_i_over_sigma_overall))
    strategy_js.write("setHelp('%s','%s');\n" % ('multiplicity',
                                                 help.predicted_multiplicity))
    strategy_js.write("setHelp('%s','%s');\n" % ('nimages',
                                                 help.total_number_of_images))
    strategy_js.write("setHelp('%s','%s');\n" % ('exposuretime',
                                                 help.total_exposure_time))
    strategy_js.write("setHelp('%s','%s');\n" % ('collectiontime',
                                                 help.total_collection_time))
    strategy_js.write("setHelp('%s','%s');\n" % ('strategy_resolution',
                                                 help.strategy_resolution))
    strategy_js.write("setHelp('%s','%s');\n" % ('description',
                                                 help.strategy_description))
    strategy_js.close()
    # Include this file in the final document
    doc.addScript(strategy_js_file, Canary.INLINE)

def addStrategySummary(section, edna_run, ranking_mode, edna_html_dir, help):
    # Title
    if edna_run.title: section.addPara(edna_run.title,
                                       css_class="strategy_title")
    # Check if it was complete
    if not edna_run.isComplete():
        section.addPara(Canary.MakeImg(os.path.join(edna_html_dir,
                                                    "warning.png")) + \
                        " There was an error processing this run - " + \
                        "some data may be missing", css_class="error")
        addEDNAFailureSummary(section, edna_run, help)
        return

    # Details of inputs
    addEDNAInputsTable(section, edna_run, help)

    # Collection plan
    addStrategyCollectionPlan(section, edna_run, help)

    # Strategy details (i.e. predicted overall multiplicity etc)
    addStrategyDetails(section, edna_run, help)

    # Log files
    addEDNAOutputFilesTable(section, edna_run, help)

    # Predicted statistics
    addStrategyPredictedStats(section, edna_run, help)

    # Optional indexing and spot prediction results
    if ranking_mode:
        # Add indexing and spot prediction specifically for this run
        indexing_and_prediction = section.addSubsection()
        addIndexingSummary(edna_run, indexing_and_prediction, edna_html_dir,
                           help)
        addPredictionSummary(edna_run, indexing_and_prediction, edna_html_dir,
                             help)

    # Links to the master log and XML files
    addStrategyFileList(edna_run, section, help)

def addEDNAFailureSummary(section, edna_run, help):
    """Write diagnostics for a failed EDNA run

    'edna_run' is a populated EDNARun object from which the
    diagnostic information is taken."""
    # Check that there was input and output
    if edna_run.data_input_xml:
        if not edna_run.input_xml_ok:
            section.addPara("Unable to process input XML file",
                            css_class="warning")
        if not edna_run.data_output_xml:
            section.addPara("No output XML file found: EDNA MXv1 " + \
                            "characterisation failed to finish?",
                            css_class="warning")
        elif not edna_run.output_xml_ok:
            section.addPara("Unable to process output XML file: EDNA MxV1 " + \
                            "characterisation failed to produce a strategy?",
                            css_class="warning")
    else:
        section.addPara("No input XML file found", css_class="warning")
    # Error code from the run processing?
    errmsg = lookupErrorCode(edna_run.error_code)
    if errmsg: section.addPara(errmsg, css_class="warning")
    # Any error messages from log file?
    if edna_run.log_errors:
        section.addPara("Error messages detected in master log file:")
        errors = section.addList()
        for err_msg in edna_run.log_errors:
            errors.addItem(err_msg)
    # Run basename
    if edna_run.run_basename:
        section.addPara("Base directory for this run: " +
                        Canary.MakeLink(edna_run.run_basename))
    # Input files
    section.addPara("The following files were used as input:")
    addStrategyFileList(edna_run, section, help)
    # Table indicating which sections weren't processed
    section.addPara("The table indicates which data from the run were found:")
    err_tbl = section.addTable(["Data", "Status", "Log file"])
    # Data collection
    err_tbl.addRow(["Data collection",
                    str(edna_run.has_data_collection),
                    "n/a"])
    # Indexing
    row = ["Indexing result", str(edna_run.has_indexing_result)]
    if edna_run.mosflm_indexing_log:
        row.append(Canary.MakeLink(edna_run.mosflm_indexing_log,
                                   "Mosflm indexing log"))
    else:
        row.append("Mosflm indexing log: not found")
    err_tbl.addRow(row)
    # Prediction
    err_tbl.addRow(["Prediction result",
                    str(edna_run.has_prediction_result),
                    "n/a"])
    # Integration
    row = ["Integration result", str(edna_run.has_integration_result)]
    integration_logs = []
    for log_file in edna_run.mosflm_integration_logs:
        integration_logs.append(Canary.MakeLink(log_file,
                                                "Mosflm integration log"))
    if integration_logs:
        row.append("<br />".join(integration_logs))
    else:
        row.append("Mosflm integration log: not found")
    err_tbl.addRow(row)
    # Strategy
    row = ["Strategy result", str(edna_run.has_strategy_result)]
    if edna_run.best_log:
        row.append(Canary.MakeLink(edna_run.best_log,
                                   "Best log"))
    else:
        row.append("Best log: not found")
    err_tbl.addRow(row)
    # Return the section
    return section

def addEDNAInputsTable(section, edna_run, help):
    """Add a summary of the inputs to EDNA to a document section

    Creates a table in the Canary document section supplied as
    'section', and populates with the input data from the EDNARun
    object 'edna_run'.

    Use the data in the Help object 'help' to populate the table
    tool-tips."""
    # Details of inputs
    inputs = section.addTable(["Inputs to EDNA", None, ""])
    inputs.addRow(['Target resolution',
                   'Target multiplicity',
                   'Target I/&sigma;',
                   'Sample composition',
                   'Radiation sensitivity',
                   'Requested strategy complexity',
                   'Anomalous data'],
                  css_classes="inputs_table_header")
    inputs.addClass("inputs")
    inputs.addClassToColumn(0, "first_child")
    row = [str(edna_run.diffraction_plan.resolution),
           str(edna_run.diffraction_plan.multiplicity),
           str(edna_run.diffraction_plan.i_over_sigma),
           'n/a',
           'n/a',
           str(edna_run.diffraction_plan.best_complexity),
           '?']
    # Report Raddose inputs
    # NOTE THAT IF THE ORDER OR NUMBER OF COLUMNS IN THE INPUTS
    # TABLE CHANGES, THE COLUMN INDICES MAY ALSO NEED TO CHANGE
    # HERE:
    if edna_run.sample.susceptibility:
        row[3] = edna_run.sample.description
        row[4] = edna_run.sample.susceptibility
    if edna_run.sample.description == "Specified protein":
        # Add a link to Raddose log, if found
        if edna_run.raddose_log:
            row[3] += " " + Canary.MakeLink(edna_run.raddose_log,
                                          "(see Raddose log)")
    # Report anomalous data
    # NOTE THAT IF THE ORDER OR NUMBER OF COLUMNS IN THE INPUTS
    # TABLE CHANGES, THE COLUMN INDEX MAY ALSO NEED TO CHANGE
    # HERE:
    if edna_run.diffraction_plan.anomalous_data:
        row[6] = "Yes"
    else:
        row[6] = "No"
    inputs.addRow(row)
    # Add tool tips to the inputs table
    inputs.addTitle(help.inputs_table_title)
    inputs.addHelpToColumn(0, help.target_resolution, Canary.ALL_ROWS)
    inputs.addHelpToColumn(1, help.target_multiplicity, Canary.ALL_ROWS)
    inputs.addHelpToColumn(2, help.target_i_over_sigma, Canary.ALL_ROWS)
    inputs.addHelpToColumn(3, help.sample_composition, Canary.ALL_ROWS)
    inputs.addHelpToColumn(4, help.radiation_susceptibility, Canary.ALL_ROWS)
    inputs.addHelpToColumn(5, help.requested_strategy_complexity,
                           Canary.ALL_ROWS)
    # Return the table
    return inputs

def addStrategyCollectionPlan(section, edna_run, help):
    """Write table(s) summarising the collection plan for a strategy

    Adds one or more tables (one table per sweep) to the Canary
    document section 'section', summarising the details of the
    collection plan predicted by the strategy in the EDNARun object
    'edna_run'.

    The Help object 'help' is used to populate the tool-tip help for
    the tables."""
    axis = edna_run.strategy.sweeps[0].subwedges[0].rotation_axis
    nsweeps = len(edna_run.strategy.sweeps)
    for sweep in edna_run.strategy.sweeps:
        plan = section.addTable(["Collection Plan",
                                 None,
                                 sweep.resolution_reasoning])
        plan.addClass("collection_plan")
        if nsweeps > 1:
            # Write header for sweep if there are multiple sweeps
            plan.setHeader(["Sweep " + str(sweep.number)])
        # Subwedges
        plan.addRow([None,
                     "Inputs for data collection software",
                     None,
                     None,
                     None,
                     None,
                     None,
                     "Additional details",
                     None],
                    css_classes="table_header")
        plan.addRow(["Subwedge",
                     axis.title() + " start (&deg;)",
                     "Rotation width (&deg;)",
                     "Number of images",
                     "Exposure (s)",
                     "Maximum resolution (&Aring;)",
                     "Relative transmission (%)",
                     "Distance (mm)",
                     "Overlap"],
                    css_classes="table_header")
        for subwedge in sweep.subwedges:
            plan.addRow([subwedge.number,
                         '%.2f' % subwedge.rotation_start,
                         '%.2f' % subwedge.rotation_width,
                         subwedge.number_of_images,
                         '%.2f' % subwedge.exposure,
                         '%.2f' % sweep.resolution,
                         subwedge.transmission,
                         '%.1f' % subwedge.distance,
                         subwedge.overlap],
                        css_classes="subwedge")
        # Add initial CSS classes to columns for styling later
        plan.addClassToColumn(0, "first_child")
        for col in range(1, 7): plan.addClassToColumn(col, "GDA_inputs")
        for col in range(7, 9): plan.addClassToColumn(col, "additional_info")
        # Add tool tip help to the table
        # The order is a little convoulted but is necessary to assure
        # that the correct text is assigned to each cell
        plan.addHelpToHeader([help.sweep_number,
                              None,
                              help.resolution_reasoning])
        plan.addHelpToColumn(0, help.subwedge_number, Canary.ALL_ROWS)
        plan.addHelpToColumn(1, help.omega_start, Canary.ALL_ROWS)
        plan.addHelpToColumn(2, help.rotation_width, Canary.ALL_ROWS)
        plan.addHelpToColumn(3, help.number_of_images, Canary.ALL_ROWS)
        plan.addHelpToColumn(4, help.exposure, Canary.ALL_ROWS)
        plan.addHelpToColumn(5, help.maximum_resolution, Canary.ALL_ROWS)
        plan.addHelpToColumn(6, help.transmission, Canary.ALL_ROWS)
        plan.addHelpToColumn(7, help.distance, Canary.ALL_ROWS)
        plan.addHelpToColumn(8, help.overlap, Canary.ALL_ROWS)
        plan.addHelpToRow(0, help.additional_details, Canary.ALL_COLUMNS)
        plan.addHelpToRow(0, [help.subwedge_number,
                             help.data_collection_software_inputs])

def addStrategyDetails(section, edna_run, help):
    """Write table summarising the predicted details for a strategy

    Adds a table to the Canary document section 'section', summarising
    the details of the strategy (predicted multiplicity, completeness
    etc) for each sweep in the collection plan stored in the EDNARun
    object 'edna_run'.

    The Help object 'help' is used to populate the tool-tip help for
    the tables."""
    # Populate table of strategy details and predicted statistics
    strategy_details = section.addTable()
    strategy_details.addClass("strategy_details")
    strategy_details.addColumn(['Total rotation range (&deg;)',
                                'Total number of images',
                                'Total exposure time (min:sec)',
                                'Total data collection time (min:sec)',
                                'Ranking resolution (&Aring;)',
                                'Predicted Statistics',
                                'Completeness (%)',
                                'I/sigma (highest resolution)',
                                'Multiplicity'],
                               header='Strategy details')
    strategy_details.addClassToRow(5, "table_header")
    nsweeps = len(edna_run.strategy.sweeps)
    i = 0
    column_header = None
    for sweep in edna_run.strategy.sweeps:
        i += 1
        predicted_stats = sweep.predicted_stats
        if nsweeps > 1:
            column_header = "Sweep " + str(i)
        # Convert times to min:sec format for display
        exposure_time = convertTimeToMinutes(sweep.total_exposure_time)
        collection_time = convertTimeToMinutes(sweep.total_data_collection_time)
        strategy_details.addColumn(['%.2f' % sweep.total_rotation_range,
                                    sweep.total_number_of_images,
                                    '%s' % exposure_time,
                                    '%s' % collection_time,
                                    sweep.ranking_resolution,
                                    None,
                                    predicted_stats.completeness,
                                    predicted_stats.i_over_sigma,
                                    '%.1f' % predicted_stats.multiplicity],
                                   header=column_header)
        # Add tool tips
        strategy_details.addHelpToRow(0, help.strategy_total_rotation_range,
                                      Canary.ALL_COLUMNS)
        strategy_details.addHelpToRow(1, help.strategy_total_number_of_images,
                                      Canary.ALL_COLUMNS)
        strategy_details.addHelpToRow(2, help.strategy_total_exposure_time,
                                      Canary.ALL_COLUMNS)
        strategy_details.addHelpToRow(3,
                                      help.strategy_total_data_collection_time,
                                      Canary.ALL_COLUMNS)
        strategy_details.addHelpToRow(4, help.strategy_ranking_resolution,
                                      Canary.ALL_COLUMNS)
        strategy_details.addHelpToRow(6, help.strategy_completeness,
                                      Canary.ALL_COLUMNS)
        strategy_details.addHelpToRow(7, help.strategy_i_over_sigma,
                                      Canary.ALL_COLUMNS)
        strategy_details.addHelpToRow(8, help.strategy_multiplicity,
                                      Canary.ALL_COLUMNS)

def addStrategyPredictedStats(section, edna_run, help):
    """Write tables summarising the predicted statistics for a strategy

    Adds tables (one per sweep) inside ToggleFolders to the Canary
    document section 'section', showing the predicted statistics as
    a function of resolution bin for the strategy stored in the EDNARun
    object 'edna_run'.

    The Help object 'help' is used to populate the tool-tip help for
    the tables."""
    # Populate table of predicted statistics
    nsweeps = len(edna_run.strategy.sweeps)
    i = 0
    column_header = None
    for sweep in edna_run.strategy.sweeps:
        i += 1
        # Full statistics for each sweep in the strategy
        folder = section.addContent(Jackdaw.ToggleFolder(doc))
        folder.addCSSClass("clear")
        strategy_stats = folder.addContent(Canary.Table())
        # Build table header
        # Construct two rows to act as header rows
        strategy_stats.addRow(["Resolution",
                               None,
                               "Completeness",
                               "Average",
                               None,
                               "I/Sigma",
                               "R-factor",
                               "Overload"], css_classes="table_header")
        strategy_stats.addRow(["Lower",
                               "Upper",
                               "%",
                               "Intensity",
                               "Sigma",
                               "",
                               "%",
                               "%"], css_classes="table_header")
        for resoln_bin in sweep.predicted_stats.resolution_bins:
            strategy_stats.addRow([resoln_bin.min_resolution,
                                   resoln_bin.max_resolution,
                                   resoln_bin.completeness,
                                   '%d' % resoln_bin.intensity,
                                   '%d' % resoln_bin.sigma,
                                   resoln_bin.i_over_sigma,
                                   resoln_bin.rfactor,
                                   resoln_bin.overload])
        # Add a class to the final row (overall stats)
        nrows = strategy_stats.nRows()
        strategy_stats.addClassToRow(nrows - 1, "overall_stats")
        # Add tool tip help
        strategy_stats.addHelpToColumn(0, help.lower_resolution, Canary.ALL_ROWS)
        strategy_stats.addHelpToColumn(1, help.upper_resolution, Canary.ALL_ROWS)
        strategy_stats.addHelpToColumn(2, help.completeness, Canary.ALL_ROWS)
        strategy_stats.addHelpToColumn(3, help.average_intensity,
                                       Canary.ALL_ROWS)
        strategy_stats.addHelpToColumn(4, help.average_sigma, Canary.ALL_ROWS)
        strategy_stats.addHelpToColumn(5, help.i_over_sigma, Canary.ALL_ROWS)
        strategy_stats.addHelpToColumn(6, help.rfactor, Canary.ALL_ROWS)
        strategy_stats.addHelpToColumn(7, help.overload, Canary.ALL_ROWS)
        strategy_stats.addHelpToRow(nrows - 1, [help.statistics_overall])
        # Configure the folder status and controls
        if nsweeps == 1:
            # Single sweep
            open_link_text = "Show detailed statistics by resolution bin.."
            close_link_text = "Hide detailed statistics.."
        else:
            # Multiple sweeps
            open_link_text = "Show detailed statistics by resolution bin " + \
                "for sweep " + str(i) + ".."
            close_link_text = "Hide detailed statistics " + \
                "for sweep " + str(i) + ".."
        folder.addOpenLinkText(Canary.MakeImg(
                os.path.join(edna_html_dir, "closed.png")) + " " + open_link_text,
                               help_text=help.show_statistics_by_resolution)
        folder.addCloseLinkText(Canary.MakeImg(
                os.path.join(edna_html_dir, "open.png")) + " " + close_link_text,
                               help_text=help.hide_statistics_by_resolution)
        folder.closedByDefault()

def addEDNAOutputFilesTable(section, edna_run, help):
    """Write table summarising the output files from an EDNA run

    Adds a table to the Canary document section 'section' summarising
    the log files associated with the EDNA run stored in the EDNARun
    object 'edna_run'.

    The Help object 'help' is used to populate the tool-tip help for
    the tables."""
    file_tbl = section.addTable()

    # Populate table of external files
    file_tbl.addClass("log_files")
    file_tbl.setHeader(["Associated files", ""])
    # Labelit.distl logs
    if edna_run.labelit_distl_logs:
        file_tbl.addRow(["Image quality indicators"],
                        css_classes="characterisation_stage")
        for filn in edna_run.labelit_distl_logs:
            file_tbl.addRow(["Labelit.distl log",
                             Canary.MakeLink(filn, os.path.basename(filn))])
            file_tbl.addHelpToRow(file_tbl.nRows() - 1,
                                  help.integration_log, Canary.ALL_COLUMNS)
    # Mosflm indexing log
    if edna_run.mosflm_indexing_log:
        file_tbl.addRow(["Indexing"],
                        css_classes="characterisation_stage")
        file_tbl.addRow(["Mosflm indexing log",
                         Canary.MakeLink(edna_run.mosflm_indexing_log,
                                         os.path.basename(
                                             edna_run.mosflm_indexing_log))])
        file_tbl.addHelpToRow(file_tbl.nRows() - 1,
                              help.indexing_log, Canary.ALL_COLUMNS)
    # Labelit indexing log
    if edna_run.labelit_indexing_log:
        file_tbl.addRow(["Labelit indexing log",
                         Canary.MakeLink(edna_run.labelit_indexing_log,
                                         os.path.basename(
                                             edna_run.labelit_indexing_log))])
        file_tbl.addHelpToRow(file_tbl.nRows() - 1,
                              help.indexing_log, Canary.ALL_COLUMNS)
    # Mosflm integration logs
    if edna_run.mosflm_integration_logs:
        file_tbl.addRow(["Integration"],
                        css_classes="characterisation_stage")
        for filn in edna_run.mosflm_integration_logs:
            file_tbl.addRow(["Mosflm integration log",
                             Canary.MakeLink(filn, os.path.basename(filn))])
            file_tbl.addHelpToRow(file_tbl.nRows() - 1,
                                  help.integration_log, Canary.ALL_COLUMNS)
    # Raddose
    if edna_run.raddose_log:
        file_tbl.addRow(["Radiation damage"],
                        css_classes="characterisation_stage")
        file_tbl.addRow(["Raddose log",
                         Canary.MakeLink(edna_run.raddose_log,
                                         os.path.basename(
                                             edna_run.raddose_log))])
        file_tbl.addHelpToRow(file_tbl.nRows() - 1,
                              help.raddose_log, Canary.ALL_COLUMNS)
    # Best
    if edna_run.best_log:
        file_tbl.addRow(["Strategy generation"],
                        css_classes="characterisation_stage")
        file_tbl.addRow(["Best log",
                         Canary.MakeLink(edna_run.best_log,
                                         os.path.basename(edna_run.best_log))])
        file_tbl.addHelpToRow(file_tbl.nRows() - 1,
                              help.best_log, Canary.ALL_COLUMNS)
        file_tbl.addRow(["Best plot file",
                         Canary.MakeLink(edna_run.best_plots,
                                         os.path.basename(
                                             edna_run.best_plots))])
        file_tbl.addHelpToRow(file_tbl.nRows() - 1,
                              help.best_plots, Canary.ALL_COLUMNS)
    # Make the first column special
    file_tbl.addClassToColumn(0, "first_child")
    # Return the file table
    return file_tbl

def addIndexingSummary(edna_run, section, edna_html_dir, help):
    # Write out a summary of the indexing results from the
    # supplied EDNA run into a subsection of the specified
    # document section
    #
    # Convenience variable for the indexing data
    indexing_results = edna_run.indexing_results

    # Show details of the selected solution
    # Spacegroup
    indexing_summary = section.addSubsection("Indexing summary")
    indexing_summary.addHelp(help.indexing_summary)
    indexing_summary.addCSSClass("indexing_summary")
    # Selected and requested spacegroup
    indexing_summary.addPara("<span class='selected_spacegroup'>" +
                             "Selected spacegroup: " +
                             Canary.makeToolTip(indexing_results.spacegroup,
                                                help.selected_spacegroup) +
                             "</span> " +
                             "<span class='requested_spacegroup'>(" +
                             "Requested spacegroup: " +
                             Canary.makeToolTip(
            edna_run.diffraction_plan.forced_spacegroup,
            help.requested_spacegroup) +
                             ")</span>")
    # Refined cell
    solution_cell_tbl = indexing_summary.addTable(
        ["Refined unit cell parameters (&Aring;/degrees)"])
    solution_cell_tbl.addRow(["a", "b", "c", "&alpha", "&beta", "&gamma"],
                             css_classes="table_header")
    solution_cell_tbl.addRow(['%.2f' % indexing_results.cell_a,
                              '%.2f' % indexing_results.cell_b,
                              '%.2f' % indexing_results.cell_c,
                              '%.2f' % indexing_results.cell_alpha,
                              '%.2f' % indexing_results.cell_beta,
                              '%.2f' % indexing_results.cell_gamma])
    solution_cell_tbl.addTitle(help.refined_unit_cell)

    # Add the table of all possible solutions but make it
    # togglable so that the user can view it if they like
    folder = indexing_summary.addContent(Jackdaw.ToggleFolder(doc))
    folder.addOpenLinkText(Canary.MakeImg(
            os.path.join(edna_html_dir, "closed.png")) +
                           " Show all possible indexing solutions..",
                            help_text=help.show_indexing_solutions)
    folder.addCloseLinkText(Canary.MakeImg(
            os.path.join(edna_html_dir, "open.png")) +
                            " Hide indexing solutions..",
                            help_text=help.hide_indexing_solutions)
    folder.closedByDefault()
    folder.addContent(Canary.Para(
               Canary.makeToolTip(
        "The selected solution (" +
        str(indexing_results.selected_solution_number) +
        ") is highlighted in green",
            help.selected_indexing_solution),
        css_class="selected_solution"))
    indexing_tbl = folder.addContent(Canary.Table())
    indexing_tbl.addRow(['',
                         None,
                         None,
                         'Cell parameters before refinement'],
                        css_classes="table_header table_header1")
    indexing_tbl.addRow(['Solution',
                         'Penalty',
                         'Lattice',
                         'a',
                         'b',
                         'c',
                         '&alpha;',
                         '&beta;',
                         '&gamma;'],
                        css_classes="table_header")
    # Write out the table of indexing solutions
    for soln in indexing_results.solutions:
        row = [soln.index,
               soln.penalty,
               soln.lattice,
               '%.2f' % soln.cell_a,
               '%.2f' % soln.cell_b,
               '%.2f' % soln.cell_c,
               '%.2f' % soln.alpha,
               '%.2f' % soln.beta,
               '%.2f' % soln.gamma]
        if soln.index == indexing_results.selected_solution_number:
            indexing_tbl.addRow(row, css_classes="selected_solution")
        else:
            indexing_tbl.addRow(row)
    # Add tool tip help to the table
    indexing_tbl.addHelpToColumn(0, help.indexing_solution_number,
                                 Canary.ALL_ROWS)
    indexing_tbl.addHelpToColumn(1, help.indexing_solution_penalty,
                                 Canary.ALL_ROWS)
    indexing_tbl.addHelpToColumn(2, help.indexing_solution_lattice,
                                 Canary.ALL_ROWS)
    indexing_tbl.addHelpToColumn(3, help.indexing_solution_cell_a,
                                 Canary.ALL_ROWS)
    indexing_tbl.addHelpToColumn(4, help.indexing_solution_cell_b,
                                 Canary.ALL_ROWS)
    indexing_tbl.addHelpToColumn(5, help.indexing_solution_cell_c,
                                 Canary.ALL_ROWS)
    indexing_tbl.addHelpToColumn(6, help.indexing_solution_cell_alpha,
                                 Canary.ALL_ROWS)
    indexing_tbl.addHelpToColumn(7, help.indexing_solution_cell_beta,
                                 Canary.ALL_ROWS)
    indexing_tbl.addHelpToColumn(8, help.indexing_solution_cell_gamma,
                                 Canary.ALL_ROWS)
    indexing_tbl.addHelpToRow(0, [None,
                                 None,
                                 None,
                                 help.indexing_solution_unrefined_cell])

    # Table of additional indexing data items with togglable rows
    indexing_data = indexing_summary.addContent(Jackdaw.ToggleTable(doc))
    indexing_data.addColumn(["Spot deviation (positional)",
                             "Spot deviation (angular)",
                             "Beam shift (X,Y)",
                             "Estimated mosaicity",
                             "Number of spots used",
                             "Number of spots total"])
    indexing_data.addColumn(['%.2f [mm]' %
                             indexing_results.spot_deviation_positional,
                             '%.2f [&deg;]' %
                             indexing_results.spot_deviation_angular,
                             '%.3f, %.3f [mm]' %
                             (indexing_results.beam_shift_x,
                              indexing_results.beam_shift_y),
                             '%.2f  [&deg;]' %
                             indexing_results.estimated_mosaicity,
                             indexing_results.number_of_spots_used,
                             indexing_results.number_of_spots_total])
    indexing_data.setHeader(['Additional indexing data'])
    # Make some rows togglable
    indexing_data.setToggleRow(4, 5)
    # Customise the controls
    indexing_data.addOpenLinkText("See all additional indexing data..",
                                  help_text=help.show_additional_indexing_data)
    indexing_data.addCloseLinkText("Collapse table..",
                                   help_text=help.hide_additional_indexing_data)
    # Add the help for the table and the row
    indexing_data.addTitle(help.additional_indexing_data)
    indexing_data.addHelpToRow(0, help.spot_deviation_positional,
                               Canary.ALL_COLUMNS)
    indexing_data.addHelpToRow(1, help.spot_deviation_angular,
                               Canary.ALL_COLUMNS)
    indexing_data.addHelpToRow(2, help.beam_shift_xy, Canary.ALL_COLUMNS)
    indexing_data.addHelpToRow(3, help.estimated_mosaicity, Canary.ALL_COLUMNS)
    indexing_data.addHelpToRow(4, help.number_of_spots_used, Canary.ALL_COLUMNS)
    indexing_data.addHelpToRow(4, help.number_of_spots_used, Canary.ALL_COLUMNS)
    indexing_data.addHelpToRow(5, help.number_of_spots_total, Canary.ALL_COLUMNS)

def addPredictionSummary(edna_run, section, edna_html_dir, help):
    # Write out a summary of the spot prediction results from the
    # supplied EDNA run into a subsection of the specified
    # document section
    prediction_summary = section.addSubsection("Spot predictions")
    prediction_summary.addHelp(help.prediction_summary)
    prediction_summary.addCSSClass("prediction_summary")
    content = ''
    for integration in edna_run.integration_ranges:
        content += "<div class='image_range'><span"
        content += " title='" + help.image_range_header + "'>"
        if integration.image_start == integration.image_end:
            content += "Image " + str(integration.image_start)
        else:
            content += "Images " + \
            str(integration.image_start) + \
            "-" + \
            str(integration.image_end)
        content += " (" + str(integration.rotation_axis) + " " + \
            '%.2f' % integration.rotation_axis_start + \
            "-" + \
            '%.2f' % integration.rotation_axis_end + \
            "&deg;)</span></div>"
        # Deal with the the images
        for image in integration.images:
            # Create some convenience variables
            image_basename = os.path.basename(image.jpeg)
            image_rootname = os.path.splitext(image_basename)[0]
            # Copy full sized image to the edna html directory
            image_jpeg = os.path.join(edna_html_dir, image_basename)
            CopyFile(image.jpeg, image_jpeg)
            image.jpeg = image_jpeg
            # Make a thumbnail version
            thumbnail = image_rootname + "_thumbnail.jpg"
            thumbnail = os.path.join(edna_html_dir, thumbnail)
            makeResizedImage(image.jpeg, thumbnail, 40, 40)
            # Create an "image box" for each image
            imgbox = "<div class='imgbox'>" + \
                "<div class='lhs'>" + Canary.MakeLink(
                image_jpeg, Canary.MakeImg(str(thumbnail),
                                          title=help.spot_prediction_image,
                                          width=40),
                new_window=True) + \
                "</div>" + \
                "<div class='rhs'><span class='image_name'" + \
                "title='" + help.image_name + "'>" + \
                image.name + "</span><br />" + "<span>" + \
                Canary.MakeLink(image_jpeg,
                                "See spot predictions",
                                help.spot_prediction_image,
                                new_window=True) + \
                "</span><br />" + \
                "<span>RMS spot deviation: " + \
                Canary.makeToolTip(
                ("%.3f" % integration.rms_spot_deviation) + " [mm]",
                help.rms_spot_deviation) + \
                "</span></div>" + \
                "</div>"
            content += imgbox + "\n"

        # Create a table with data inside a toggle folder for each range
        folder = Jackdaw.ToggleFolder(doc)
        folder.addCSSClass("prediction_data")
        folder.addOpenLinkText(Canary.MakeImg(
            os.path.join(edna_html_dir, "closed.png")) +
                               " See more data..",
                               help_text=help.show_integration_statistics)
        folder.addCloseLinkText(Canary.MakeImg(
            os.path.join(edna_html_dir, "open.png")) +
                                " Hide tables..",
                                help_text=help.hide_integration_statistics)
        folder.closedByDefault()
        # Table of integration statistics
        integration_tbl = folder.addContent(Canary.Table())
        integration_tbl.addColumn(["RMS spot deviation",
                                   "Average I/&sigma;",
                                   "Overall",
                                   "Highest resolution"],
                                  header="Statistics for this range")
        # I/sigma for fully recorded reflections
        column_fulls = ["%.3f [mm]" % integration.rms_spot_deviation,
                        "Fulls"]
        if integration.i_over_sigma_overall_fulls:
            column_fulls.append("%.1f" % integration.i_over_sigma_overall_fulls)
        else:
            column_fulls.append("n/a")
        if integration.i_over_sigma_highest_resoln_fulls:
            column_fulls.append("%.1f" %
                                integration.i_over_sigma_highest_resoln_fulls)
        else:
            column_fulls.append("n/a")
        # I/sigma for partially recorded reflections
        column_partials = [None,
                           "Partials"]
        if integration.i_over_sigma_overall_partials:
            column_partials.append("%.1f" %
                                   integration.i_over_sigma_overall_partials)
        else:
            column_partials.append("n/a")
        if integration.i_over_sigma_highest_resoln_partials:
            column_partials.append("%.1f" %
                             integration.i_over_sigma_highest_resoln_partials)
        else:
            column_partials.append("n/a")
        # Add the columns to the table
        integration_tbl.addColumn(column_fulls)
        integration_tbl.addColumn(column_partials)
        # Add extra styles, title etc
        integration_tbl.addClassToRow(1, "table_header table_header_alt")
        integration_tbl.addTitle(help.integration_statistics_table)
        # Add help
        integration_tbl.addHelpToRow(0, help.rms_spot_deviation,
                                     Canary.ALL_COLUMNS)
        integration_tbl.addHelpToRow(2, help.average_i_over_sigma_overall,
                                     Canary.ALL_COLUMNS)
        integration_tbl.addHelpToRow(3,
                                     help.average_i_over_sigma_highest_resoln,
                                     Canary.ALL_COLUMNS)
        # Table of reflection statistics
        reflections_tbl = folder.addContent(Canary.Table())
        reflections_tbl.addColumn(["Fully recorded",
                                   "Partials",
                                   "Overlapped",
                                   "With negative intensity",
                                   "Bad"],
                                  header="Number of reflections")
        reflections_tbl.addColumn([integration.fully_recorded_reflns,
                                   integration.partially_recorded_reflns,
                                   integration.overlapped_reflns,
                                   integration.negative_reflns,
                                   integration.bad_reflns])
        reflections_tbl.addTitle(help.reflections_statistics_table)
        reflections_tbl.addHelpToRow(0, help.reflections_fully_recorded,
                                     Canary.ALL_COLUMNS)
        reflections_tbl.addHelpToRow(1, help.reflections_partials,
                                     Canary.ALL_COLUMNS)
        reflections_tbl.addHelpToRow(2, help.reflections_overlapped,
                                     Canary.ALL_COLUMNS)
        reflections_tbl.addHelpToRow(3, help.reflections_negative,
                                     Canary.ALL_COLUMNS)
        reflections_tbl.addHelpToRow(4, help.reflections_bad,
                                     Canary.ALL_COLUMNS)
        content += folder.render()
    # Add all the info to the document
    prediction_summary.addContent(content)

def addStrategyFileList(edna_run, section, help):
    # Write out a list of the master log file and the input and output
    # XML files from edna_run
    filelist = section.addList()
    filelist.addClass("clear")
    if edna_run.log_file:
        filelist.addItem("Log file: " +
                         str(Canary.MakeLink(edna_run.log_file,
                                             os.path.basename(edna_run.
                                                              log_file),
                                             title=help.log_file)))
    else:
        filelist.addItem("Log file: [not supplied]")
    if edna_run.data_input_xml:
        filelist.addItem("XML input: " +
                         str(Canary.MakeLink(edna_run.data_input_xml,
                                             os.path.basename(edna_run.
                                                              data_input_xml),
                                             title=help.xml_input_file)))
    else:
        filelist.addItem("XML input: [not supplied]")
    if edna_run.data_output_xml:
        filelist.addItem("XML output: " +
                         str(Canary.MakeLink(edna_run.data_output_xml,
                                             os.path.basename(edna_run.
                                                             data_output_xml),
                                             title=help.xml_output_file)))
    else:
        filelist.addItem("XML output: [not supplied]")

def addFooter(doc):
    """Add the footer text to the HTML document

    The footer gives details of time, date and version numbers for
    each component."""
    doc.addPara("This file was generated for you from EDNA mxv1 output by EDNA2html %s on %s<br />Powered by Magpie %s and Canary %s<br />&copy; Diamond 2010" \
                % (version(),
                   time.asctime(),
                   Magpie.version(),
                   Canary.version()),
                css_class='credits')
    return

def CopyIcons(icon_list, source_icon_dir, target_icon_dir):
    """Copy the named icons in icon_list from the source to the target dir"""
    for icon in icon_list:
        CopyFile(os.path.join(source_icon_dir, icon),
                 os.path.join(target_icon_dir, icon))

def lookupErrorCode(error_code):
    """Return error message given an EDNA run error code"""
    if error_code == NO_ERROR:
        errmsg = None
    elif error_code == INCOMPLETE_EDNA_RUN_DATA:
        errmsg = "This may be because EDNA MXv1 failed to complete, " + \
                 " or because of an error in EDNA2html."
    elif error_code == RUN_BASENAME_DIR_NOT_FOUND:
        errmsg = "The supplied output directory for the EDNA run doesn't " + \
                 "exist"
    elif error_code == CHARACTERISATION_DIR_NOT_FOUND:
        errmsg = "EDNA2html was unable to locate the 'Characterisation' " + \
                 "subdirectory of the EDNA run output directory"
    elif error_code == UNDETERMINED_XML_PREFIX:
        errmsg = "EDNA2html was unable to determine the prefix for the " + \
                 "...dataInput.xml file in the 'Characterisation' " + \
                 "subdirectory of the EDNA run output directory"
    else:
        errmsg = "Unknown error (code = " + str(error_code) + ")"
    return errmsg

#######################################################################
# Main program
#######################################################################

if __name__ == "__main__":

    print "EDNA2html: started"
    print "Version " + str(version())
    print "Start time: " + str(time.asctime())

    # Collect the EDNA2HTMLDIR environment variable
    try:
        edna2htmldir = os.environ['EDNA2HTMLDIR']
    except KeyError:
        print "EDNA2HTMLDIR environment variable not set, stopped."
        sys.exit(1)
    print "EDNA2HTMLDIR = %s" % edna2htmldir

    # Set the usage string
    usage = "python EDNA2html.py [--title=<title text>] --input_xml=<XML_dataInput> --output_xml=<XML_dataOutput> --output_log=<log_file> [[--title=...] --input_xml=... ] [--basename=<name>]\npython EDNA2html.py [--title=<title text>] --run_basename=<run_basename> [[--title=...] --run_basename=...] [--basename=<name>] [--ranking] [--help_file=<tool_tip_file>] [--debug_help] [--portable]"

    # Initialise
    edna_runs = []
    edna_run = None
    invalid_input = False
    input_xml = None
    output_xml = None
    output_log = None
    basename = "edna"
    title = None
    tool_tip_file = "EDNA2html_tooltips_en_GB.txt"
    debug_help = False
    portable_output = False
    ranking_mode = False
    error_code = None

    # No command line arguments?
    if not len(sys.argv[1:]):
        print "Usage: " + str(usage)
        sys.exit(0)

    # Process the command line and collect file names
    for arg in sys.argv[1:]:
        if str(arg).startswith("--output_xml="):
            # Explicitly specify name of the dataOutput.xml file
            output_xml = arg[arg.index("=") + 1:]
            print "Output XML file: " + output_xml
        elif str(arg).startswith("--input_xml="):
            # Explicitly specify name of the dataInput.xml file
            input_xml = arg[arg.index("=") + 1:]
            print "Input XML file: " + input_xml
        elif str(arg).startswith("--output_log="):
            # Explicitly specify name of the log file
            output_log = arg[arg.index("=") + 1:]
            print "Output log file: " + output_log
        elif str(arg).startswith("--basename="):
            # Specify name to use for the output html file and
            # directory
            basename = arg[arg.index("=") + 1:]
            # Divide into leading directory and base file name
            basedirn = os.path.dirname(basename)
            basename = os.path.basename(basename)
            # Move to the base directory
            if basedirn:
                print "Moving to directory " + str(basedirn)
                os.chdir(basedirn)
            print "Basename: " + basename
        elif str(arg).startswith("--run_basename="):
            # Specify a basename for the run that will be used
            # to construct the names for input and output XML and
            # log files
            run_basename = arg[arg.index("=") + 1:]
            print "Run basename: " + run_basename
            print "Adding an EDNA run..."
            edna_run = EDNARunBuilder().setRunBasename(run_basename).EDNARun()
        elif str(arg).startswith("--title="):
            # Specify a title string to be associated with a run
            title = arg[arg.index("=") + 1:]
            print "Title: " + title + " (will be assigned to next run)"
        elif str(arg).startswith("--ranking"):
            # Turn on "ranking" mode
            print "Ranking mode: strategies will be assumed to be from " + \
                  "different crystals"
            ranking_mode = True
        elif str(arg).startswith("--help_file="):
            # Specify a title string to be associated with a run
            tool_tip_file = arg[arg.index("=") + 1:]
            print "Help file: " + tool_tip_file
        elif str(arg) == "--debug_help":
            # Display placeholder names rather than tool tips
            print "Debug help: display placeholders rather than tool tips"
            debug_help = True
        elif str(arg) == "--portable":
            # Make output portable by copying files to the output HTML dir
            print "Portable: generate \"portable\" output from EDNA2html"
            portable_output = True
        else:
            # Unrecognised option
            print "Unrecognised option: '" + str(arg) + "'"
            invalid_input = True
        if input_xml and output_xml and output_log:
            # We have a complete set of files
            # Create a new EDNARun object
            print "Adding an EDNA run..."
            edna_run = EDNARunBuilder().\
                       setInputXML(input_xml).\
                       setOutputXML(output_xml).\
                       setOutputLog(output_log). \
                       EDNARun()
            # Reset the variables for the files
            input_xml = None
            output_xml = None
            output_log = None
        # Deal with new EDNARun that may have been generated
        if edna_run:
            # Add the title, if supplied
            if title:
                edna_run.title = title
                title = None
            # Add to the list of runs
            edna_runs.append(edna_run)
            # Check for errors in processing the run data
            if not edna_run.isComplete():
                print "*** Warning: missing data or processing error"
            # Reset for the next pass
            edna_run = None
    if invalid_input:
        # Incorrect arguments
        print "Usage: " + str(usage)
        sys.exit(1)

    #####################################################
    # Make directory to store the additional files
    #####################################################

    # Basename used as name of html file and directory
    edna_html_file = basename + ".html"
    edna_html_dir = basename + "_html"
    if not os.path.isdir(edna_html_dir):
        print "Making directory '" + edna_html_dir + "'"
        os.mkdir(edna_html_dir)

    #####################################################
    # Check for major errors
    #####################################################

    # Were any runs actually supplied?
    if not len(edna_runs):
        print "*** ERROR ***"
        print "No EDNA runs supplied!"
        ErrorReporter(edna2htmldir,
                      edna_html_dir,
                      edna_runs).renderFile(edna_html_file)
        print "Stopped."
        sys.exit(1)

    # Locate the highest resolution run that completed
    completed_edna_run = None
    # Loop over all runs
    for edna_run in edna_runs:
        if edna_run.isComplete():
            if not completed_edna_run:
                # First completed run found so store it
                completed_edna_run = edna_run
            elif edna_run.strategy.strategy_resolution < \
                 completed_edna_run.strategy.strategy_resolution:
                # New highest resolution strategy
                completed_edna_run = edna_run
    # No completed runs - write error doc and exit
    if not completed_edna_run:
        print "*** ERROR ***"
        print "Wasn't able to process complete data from any supplied run"
        ErrorReporter(edna2htmldir,
                      edna_html_dir,
                      edna_runs).renderFile(edna_html_file)
        print "Stopped."
        sys.exit(1)

    #####################################################
    # Set up tool tips from external file
    #####################################################

    # Find the file
    if not os.path.isfile(tool_tip_file):
        tool_tip_file = os.path.join(edna2htmldir, tool_tip_file)

    # Initialise Help object for tool tip help
    # If show_names is True then the tool tips will be
    # replaced by the names of the placeholders that the
    # text is taken from (provided to help with updating
    # tool tips)
    help = Help(tool_tip_file, show_names=debug_help)

    #####################################################
    # Deal with "portable" output
    #####################################################

    if portable_output:
        # Loop over all EDNA runs and make copies of relevant
        # files in the HTML output directory (and updating stored
        # references to point to the copies)
        i = 0
        for edna_run in edna_runs:
            i += 1
            # Make a directory for this strategy
            strategy_dir = os.path.join(edna_html_dir, "strategy_" + str(i))
            if not os.path.isdir(strategy_dir):
                os.mkdir(strategy_dir)
            # Copy input XML and log
            edna_run.data_input_xml = makePortableFileCopy(\
                edna_run.data_input_xml, strategy_dir)
            edna_run.data_output_xml = makePortableFileCopy(\
                edna_run.data_output_xml, strategy_dir)
            edna_run.log_file = makePortableFileCopy(edna_run.log_file,
                                                     strategy_dir)
            # Copy log files to this directory
            for j in range(0, len(edna_run.labelit_distl_logs)):
                edna_run.labelit_distl_logs[j] = makePortableFileCopy(\
                    edna_run.labelit_distl_logs[j], strategy_dir)
            edna_run.mosflm_indexing_log = makePortableFileCopy(\
                edna_run.mosflm_indexing_log, strategy_dir)
            edna_run.labelit_indexing_log = makePortableFileCopy(\
                edna_run.labelit_indexing_log, strategy_dir)
            for j in range(0, len(edna_run.mosflm_integration_logs)):
                edna_run.mosflm_integration_logs[j] = makePortableFileCopy(\
                    edna_run.mosflm_integration_logs[j], strategy_dir)
            edna_run.raddose_log = makePortableFileCopy(edna_run.raddose_log,
                                                        strategy_dir)
            edna_run.best_log = makePortableFileCopy(edna_run.best_log,
                                                     strategy_dir)
            edna_run.best_plots = makePortableFileCopy(edna_run.best_plots,
                                                       strategy_dir)

    #####################################################
    # Make a HTML document
    #####################################################

    doc = Canary.Document("Strategy for image template " +
                          Canary.makeToolTip(completed_edna_run.image_template,
                                             help.image_template))
    doc.addStyle(os.path.join(edna2htmldir, "EDNA2html.css"), Canary.INLINE)
    doc.addScript(os.path.join(edna2htmldir, "EDNA2html.js"), Canary.INLINE)
    doc.addScript(os.path.join(edna2htmldir, "TabbedFolder.js"), Canary.INLINE)
    doc.addScript(os.path.join(edna2htmldir, "ToggleTable.js"), Canary.INLINE)
    doc.addScript(os.path.join(edna2htmldir, "EDNA2html_sortable_table.js"),
                  Canary.INLINE)

    # Make document skeleton
    #
    # Untitled section for indexing and integration summaries
    indexing_and_integration = doc.addSection()
    #
    # Section with full summaries of each strategy
    strategies_summary = doc.addSection("Strategies to resolution %.2f &Aring;"
                                        % completed_edna_run.
                                        strategy.strategy_resolution)
    strategies_summary.addHelp(help.strategies_summary)
    #
    # Summary table comparing predicted stats etc from the strategies
    summary_table = strategies_summary.addTable()
    summary_table.addClass("summary")
    #
    # Append a comment to the table if at least one run has more
    # than one sweep, to explain values marked with "*" later on
    multi_sweep = False
    for edna_run in edna_runs:
        if len(edna_run.strategy.sweeps) > 1:
            multi_sweep = True
            break
    if multi_sweep:
        strategies_summary.addPara(Canary.MakeImg(os.path.join(edna_html_dir, "info.png")) + " Note that '*' indicates that this is the value from the highest resolution sweep in the strategy",
                                   css_class="info")

    # Indexing and spot prediction results section
    if not ranking_mode:
        # In this mode assume that all the runs used the same images
        # Write a single summary using data from the first run
        addIndexingSummary(completed_edna_run,
                           indexing_and_integration, edna_html_dir,
                           help)
        addPredictionSummary(completed_edna_run,
                             indexing_and_integration, edna_html_dir,
                             help)

    # Each strategy summary in its own tab
    summary_column = []
    strategy_tab = strategies_summary.addContent(Jackdaw.TabbedFolder(doc))
    i = 0
    tab_list = []
    for edna_run in edna_runs:
        i += 1
        tab = strategy_tab.addTab("Strategy " + str(i))
        if edna_run.title:
            tab.addHelp(edna_run.title)
        else:
            tab.addHelp("Strategy from run " + str(i))
        strategy = tab.addContent(Canary.Section(None, 1, doc))
        try:
            addStrategySummary(strategy, edna_run, ranking_mode, edna_html_dir,
                               help)
        except Exception:
            print "*** Failed to add strategy summary ***"
        tab_list.append(tab.id())
        strategy.addCSSClass("strategy_summary")
    # Build the summary table of strategies
    #
    # Build script to populate data structures for the sortable
    # summary table
    populateStrategySummaryTable(doc,
                                 summary_table,
                                 edna_html_dir,
                                 ranking_mode,
                                 edna_runs,
                                 strategy_tab.id(),
                                 tab_list)
    # Include descriptions in the table?
    show_descriptions = Canary.JS_FALSE
    for edna_run in edna_runs:
        if edna_run.title:
            show_descriptions = Canary.JS_TRUE
            break
    # Include ranking resolution in the table?
    if ranking_mode:
        show_ranking_resolution = Canary.JS_TRUE
    else:
        show_ranking_resolution = Canary.JS_FALSE
    # Set up the sortable table
    onload_script = "initTable('strategyData'," + \
                    show_descriptions + "," + \
                    show_ranking_resolution + ");"
    doc.addOnload(onload_script)

    # References section
    references = doc.addSection("References")
    references_list = references.addList()
    references_list.addItem("<b>EDNA</b>: " + Canary.MakeLink(\
        "http://journals.iucr.org/s/issues/2009/06/00/wa5014/index.html",
        "M.-F. Incardona, G. P. Bourenkov, K. Levik, R. A. Pieritz, A. N. Popov and O. Svensson, J. Synchrotron Rad. (2009), 16, 872-879"))
    references_list.addItem("<b>MOSFLM</b>: Leslie, A.G.W., (1992), Joint CCP4 + ESF-EAMCB Newsletter on Protein Crystallography, No. 26.")
    references_list.addItem("<b>Raddose</b>: Paithankar, K.S., Owen, R.L and Garman, E.F, J. Syn. Rad. (2009), 16, 152-162")
    references_list.addItem("<b>Raddose</b>: Murray, J.W., Garman, E.F., and Ravelli, R.B.G, J. Appl. Cryst. (2004) 37, 513-522")
    references_list.addItem("<b>BEST</b>: " + Canary.MakeLink(\
        "http://journals.iucr.org/d/issues/2010/04/00/ba5145/index.html",
        "Bourenkov, Gleb P. &amp; Popov, Alexander N. (2010) Acta Crystallographica Section D 66, 409--419"))

    # Acknowledgements/credits
    addFooter(doc)

    # Create the final document
    print "Generating ouput HTML file: " + str(edna_html_file)
    doc.renderFile(edna_html_file)
    # Copy icons
    CopyIcons(['open.png', 'closed.png', 'info.png', 'warning.png'],
              os.path.join(edna2htmldir, "icons"),
              edna_html_dir)
    # Finished
    print "Done"
