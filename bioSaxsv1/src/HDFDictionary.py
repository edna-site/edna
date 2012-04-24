"""
==============================================
  NAME       : HDF Dictionary (HDFDictionary.py)
  
  DESCRIPTION:
    
  VERSION    : 1

  REVISION   : 0

  RELEASE    : 2009/MAR/04

  PLATFORM   : None

  EMAIL      : ricardo.fernandes@esrf.fr
  
  HISTORY    :
==============================================
"""


# =============================================
#  IMPORT MODULES
# =============================================
try:
    import sys
    import os
    from xml.sax import make_parser
    from xml.sax.handler import ContentHandler
except Exception:
    print __name__ + ".py: error when importing module!"



# =============================================
#  CLASS DEFINITION
# =============================================
class HDFDictionary():
    """
    Class that allows the extraction/conversion of keywords and their values from a given python list. The set of rules that
    specifies how to do such operations is represented in a XML file. It can contain one or more dictionaries (each of them
    is delimited by the "dictionary" tag). A typical XML file containing dictionaries would be similar to this (in this example,
    SPEC and EDF):
    
        <hdf>
        
            <dictionary name = "SPEC">
                <keyword name = "Sample c">concentration</keyword>
                <keyword name = "Dim_1">dimension_1</keyword>
                <keyword name = "SampleDistance">sample_distance</keyword>                
                        .
                        .
                        .                                                
                <keyword name = "-i1pix" separator = " " finish = " -" split = " ">beamline_pixel_size_X, beamline_pixel_size_Y</keyword>
            </dictionary>
            
            <dictionary name = "EDF">    
                <keyword name = "EDF_DataBlockID">data_block_ID</keyword>    
                <keyword name = "Center_1">detector_beam_center_X</keyword>
                <keyword name = "Center_2">detector_beam_center_Y</keyword>
                        .
                        .
                        .                                                
                <keyword name = "SaxsDataVersion">saxs_data_version</keyword>
            </dictionary>
            
        </hdf>

    
    The "keyword" tag is the one where the rules of extracting/converting a certain keyword is specified. The syntax is the following:
    
        <keyword name = "a" separator = "b" finish = "c" split = "d" slice = "e" format = "f">g</keyword>
    
    name (mandatory)    : the name of the keyword to look for in a certain line.
    separator (optional): the characters that separates the keyword from its value. If not specified, then the default separator is "=".
    finish (optional)   : the characters that delimits the value. If not specified, then it is assumed to go until the end of the line.
    split (optional)    : the characters that splits the value into sub-values. If not specified, then no split will be done.
    slice (optional)    : the slice of the value (basically, it returns a substring of the value using the same slicing syntax as Python). If not
                          specified, then no slice will be done.
    format (optional)   : the format of the value (basically, it formats the value using the same syntax as Python). If not specified, then no
                          format will be done. For more details, please see http://docs.python.org/library/string.html#formatspec.                       
    """



    # =============================================
    #  CONSTRUCTOR
    # =============================================
    def __init__(self):
        self.__filename = None



    # =============================================
    #  CLASS METHODSstring
    # =============================================
    def get(self, pFilename, pDictionary=None):
        """
        Return a dictionary (or all dictionaries) stored in a certain XML file.

        @type pFilename: string
        @param pFilename: the file name where to get the dictionary (or all dictionaries).
        @type pDictionary: list
        @param pDictionary: the dictionary to be returned (if None, then all existing dictionaries stored in the XML file will be returned).
        @return: status, dictionaries       
        @rtype: int (status), list (containing a single dictionary) or dictionary (containing two or more dictionaries).
        """
        try:
            xmlHandler = _XMLHandler()
            parser = make_parser()
            parser.setContentHandler(xmlHandler)
            parser.parse(str(pFilename))
            dictionary = xmlHandler.getDictionary()
            if pDictionary is None:
                if len(dictionary) == 1:
                    return 0, dictionary[dictionary.keys()[0]]
                else:
                    return 0, dictionary
            else:
                pDictionary = str(pDictionary)
                if dictionary.has_key(pDictionary):
                    return 0, dictionary[pDictionary]
                else:
                    return 0, []
        except Exception:
            return - 1, []



    def translate(self, pMetaData, pDictionary=None):
        """
        Translate (extract and convert) a list of data using a certain dictionary.

        @type pMetaData: list
        @param pMetaData: the data to extract/convert the keywords and their values.
        @type pDictionary: list
        @param pDictionary: the dictionary to be used for the extraction/translation 
        of keywords and their values 
        (if None, then it is assumed that, for each line of the data, 
        the keyword is on the left side of "=" and the value is on the right side of "=").
        @return: status, metadata        
        @rtype: int (status), list of lists (containing the translated metadata)
        """
        status = 0
        result = []
        try:
            metaDataList = []
            for metaData in pMetaData:
                if pDictionary is None:
                    i = metaData.find("=")
                    if i != -1:
                        result.append([metaData[:i].strip(), metaData[i + 1:].strip()])
                else:
                    for keyWord, separator, finish, split, slice, format, translate in pDictionary:
                        if keyWord not in metaDataList:
                            i = metaData.find(keyWord)
                            if i != -1:
                                i = metaData.find(separator, len(keyWord) + i)
                                if i != -1:
                                    if len(finish) == 0:
                                        data = metaData[i + 1:].strip()
                                    else:
                                        j = metaData.find(finish, i + 1)
                                        if j == -1:
                                            data = metaData[i + 1:].strip()
                                        else:
                                            data = metaData[i + 1:j].strip()
                                    if len(slice) > 0:
                                        i = slice.find(":")
                                        if i == -1:
                                            j = slice
                                            k = ""
                                            flag = False
                                        else:
                                            j = slice[:i]
                                            k = slice[i + 1:]
                                            flag = True
                                    if len(split) == 0:
                                        if len(slice) > 0:
                                            if flag:
                                                if len(j) == 0:
                                                    data = data[:int(k)]
                                                else:
                                                    if len(k) == 0:
                                                        data = data[int(j):]
                                                    else:
                                                        data = data[int(j):int(k)]
                                            else:
                                                data = data[int(j)]
                                        if len(format) == 0:
                                            result.append([translate, data])
                                        else:
                                            result.append([translate, format % data])
                                    else:
                                        dataList = data.split(split)
                                        translateList = translate.split(",")
                                        if len(dataList) > len(translateList):
                                            count = len(translateList)
                                        else:
                                            count = len(dataList)
                                        for i in range(0, count):
                                            if len(slice) == 0:
                                                data = dataList[i].strip()
                                            else:
                                                if flag:
                                                    if len(j) == 0:
                                                        data = dataList[i].strip()[:int(k)]
                                                    else:
                                                        if len(k) == 0:
                                                            data = dataList[i].strip()[int(j):]
                                                        else:
                                                            data = dataList[i].strip()[int(j):int(k)]
                                                else:
                                                    data = dataList[i].strip()[int(j)]
                                            if len(format) == 0:
                                                result.append([translateList[i].strip(), data])
                                            else:
                                                result.append([translateList[i].strip(), format % data])

                                    metaDataList.append(keyWord)
            return status, result
        except Exception:
            return - 1, []




# =============================================
#  OTHER CLASS
# =============================================                 
class _XMLHandler(ContentHandler):


    # =============================================
    #  CONSTRUCTOR
    # =============================================    
    def __init__(self):
        ContentHandler.__init__(self)
        self.__result = None
        self.__dictionary = None
        self.__keyWord = None



    # =============================================
    #  CLASS METHODS
    # =============================================
    def getDictionary(self):
        return self.__result


    def startDocument(self):
        self.__result = {}
        self.__dictionary = ""
        self.__keyWord = []



    def startElement(self, pName, pAttributes):
        if pName == "dictionary":
            self.__dictionary = str(pAttributes["name"])
            self.__result[self.__dictionary] = []
        else:
            if pName == "keyword":
                self.__keyWord = [str(pAttributes["name"])]
                if pAttributes.has_key("separator"):
                    self.__keyWord.append(str(pAttributes["separator"]))
                else:
                    self.__keyWord.append("=")
                if pAttributes.has_key("finish"):
                    self.__keyWord.append(str(pAttributes["finish"]))
                else:
                    self.__keyWord.append("")
                if pAttributes.has_key("split"):
                    self.__keyWord.append(str(pAttributes["split"]))
                else:
                    self.__keyWord.append("")
                if pAttributes.has_key("slice"):
                    self.__keyWord.append(str(pAttributes["slice"]))
                else:
                    self.__keyWord.append("")
                if pAttributes.has_key("format"):
                    self.__keyWord.append(str(pAttributes["format"]))
                else:
                    self.__keyWord.append("")



    def characters(self, pContent):
        if len(self.__keyWord) > 0:
            self.__keyWord.append(str(pContent))
            self.__result[self.__dictionary].append(self.__keyWord)
            self.__keyWord = []



    def endDocument(self):
        pass




if __name__ == "__main__":


    # =============================================
    #  CHECK IF PARAMETERS ARE VALID
    # =============================================
    dictionaryFile = ""
    dictionaryName = ""
    inputFile = ""
    outputFile = ""
    maxLines = 0
    for i in range(1, len(sys.argv)):
        if sys.argv[i].upper() == "-HELP":
            print
            print "  -help          Show this help."
            print
            print "  -dic_file:x    Use dictionary XML file 'x'. This parameter is mandatory."
            print
            print "  -dic_name:x    Use dictionary name 'x'. If not specified, then the first dictionary found in the XML file is used."
            print
            print "  -input:x       Read data to be extracted/converted from file 'x'. This parameter is mandatory."
            print
            print "  -max:x         Read the first 'x' lines from input file. If not specified, then the input file is read until the end."
            print
            print "  -output:x      Save extracted/converted data to file 'x'. If not specified, then the output is displayed on screen."
            print
            sys.exit(0)
        else:
            if sys.argv[i][:10].upper() == "-DIC_FILE:":
                dictionaryFile = sys.argv[i][10:]
                if len(dictionaryFile) == 0:
                    print
                    print "Please, specify the dictionary file (example: /users/dummy/myDictionary.xml)."
                    print
                    sys.exit(-1)
                else:
                    if not os.path.isfile(dictionaryFile):
                        print
                        print "The dictionary file '" + dictionaryFile + "' does not exists!"
                        print
                        sys.exit(-1)
            else:
                if sys.argv[i][:10].upper() == "-DIC_NAME:":
                    dictionaryName = sys.argv[i][10:]
                    if len(dictionaryFile) == 0:
                        print
                        print "Please, specify the dictionary name (example: SPEC)."
                        print
                        sys.exit(-1)
                else:
                    if sys.argv[i][:7].upper() == "-INPUT:":
                        inputFile = sys.argv[i][7:]
                        if len(inputFile) == 0:
                            print
                            print "Please, specify the input file (example: /users/dummy/myInput.txt)."
                            print
                            sys.exit(-1)
                        else:
                            if not os.path.isfile(inputFile):
                                print
                                print "The input file '" + inputFile + "' does not exists!"
                                print
                                sys.exit(-1)
                    else:
                        if sys.argv[i][:5].upper() == "-MAX:":
                            maxLines = sys.argv[i][5:]
                            if len(maxLines) == 0:
                                print
                                print "Please, specify the maximum lines (example: 10)."
                                print
                                sys.exit(-1)
                            else:
                                if not maxLines.isdigit():
                                    print
                                    print "The maximum lines should be a number (example: 10)."
                                    print
                                    sys.exit(-1)
                                else:
                                    maxLines = int(maxLines)
                        else:
                            if sys.argv[i][:8].upper() == "-OUTPUT:":
                                outputFile = sys.argv[i][8:]
                                if len(outputFile) == 0:
                                    print
                                    print "Please, specify the output file (example: /users/dummy/myOutput.txt)."
                                    print
                                    sys.exit(-1)
                            else:
                                print
                                print "Parameter '" + sys.argv[i] + "' invalid. Please, execute with '-help' for valid parameters."
                                print
                                sys.exit(-1)



    # =============================================
    #  START PROCESSING
    # =============================================    
    if len(dictionaryFile) > 0:
        if len(inputFile) > 0:

            try:
                inputHandler = open(inputFile, "r")
                lineList = []
                countLines = 0
                for line in inputHandler:
                    lineList.append(line)
                    countLines += 1
                    if countLines == maxLines:
                        break
                inputHandler.close()

                hdfDictionary = HDFDictionary()

                if len(dictionaryName) == 0:
                    status, dictionaryList = hdfDictionary.get(dictionaryFile)
                    if len(dictionaryList) > 1:
                        dictionaryList = dictionaryList[dictionaryList.keys()[0]]
                else:
                    status, dictionaryList = hdfDictionary.get(dictionaryFile, dictionaryName)

                if status == 0:
                    status, translationList = hdfDictionary.translate(lineList, dictionaryList)
                    if status == 0:
                        if len(outputFile) > 0:
                            outputHandler = open(outputFile, "w")
                            for translation in translationList:
                                outputHandler.write(str(translation[0]) + "=" + str(translation[1]) + "\r\n")
                            outputHandler.close()
                        else:
                            for translation in translationList:
                                print str(translation[0]) + "=" + str(translation[1])
                    else:
                        raise(StandardError)
                else:
                    raise(StandardError)
            except Exception:
                print
                print "Error when processing. Exiting..."
                print
                sys.exit(-1)

            sys.exit(0)

        else:
            print
            print "Please, specify the input file parameter (example: -input:/users/dummy/myInput.txt)."
            print
            sys.exit(-1)
    else:
        print
        print "Please, specify the dictionary file parameter (example: -dic_name:/users/dummy/myDictionary.xml)."
        print
        sys.exit(-1)




