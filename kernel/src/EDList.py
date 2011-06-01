
################################################################################
# Warning: Deprecation mode 
# This code will be deleted by ... June 7th 2010
################################################################################


from EDVerbose import EDVerbose
_strDeprecate = "Deprecation by Monday 7th June 2010 of EDList, called "
class EDList(list):
    """
    Interface for EDList objects.
    """
    def __init__(self, _oList=[]):
        EDVerbose.WARNING(_strDeprecate + "init")
#        ALObject.__init__(self)
        list.__init__(self)
        for i in _oList:
            self.append(i)


    def getNumberObjects(self):
        EDVerbose.WARNING(_strDeprecate + "getNumberObjects")
        return len(self)
