strEdml = """

complex type XSDataISPyBScreeningInput extends XSData {
    screeningInputId : XSDataInteger optional
    screeningId : XSDataInteger
    diffractionPlanId: XSDataInteger
    beamX : XSDataLength
    beamY : XSDataLength
    rmsErrorLimits : XSDataDouble
    minimumFractionIndexed : XSDataDouble
    maximumFractionRejected : XSDataDouble
    minimumSignalToNoise : XSDataDouble
    xmlSampleInformation : XSDataString
}

"""
#    def storeAutoProcProgram(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcProgram):
#        """Creates an entry in the ISPyB AutoProcProgram table"""
#        self.DEBUG("EDPluginISPyBStoreAutoProcv1_4.storeAutoProcProgram")
dictType = {"XSDataString" : "str", \
            "XSDataInteger" : "i", \
            "XSDataDouble" : "f", 
            "XSDataBoolean" : "b", \
            "XSDataLength"  : "f", \
            }
dictDefault = {"XSDataString" : "\"\"", \
            "XSDataInteger" : "0", \
            "XSDataDouble" : "-1.0", 
            "XSDataBoolean" : "False", \
            "XSDataLength"  : "9999.0", \
            }
def firstUpper(_strValue):
    return _strValue[0].upper()+_strValue[1:]

#f = open("../datamodel/XSDataISPyBv1_4.edml")
#strEdml = f.read()
#f.close()

# Parse XML
bDefiningWebService = False
for strLine in strEdml.split("\n"):
#    print strLine, bDefiningWebService
    if (strLine.find("extends XSData ") != -1) and not bDefiningWebService:
        bDefiningWebService = True
        iPos1 = strLine.find("XSDataISPyB")
        iPos2 = strLine.find("extends XSData ")
        strWebServiceName = strLine[iPos1+11:iPos2-1]
        listApi = []
    elif (strLine.find("}") != -1) and bDefiningWebService:
        bDefiningWebService = False
        #        print strAttribute, strType
        #    print bDefiningWebService, [strLine]
#        print strWebServiceName
#        print listApi
        bAbort = False
        strClientCode = "    def storeOrUpdate%s(self, _clientToolsForScreeningEDNAWebServiceWsdl, _xsDataISPyB%s):\n" %\
            (strWebServiceName, strWebServiceName)
        strClientCode += "        \"\"\"Creates an entry in ISPyB for the %s table\"\"\"\n" % strWebServiceName
        strClientCode += "        self.DEBUG(\"EDPluginISPyBStoreScreeningv1_4.store%s\")\n" % strWebServiceName
        for listAttribute in listApi:
            strAttribute = listAttribute[0]
            strType = listAttribute[1]
            if not strType in dictType.keys():
                print "Warning! Unrecognized type %s in attribute %s for %s" % (strType, strAttribute, strWebServiceName)
                bAbort = True
            else:
                strPrefix = dictType[listAttribute[1]]
                strDefault = dictDefault[listAttribute[1]]
                strClientCode += "        %s%s = self.getXSValue(_xsDataISPyB%s.%s, %s)\n" % \
                    (strPrefix, firstUpper(strAttribute), strWebServiceName, strAttribute, strDefault)
        if not bAbort:
            strClientCode += "        i%sId = _clientToolsForScreeningEDNAWebServiceWsdl.service.storeOrUpdate%s(\n" % (strWebServiceName, strWebServiceName)
            iIndex = 0
            for listAttribute in listApi:
                strAttribute = listAttribute[0]
                strPrefix = dictType[listAttribute[1]]
                strDefault = dictDefault[listAttribute[1]]
                strClientCode += "            in%d = %s%s, \\\n" % (iIndex, strPrefix, firstUpper(strAttribute))
                iIndex += 1
            strClientCode += "            )\n"
            strClientCode += "        self.DEBUG(\"%sId: %%d\" %% i%sId)\n" % (strWebServiceName, strWebServiceName)
            strClientCode += "        return i%sId\n" % strWebServiceName
            print strClientCode
    elif bDefiningWebService:
        listSplit = strLine.split()
        print listSplit
        if len(listSplit) > 1:
            strAttributeName = listSplit[0].split(":")[0]
            if len(listSplit)>2:
                strType = listSplit[2]                
            else:
                strType = listSplit[1]
            listApi.append([strAttributeName, strType])
            print strAttributeName, strType
