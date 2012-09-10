from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFloat
x = XSDataBoolean(True)
print x.value
print x.marshal()
x = XSDataBoolean(False)
print x.value
print x.marshal()
x = XSDataBoolean('true')
print x.value
print x.marshal()
x = XSDataBoolean('False')
print x.value
print x.marshal()
x = XSDataBoolean(0)
print x.value
print x.marshal()
x = XSDataBoolean(1)
print x.value
print x.marshal()
x = XSDataBoolean(2)
print x.value
print x.marshal()
y = XSDataFloat('this is not a float')
print y.value
print y.marshal()
z = XSDataInteger('this is not an integer')
print z.value
print z.marshal()
