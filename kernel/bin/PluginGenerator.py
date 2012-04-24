#!/usr/bin/env python
#-*- coding: UTF8 -*-
#
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: PluginGenerator.py 1092 2010-02-02 kieffer $"
#
#    Copyright (C) 2009-2010 DLS
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
__authors__ = ["Mark Basham", "Olof Svensson", "Jérôme Kieffer"]
__license__ = "GPLv3"
__date__ = "2011-06-17"
__copyright__ = "DLS"
"""

 This creates an EDNA plugin template for use with the EDNA framework
 It creates the whole directory framework needed, the core plugin code
 and the core tests, which are all run as part of the generator

 This creates the following directory structure and files::
  ProjectName
   |--plugins
   |    |--EDPluginName-v1.0
   |    |  |--datamodel
   |    |  |  |--generateXSDataTemplate.sh
   |    |  |  |--XSDataExecTest3.xsd
   |    |  |--plugins
   |    |  |  |--EDPluginNamev10.py
   |    |  |  |--XSDataPluginName.py
   |    |  |--tests
   |    |  |  |--data
   |    |  |  |  |--XSConfiguration_PluginName.xml
   |    |  |  |  |--XSDataInputPluginName_reference.xml
   |    |  |  |  |--XSDataResultPluginName_reference.xml
   |    |  |  |--testsuite
   |    |  |  |  |--EDTestCasePluginNameExecuteTest.py
   |    |  |  |  |--EDTestCasePluginNameUnitTest.py
   |    |  |  |  |--EDTestSuitePluginNameTest.py
 
"""
import optparse
import os
import sys
import shutil
import subprocess
import xml.dom.minidom

class PluginGenerator(object):
    """
    Class description
    """
    def __init__(self):
        # the name of the plugin from which this inherits
        self._base_name = None
        # the name of the project where this plugin will be placed
        self._project_name = None
        # name of the default site for the plugin
        self._site_name = None

        # Some basic information for the file headers and pathnames etc.
        self._version = None
        self._copyright = None
        self._author = None

        # directorys where the templates and final plugin will be stored
        self._template_dir = None
        self._root_directory = None

        # All the information required for the xsd manipulation
        self._xsd_filename = None
        self._xsd_name = None
        self._xsd_data_input_name = None
        self._xsd_data_result_name = None
        self._xsd_input = None
        self._xsd_result = None
        self._xsd_general = None

        # All the plugin information
        self._plugin_name = None
        self._plugin_base_directory = None
        self._plugin_filename = None
        self._plugin_test_filename = None

        # If the plugin is a control plugin, this is the name of the plugin which will be controlled
        self._slave_plugin_name = None

        # List of all the valid basenames
        # Adding to this requires the additional templates to be in place
        self._valid_base_names = ["Exec", "Control"]

        # Add the list of invalid charaters which should not be in the plugin name etc.
        self._invalid_plugin_characters = [' ']

        # Set up all the caches
        self._cache_dirname = None
        self._cache_xsd_base_name = None
        self._cache_replacements = None

        return

    def set_root_directory(self, root_directory):
        """
        Sets the root directory as well as checking that it exists
        """

        if not os.path.exists(root_directory):
            raise RuntimeError("The directory '%s' is not present" % root_directory)
        self._root_directory = root_directory
        return

    def get_xsd_base_name(self):
        if not self._cache_xsd_base_name :
            assert(self._plugin_name)
            if (self._xsd_general == None):
                self._cache_xsd_base_name = "XSData%s%s" % (self._base_name, self._plugin_name)

            else:
                (filepath, filename) = os.path.split(self._xsd_filename)
                self._cache_xsd_base_name = filename.split('.')[0]
        return self._cache_xsd_base_name

    def set_base_name(self, base_name):
        """
        Sets the base name, and makes sure it is valid
        """
        for valid_name in self._valid_base_names:
            if(base_name.upper() == valid_name.upper()):
                self._base_name = valid_name
                return

        # if the base name is not on the list then return an error
        raise RuntimeError("Base plugin needs to be either a control or exec plugin you have specified a %s plugin" % base_name)


    def set_plugin_name(self, plugin_name):
        """
        Set the plugin name throwing an error if there are any invalid characters
        """
        self._plugin_name = plugin_name.strip()
        for token in self._invalid_plugin_characters:
            if plugin_name.find(token) > 0:
                raise RuntimeError("The plugin name contains the invalid character '%s' please remove this to continue" % token)

        self._plugin_name = plugin_name
        return

    def set_version(self, version):
        # Check that the version contains a "." surrounded by two integers
        if version.find(".") == -1:
            raise RuntimeError("""The plugin version must contain a  ".", e.g. 1.0, 2.2 etc. Non valid version: %s""" % version)
        (strMajorNumber, strMinorNumber) = version.split(".")
        try:
            iMajorNumber = int(strMajorNumber)
        except Exception:
            raise RuntimeError("""The plugin version major number not an integer: %s""" % strMajorNumber)
        try:
            iMinorNumber = int(strMinorNumber)
        except Exception:
            raise RuntimeError("""The plugin version minor number not an integer: %s""" % strMinorNumber)
        self._version = version
        return

    def set_copyright(self, copyright):
        self._copyright = copyright
        return

    def set_author(self, author):
        self._author = author
        return

    def set_template_dir(self, template_dir):
        if not os.path.exists(template_dir):
            raise RuntimeError("The template directory '%s' does not exist" % template_dir)
        self._template_dir = template_dir
        return

    def set_xsd_filename(self, xsd_filename):
        """
        Sets the filename and also works out the name part, i.e. XSDataFooBar.xsd
        This now also pulls out the information and sets 2 other parameters :
        _xsd_data_input_name
        _xsd_data_result_name
        """
        if xsd_filename is not None:
            if not os.path.exists(xsd_filename):
                raise RuntimeError("The xsd filename '%s' does not exist" % xsd_filename)
            self._xsd_filename = xsd_filename
            self._xsd_name = os.path.split(xsd_filename)[-1]
            self.check_xsd_input_and_result_with_xsd(xsd_filename)
        return

    def set_xsd_input(self, xsd_input):
        self._xsd_input = xsd_input
        return

    def set_xsd_result(self, xsd_result):
        self._xsd_result = xsd_result
        return

    def set_xsd_general(self, xsd_general):
        self._xsd_general = xsd_general
        return

    def set_project_name(self, project_name):
        self._project_name = project_name
        return

    def set_generator_filename(self, generator_filename):
        self._generator_filename = generator_filename
        return

    def get_dir_name(self):
        if not self._cache_dirname :
            assert(self._plugin_name)
            assert(self._version)
            self._cache_dirname = "EDPlugin%s%s-v%s" % (self._base_name, self._plugin_name, self._version)
        return self._cache_dirname

    def get_xsd_name(self):
        return self.get_xsd_base_name() + ".xsd"

    def set_plugin_filename(self, plugin_filename):
        self._plugin_filename = plugin_filename
        return

    def set_plugin_test_filename(self, plugin_test_filename):
        self._plugin_test_filename = plugin_test_filename
        return

    def set_slave_plugin_name(self, slave_plugin_name):
        self._slave_plugin_name = slave_plugin_name
        return

    def set_site_name(self, site_name):
        self._site_name = site_name
        return

    def set_plugin_directory(self, plugin_directory):
        self._plugin_base_directory = plugin_directory

    def create_file_structure(self):
        """
        This creates the file structure and populates some other parameters which are needed
        """
        assert(self._root_directory)
        if not self._plugin_base_directory:
            self._plugin_base_directory = os.path.join(self._root_directory, self.get_dir_name())
#        if(os.path.exists(self._plugin_base_directory)):
#            raise Exception("The directory %s already exists, please delete this to continue" % (self._plugin_base_directory))

        # now make the directories
        if not self._xsd_general:
            if self._xsd_name:
                os.makedirs(os.path.join(self._plugin_base_directory, "datamodel"))
        plugin_dir = os.path.join(self._plugin_base_directory, "plugins")
        for lmydir in [["plugins"], ["tests", "data"], ["tests", "testsuite"]]:
            full_path = os.path.join(*([self._plugin_base_directory] + lmydir))
            if not os.path.isdir(full_path):
                os.makedirs(full_path)
#        os.makedirs(os.path.join(self._plugin_base_directory, "plugins"))
#        os.makedirs(os.path.join(self._plugin_base_directory, "tests", "data"))
#        os.makedirs(os.path.join(self._plugin_base_directory, "tests", "testsuite"))
#        return

    def get_replacement_dictionary(self):
        if not self._cache_replacements :
            assert(self._copyright)
            assert(self._author)
            assert(self._project_name)
            assert(self._base_name)
            self._cache_replacements = {}
            self._cache_replacements['<copyright>'] = self._copyright
            self._cache_replacements['<author>'] = self._author
            self._cache_replacements['<xsDataBaseDir>'] = self.get_dir_name()
            self._cache_replacements['<xsDataBaseName>'] = self.get_xsd_base_name()
            self._cache_replacements['<xsDataName>'] = self.get_xsd_name()
            self._cache_replacements['<projectName>'] = self._project_name
            self._cache_replacements['<fileName>'] = "EDPlugin%s%s%sv%s" % (self._base_name, self._plugin_name, self._version.replace(".", "_"), '.py')
            self._cache_replacements['<xsDataInputName>'] = self._xsd_data_input_name
            self._cache_replacements['<xsDataResultName>'] = self._xsd_data_result_name

            self._cache_replacements['<pluginName>'] = "%sv%s" % (self._plugin_name, self._version.replace(".", "_"))
            self._cache_replacements['<controledPluginName>'] = self._slave_plugin_name
            self._cache_replacements['<basePluginName>'] = self._plugin_name
            self._cache_replacements['<pluginDir>'] = self.get_dir_name()
            self._cache_replacements['<baseName>'] = self._base_name
            self._cache_replacements['[pluginName]'] = "EDPlugin%s%sv%s" % (self._base_name, self._plugin_name, self._version.replace(".", "_"))
        return self._cache_replacements

    def create_template_replaced_file(self, templatefilename, outputfilename, replacement_dict):
        infile = open(templatefilename, "r")
        outfile = open(outputfilename, "w")
        for line in infile.readlines():
            for key in replacement_dict.keys():
                if replacement_dict[key] is not None:
                    line = line.replace(key, replacement_dict[key])
                else:
                    line = line.replace(key, "None")
            outfile.write(line)

    def create_xsd_converter_script(self):
        print 'running create_xsd_converter_script()...'
        assert(self._plugin_base_directory)
        assert(self._xsd_filename)
        assert(self._xsd_name)
        assert(self._template_dir)
        replacements = self.get_replacement_dictionary()

        template_file = os.path.join(self._template_dir, "datamodel", "generateXSDataTemplate.sh")
        new_file = os.path.join(self._plugin_base_directory, "datamodel", "generate%s.sh" % os.path.splitext(self._xsd_name)[0])
        self.set_generator_filename(new_file)
        self.create_template_replaced_file(template_file, new_file, replacements)


    def check_xsd_input_and_result_with_xsd(self, xsd_file_name):
        tree = xml.dom.minidom.parse(xsd_file_name)
        input_and_result = tree.getElementsByTagName("xs:complexType")
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print self._xsd_input

        bFoundInput = False
        bFoundResult = False
        for part in input_and_result:
            if not part.getElementsByTagName("xs:extension") == []:
                xsd_data_name = part.getAttribute("name")
                if xsd_data_name == self._xsd_input:
                    bFoundInput = True
                    self._xsd_data_input_name = self._xsd_input
                if xsd_data_name == self._xsd_result:
                    bFoundResult = True
                    self._xsd_data_result_name = self._xsd_result
        if not bFoundInput:
            raise RuntimeError("ERROR! Couldn't find definition of %s in %s." % (self._xsd_input, xsd_file_name))
        if not bFoundResult:
            raise RuntimeError("ERROR! Couldn't find definition of %s in %s." % (self._xsd_result, xsd_file_name))


#    def populate_xsd_input_and_result_from_xsd(self, xsd_file_name):
#
#        self._xsd_data_input_order = self._xsd_input
#        self._xsd_data_result_order = self._xsd_result
#
#
#        tree = xml.dom.minidom.parse(xsd_file_name)
#
#        try:
#            input_only = tree.getElementsByTagName("xs:complexType")[int(self._xsd_data_input_order)].getElementsByTagName("xs:extension")
#            result_only = tree.getElementsByTagName("xs:complexType")[int(self._xsd_data_result_order)].getElementsByTagName("xs:extension")
#        except Exception:
#            print '\n-i and -r options are mandatory. Please check valid inputs/results values in the following:'
#            self.display_xsd_file(xsd_file_name)
#            os.sys.exit(0)
#
#        if input_only[0].getAttribute("base") == "XSDataInput":
#            self._xsd_data_input_name = tree.getElementsByTagName("xs:complexType")[int(self._xsd_data_input_order)].getAttribute("name")
#            print ''
#            print 'input: ' + self._xsd_data_input_name
#        else:
#            print 'the element you selected is not of type XSDataInput or does not exist. Please check the -i parameter.'
#            self.display_xsd_file(xsd_file_name)
#            os.sys.exit(0)
#
#        if result_only[0].getAttribute("base") == "XSDataResult":
#            self._xsd_data_result_name = tree.getElementsByTagName("xs:complexType")[int(self._xsd_data_result_order)].getAttribute("name")
#            print 'result: ' + self._xsd_data_result_name
#            print ''
#        else:
#            print 'the element you selected is not of type XSDataResult or does not exist. Please check the -r parameter.'
#            self.display_xsd_file(xsd_file_name)
#            os.sys.exit(0)

    def display_xsd_file(self, xsd_file_name):
        tree = xml.dom.minidom.parse(xsd_file_name)
        input_and_result = tree.getElementsByTagName("xs:complexType")

        order = 0
        for part in input_and_result:
            if not part.getElementsByTagName("xs:extension") == []:
                if part.getElementsByTagName("xs:extension")[0].getAttribute("base") == "XSDataInput":
                    self._xsd_data_input_name = part.getAttribute("name")
                    print 'XSDataInput ' + str(order) + ' : ' + str(self._xsd_data_input_name)
            order = order + 1

        order = 0
        for part in input_and_result:
            if not part.getElementsByTagName("xs:extension") == []:
                if part.getElementsByTagName("xs:extension")[0].getAttribute("base") == "XSDataResult":
                    self._xsd_data_input_name = part.getAttribute("name")
                    print 'XSDataResult ' + str(order) + ' : ' + str(self._xsd_data_input_name)
            order = order + 1

    def copy_xsd_to_local(self):
        assert(self._plugin_base_directory)
        assert(self._xsd_filename)
        new_path = os.path.join(self._plugin_base_directory, "datamodel", self.get_xsd_name())
        shutil.copy(self._xsd_filename, new_path)
        return


    def run_the_xsd_script(self):
        assert(self._generator_filename)
        subprocess.call(["bash", self._generator_filename])
        return

    def check_file_does_not_exist(self, new_file):
        if os.path.exists(new_file):
            raise RuntimeError("The file %s already exist, I stop NOW !!!" % new_file)
            sys.exit(1)


    def copy_and_populate_plugin(self):
        assert(self._base_name)
        replacements = self.get_replacement_dictionary()
        template_file = os.path.join(self._template_dir, "plugins")
        template_file = os.path.join(template_file, "EDPlugin%s.py.template" % self._base_name)
        new_file = os.path.join(self._plugin_base_directory, "plugins")
        new_file = os.path.join(new_file, "EDPlugin%s%sv%s.py" % (self._base_name, self._plugin_name, self._version.replace(".", "_")))
        self.check_file_does_not_exist(new_file)
        self.set_plugin_filename(new_file)
        self.create_template_replaced_file(template_file, new_file, replacements)
        return

    def copy_and_populate_plugin_tests(self):
        assert(self._base_name)
        assert(self._plugin_name)
        replacements = self.get_replacement_dictionary()
        template_dir = os.path.join(self._template_dir, "tests", "testsuite")
        plugin_dir = os.path.join(self._plugin_base_directory, "tests", "testsuite")
        template_file = os.path.join(template_dir, "EDTestCasePluginExecute%s.py.template" % self._base_name)
        new_file = os.path.join(plugin_dir, "EDTestCasePluginExecute%s%sv%s.py" % (self._base_name, self._plugin_name, self._version.replace(".", "_")))
        self.check_file_does_not_exist(new_file)
        self.create_template_replaced_file(template_file, new_file, replacements)
        template_file = os.path.join(template_dir, "EDTestCasePluginUnit%s.py.template" % self._base_name)
        new_file = os.path.join(plugin_dir, "EDTestCasePluginUnit%s%sv%s.py" % (self._base_name, self._plugin_name, self._version.replace(".", "_")))
        self.check_file_does_not_exist(new_file)
        self.create_template_replaced_file(template_file, new_file, replacements)
        template_file = os.path.join(template_dir, "EDTestSuitePlugin.py.template")
        new_file = os.path.join(plugin_dir, "EDTestSuitePlugin%s%sv%s.py" % (self._base_name, self._plugin_name, self._version.replace(".", "_")))
        self.check_file_does_not_exist(new_file)
        self.create_template_replaced_file(template_file, new_file, replacements)
        return

    def copy_test_data_information(self):
        replacements = self.get_replacement_dictionary()
        template_file_base = os.path.join(self._template_dir, "tests", "data")
        template_file = os.path.join(template_file_base, "XSConfigTemplate.xml")
        new_file_base = os.path.join(self._plugin_base_directory, "tests", "data")
        new_file = os.path.join(new_file_base, "XSConfiguration_%s.xml" % (self._plugin_name))
        self.check_file_does_not_exist(new_file)
        self.create_template_replaced_file(template_file, new_file, replacements)
        template_file = os.path.join(template_file_base, "XSDataInputTemplate_reference.xml")
        new_file = os.path.join(new_file_base, "XSDataInput%s_reference.xml" % (self._plugin_name))
        self.check_file_does_not_exist(new_file)
        self.create_template_replaced_file(template_file, new_file, replacements)
        template_file = os.path.join(template_file_base, "XSDataResultTemplate_reference.xml")
        new_file = os.path.join(new_file_base, "XSDataResult%s_reference.xml" % (self._plugin_name))
        self.check_file_does_not_exist(new_file)
        self.create_template_replaced_file(template_file, new_file, replacements)
        return

    def run_execute_test(self):
        assert(self._base_name)
        assert(self._plugin_name)
        assert(self._version)
        test_runner_location = os.path.join(os.environ['EDNA_HOME'], "kernel", "bin", "edna-test-launcher")
        plugin_to_be_tested = "EDTestSuitePlugin%s%sv%s" % (self._base_name, self._plugin_name, self._version.replace(".", "_"))
        print "Running the tests"
        subprocess.call([test_runner_location, "--test", plugin_to_be_tested])
        return

    def register_with_site_config(self):
        assert(self._site_name)
        assert(self._root_directory)
        assert(self._plugin_base_directory)
        assert(self._plugin_name)
        #check to see if the file exists
        config_path = os.path.join(self._root_directory, "..", "conf")
        config_filename = os.path.join(config_path, "XSConfiguration_%s.xml" % self._site_name)
        config_testfile = os.path.join(self._plugin_base_directory, "tests", "data", "XSConfiguration_%s.xml" % (self._plugin_name))

        if os.path.exists(config_filename):

            main_tree = xml.dom.minidom.parse(config_filename)
            add_tree = xml.dom.minidom.parse(config_testfile)

            add_node = add_tree.getElementsByTagName("XSPluginItem")[0]
            main_tree.getElementsByTagName("XSPluginList")[0].appendChild(add_node)

            main_tree.writexml(open(config_filename, "w"))
            return

        else :
            if not os.path.exists(config_path):
                os.makedirs(config_path)

            shutil.copy(config_testfile, config_filename)
            return

    def create_plugin(self):
        """
        Runs all the components of the plugin generator
        """
        self.create_file_structure()


        if (self._xsd_general == None) and (self._xsd_filename):
            self.create_xsd_converter_script()
            self.copy_xsd_to_local()
            self.run_the_xsd_script()

        self.copy_and_populate_plugin()
        self.copy_and_populate_plugin_tests()
        self.copy_test_data_information()
        if self._xsd_filename:
            self.run_execute_test()
        self.register_with_site_config()
        return

class HelpFormatter(optparse.IndentedHelpFormatter):
    """ 
    Overrides the standard help formatter to make the output format suit our requirements.
    Nicked from Mathew Webber
    """
    def __init__(self, width=80):
        """
        Make the output a bit wider than the default of 80.
        """
        optparse.IndentedHelpFormatter.__init__(self, width=width)
        return

    def format_description(self, description):
        """
        The standard format_description() removes \n with the description, this version retains them.
        """
        return description + "\n"

def main():

    parser = optparse.OptionParser(formatter=HelpFormatter(), description=
        "This program is designed to allow the auto generation of an EDNA plugin."
        "\nTo use this EDNA_HOME, and EDNA_CONFIG need to be set, where EDNA_CONFIG should be something "
        "\nlike 'DLS' or 'ESRF' and EDNA_HOME should be set to the direcoty which contains the EDNA "
        "\nkernel, it must also contain the base directory structure of the project you want to use."
        "\nThe default project is EDNA_HOME/templatev1/plugin"
        "\n\nUsage :"
        "\nPluginGenerator.py"
        "\n\tGenerates an example plugin in the default project"
        "\nPluginGenerator.py -n MyPlugin -b Control -v 2.1 -i XSDataInputMTZDUMPUnitCellSpaceGroup -r XSDataResultMTZDUMPUnitCellSpaceGroup -a 'Mark Basham' -c DLS"
        "\n\tGenerates a plugin called MyPlugin which is version 2.1 of a control plugin with the specified input and result"
        "\n\tauthored by Mark Basham and with DLS as the copyright holder"
        "\n\t"
        )

    parser.add_option("-n", "--plugin-name", dest="plugin_name", help="Specifies the name of the plugin you wish to create", default="Template")
    parser.add_option("-b", "--base-plugin", dest="base_name", help="Specifies which plugin you want your new plugin to inherit from", default="Exec")
    parser.add_option("-p", "--project-name", dest="project_name", help="Specifies the name of the project inside edna where this plugin will be i.e. the directory after EDNA_HOME, such as mxv1 or darcv1", default="templatev1")
    parser.add_option("-x", "--xsd-location", dest="xsd_location", help="Specifies the location of the XSD, which is to be used for the plugin. This option is mandatory if the -g tag is not specified (using the local xsd).")

    parser.add_option("-i", "--xsd-input", dest="xsd_input", help="Specifies the input XSData class, e.g. XSDataInputStrategy")
    parser.add_option("-r", "--xsd-result", dest="xsd_result", help="Specifies the result XSData class, e.g. XSDataResultStrategy")

    # -g option does not need a value
    parser.add_option("-g", "--xsd-general", dest="xsd_general", action="store_true", help="Specifies that the plugin generator will be using the general datamodel")

    parser.add_option("-e", "--emulate-plugin", dest="plugin_to_emulate", help="Specifies the location of the plugin which this plugin will replace, this is not curently implemented")
    parser.add_option("-v", "--plugin-version", dest="plugin_version", help="Specifies version of the plugin, e.g. 1.0/1.2/2.3/3.10 etc", default="1.0")
    parser.add_option("-a", "--author", dest="plugin_author", help="The principle author of the plugin i.e. you", default="Default Author")
    parser.add_option("-c", "--copyright", dest="plugin_copyright", help="Specifies the copyright string which will be present in the plugin", default="2008-2009 - EDNA Default Copyright")
    parser.add_option("-s", "--slave-plugin-name", dest="slave_plugin_name", help="If the plugin is a control plugin, this specifies which plugin will be controled", default="EDPluginExecTemplate")
    parser.add_option("--site-name", dest="site_name", help="the name of the site, to decide which configuration file to add the plugin to, i.e. DLS/ESRF etc, default is DLS", default="DLS")
    parser.add_option("--no-xsd", dest="generateDB", action="store_false", help="use this option to prevent the generation of the databindings ", default=True)
    parser.add_option("--force_location", dest="plugin_root", help="use this option to enforce the location a plugin in EDNA's tree", default=None)

    (options, args) = parser.parse_args()

    # xsd is a mandatory option if -g tag is not present
    if options.xsd_location is None and options.xsd_general is not None:
        print "A mandatory option -x is missing as -g is present\n"
        parser.print_help()
        os.sys.exit(0)

    pg = PluginGenerator()

    if not 'EDNA_HOME' in os.environ:
        pyStrProgramPath = os.path.abspath(sys.argv[0])
        pyStrBinPath = os.path.split(pyStrProgramPath)[0]
        pyStrKernelPath = os.path.split(pyStrBinPath)[0]
        pyStrEdnaHomePath = os.path.split(pyStrKernelPath)[0]
        os.environ["EDNA_HOME"] = pyStrEdnaHomePath
        print ('EDNA_HOME not set, trying to guess it .... %s' % pyStrEdnaHomePath)
    else:
        pyStrEdnaHomePath = os.environ['EDNA_HOME']

    if options.plugin_root:
        root_dir = os.path.join(pyStrEdnaHomePath, options.plugin_root)
        plugin_dir = os.path.join(pyStrEdnaHomePath, options.plugin_root)
    else:
        root_dir = os.path.join(pyStrEdnaHomePath, options.project_name, "plugins")

    if not os.path.exists(root_dir):
        # now make the directory
        os.makedirs(root_dir)

    template_dir = os.path.join(os.environ['EDNA_HOME'], "template")

    xsd_loc = options.xsd_location
    if xsd_loc == None and options.generateDB:
        xsd_loc = os.path.join(template_dir, "datamodel")
        xsd_loc = os.path.join(xsd_loc, "XSDataTemplate.xsd")

    pg.set_root_directory(root_dir)
    pg.set_base_name(options.base_name)
    pg.set_plugin_name(options.plugin_name)
    pg.set_version(options.plugin_version)
    pg.set_author(options.plugin_author)
    pg.set_copyright(options.plugin_copyright)
    pg.set_plugin_directory(plugin_dir)
    if options.generateDB:
        pg.set_xsd_input(options.xsd_input)
        pg.set_xsd_result(options.xsd_result)
        pg.set_xsd_general(options.xsd_general)
        pg.set_xsd_filename(xsd_loc)
    pg.set_template_dir(template_dir)
    pg.set_project_name(options.project_name)
    pg.set_slave_plugin_name(options.slave_plugin_name)
    pg.set_site_name(options.site_name)

    pg.create_plugin()

if __name__ == "__main__":
    main()
