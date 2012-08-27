"""
=============================================
  NAME       : EDF (EDF.py)
  
  DESCRIPTION:
    
  VERSION    : 1

  REVISION   : 0

  RELEASE    : 2009/MAR/04

  PLATFORM   : None

  EMAIL      : ricardo.fernandes@esrf.fr
  
  HISTORY    :
=============================================
"""


# =============================================
#  IMPORT MODULES
# =============================================
try:
    import os
    import sys
except Exception:
    print __name__ + ".py: error when importing module!"




# =============================================
#  CLASS DEFINITION
# =============================================
class EDF:



    # =============================================
    #  CONSTRUCTOR
    # ============================================= 
    def __init__(self):
        self.__handler = None        
        self.__filename = None



    # =============================================
    #  CLASS METHODS
    # =============================================
    def getFilename(self):
        return self.__filename
    

    
    def open(self, pFilename, pMode = "r+"):
        try:
            self.__filename = str(pFilename)
            self.__handler = open(self.__filename, str(pMode))
            return 0
        except Exception:
            return -1



    def close(self):
        try:
            self.__handler.close()
            return 0
        except Exception:
            return -1




    def isValid(self):            
        try:
            self.__handler.seek(0)
            if self.__handler.read(1) == "{":                                              
                return 0
            else:
                return -1                                              
        except Exception:
            return -1
        


    def getHeader(self, pSplit = False):
        header = []
        try:
            self.__handler.seek(1)
            lines = self.__handler.read(8192).split(";")
            count = len(lines)                                     
            for i in range(0, count):                 
                if pSplit:
                    j = lines[i].find("=")
                    if j != -1:
                        header.append([lines[i][1:j].strip(), lines[i][j + 1:].strip()])
                else:                 
                    #if i > 0:
                    header.append(lines[i][2:-1])
        except Exception:
            pass
        return header    
                


    def getValues(self):        
        result = ""
        try:
            self.__handler.seek(8192)                
            while True:
                tmp = self.__handler.read(1024)
                if tmp == "":
                    break
                else:
                   result.join(tmp)
        except Exception:
            pass            
        return result
    
    



if __name__ == "__main__":

    edf = EDF()
    
    print edf.open("/bliss/users/nogueira/workspace/data/processing/test_001_01.edf")
    
    print edf.isValid()
    
    print edf.getHeader()
    
    print len(edf.getValues())
    
    print edf.close()
    

