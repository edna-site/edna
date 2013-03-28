import numpy, os, tempfile, sys
import re

#strDataFileBaseName = "dimer+amine_conc_1b_log_0"
strDataFileBaseName = "Pdfoil_sequence_02_log_0"
if not "file_path" in dir():
    file_path = "/users/pommier/workspace-id24/data/ID24/20120530/%s" % strDataFileBaseName
    #file_path = "/users/pommier/workspace-id24/data/ID24/20120529/%s" % strDataFileBaseName

file_name = os.path.basename(file_path)

f = open(file_path)
strData = f.read()
f.close()

listLines = strData.split("\n")

n1 = len(listLines)-2
n2 = len(listLines[1].split(" "))

#print(n1, n2)

dataArray = numpy.ndarray((n1,n2-1))
calibratedEnergy = numpy.ndarray((n1))
Images=numpy.ndarray((n2-1))
Edge=numpy.ndarray((n2-1,1)) #remove the 2nd line, the table first one is empty 
Slope=numpy.ndarray((n2-1,1))
Jump=numpy.ndarray((n2-1,1))
Hwl=numpy.ndarray((n2-1,1))
EWL=numpy.ndarray((n2-1,1))

a = 23.650
b = 0.001
c = 0.0
d = 0.0

index = 0
for strLine in listLines[1:-1]:
    listStrValues = strLine.split(" ")
    if '' in listStrValues:
        listStrValues.remove('')
    listFloatValues = map(float, listStrValues)
    fIndex = listFloatValues[0]
    calibratedEnergy[index] = a + b*fIndex + c*fIndex**2 + d*fIndex**3
    dataArray[index, :] = listFloatValues[1:]
    index += 1


indexImages=0
for n in range(n2-1):
    Images[indexImages]=indexImages
    indexImages=indexImages+1
    
Imagesbis=Images[1:];Imagesbis
#print Images
print Imagesbis
import h5py


#print "Write a NeXus HDF5 file"
fileName = "/users/pommier/workspace-id24/id24_tests/output/%s.hdf5" % strDataFileBaseName
timestamp = "2010-10-18T17:17:04-0500"

## load data from two column format
#data = numpy.loadtxt('input.dat').T
#mr_arr = data[0]
#i00_arr = numpy.asarray(data[1],'int32')
def makeFile(filename, **attr):
    f = h5py.File(filename, "w")
    add_attributes(f, attr)
    return f

def add_attributes(parent, attr):
    """
    add attributes to an h5py data item
    
    :param obj parent: h5py parent object
    :param dict attr: dictionary of attributes
    """
    if attr and type(attr) == type({}):
        # attr is a dictionary of attributes
        for k, v in attr.items():
            parent.attrs[k] = v

def makeDataset(parent, name, data = None, **attr):
    if data == None:
        obj = parent.create_dataset(name)
    else:
        obj = parent.create_dataset(name, data=data)
    add_attributes(obj, attr)
    return obj 

def makeGroup(parent, name, nxclass, **attr):
    group = parent.create_group(name)
    group.attrs["NX_class"] = nxclass
    add_attributes(group, attr)
    return group

# create the HDF5 NeXus file
f = makeFile(fileName, file_name=fileName,
file_time=timestamp,
instrument="APS USAXS at 32ID-B",
creator="test_convert_to_nexus.py",
NeXus_version="4.3.0",
HDF5_Version=h5py.version.hdf5_version,
h5py_version=h5py.version.version) 


nxentry = makeGroup(f, "entry", "NXentry")
makeDataset(nxentry, 'title', data='id24 scan')

nxdata = makeGroup(nxentry, "energy_scan", "NXdata", long_name='Energy (keV)')

makeDataset(nxdata, "Energy (keV)", calibratedEnergy, axis=1,primary=2, units='keV', long_name='Energy (keV)')

makeDataset(nxdata, "Image number", Images, axis=0,primary=1, units='number', long_name='Image number')

makeDataset(nxdata, "I0 (counts)", dataArray.transpose(), units='counts',
            signal='1', # Y axis of default plot
            axes='Energy (keV):Image number', # name of X and Y axes
            long_name='I0 (counts)')
            






#print dataArray

dir = tempfile.mkdtemp(prefix="dawn-jesf-")
os.chdir(dir)
print dir
#print dir

#strJesfBashScript = """#!/bin/bash
#/users/pommier/bin/jesf > /dev/null << EOF
#spectra.dat
#EOF
#"""

strJesfBashScript = """#!/bin/bash
/users/pommier/bin/jesf > jesf.log << EOF
spectra.dat
EOF
"""

f = open("jesf.bat", "w")
f.write(strJesfBashScript)
f.close()
#print calibratedEnergy
#print dataArray

dataFort92 = None
dataFort95 = None
dataFort96 = None
dataFort97 = None
dataFort98 = None
dataFort99 = None



cutOff95 = 1200
cutOff96 = 1200
cutOff97 = 200

dataFort95_x = None
dataFort96_x = None
dataFort97_x = None

for index in range(n2-1):
#for index in range(10):
    spectra = numpy.ndarray((2,n1))
    spectra[0,:] = calibratedEnergy[:]
    spectra[1,:] = dataArray[:, index]
    #print spectra.transpose()
    numpy.savetxt("spectra.dat", spectra.transpose(), fmt='%.6e')
    os.system("bash jesf.bat")
    
    # read the jesf log file
    if os.path.exists("jesf.log"):
        f = open("jesf.log")
        jesf_log = f.readlines()
        f.close()
        
    #print jesf_log[0:10]
    print jesf_log
    for line in jesf_log:       
     print  line.rstrip('\n\r').split(",")
     if re.search('EDGE',line):
         regex = re.compile('([0-9]+)\.([0-9]+)')
         resultatEdge = regex.search(line)     
         Edge[index]=resultatEdge.group(0)
     if re.search('SLOPE',line):
         regex = re.compile('([0-9]+)\.([0-9]+)')
         resultatSlope = regex.search(line)     
         Slope[index]=resultatSlope.group(0)
     if re.search('JUMP',line):
         regex = re.compile('([0-9]+)\.([0-9]+)')
         resultatJump = regex.search(line)     
         Jump[index]=resultatJump.group(0)
     if re.search('EWL',line):
         regex = re.compile('([0-9]+)\.([0-9]+)')
         resultatEwl = regex.search(line)
         EWL[index]=0 
         if resultatEwl is not None:
             resultatEwlFloat=float(resultatEwl.group(0))
             resultatEwlInt=int(resultatEwlFloat)
             EWL[index]=resultatEwlFloat 
     if re.search('hwl',line):
         regex = re.compile('([0-9]+)\.([0-9]+)')
         resultatHwl = regex.search(line)     
         Hwl[index]=resultatHwl.group(0)
  
    
#    sys.exit(1)
    # fort.95
    if os.path.exists("fort.95"):
        dataTmpFort95 = numpy.genfromtxt("fort.95")
        (dimTmp95x, dimTmp95y) = dataTmpFort95.shape
        if dataFort95 is None:
            dataFort95 = numpy.ndarray((n1,n2-1))
        else:
            if dataFort95_x is None:
                dataFort95_x = numpy.ndarray((n1))
            dataFort95_x[:dimTmp95x] = dataTmpFort95[:, 0]
    #            makeDataset(nxdataResult, "dataFort95 ", dataFort95, axis=1,primary=1, units='number', long_name='dataFort95 Result')                  
            dataFort95[:dimTmp95x,index] = dataTmpFort95[:, 1]
            dataFort95bis=dataFort95[:,1:];dataFort95bis
        os.remove("fort.95")
       
    # fort.96
    if os.path.exists("fort.96"):
        dataTmpFort96 = numpy.genfromtxt("fort.96")
        (dimTmp96x, dimTmp96y) = dataTmpFort96.shape
        print dataTmpFort96.shape
        if dataFort96 is None:
            dataFort96 = numpy.ndarray((cutOff96,n2-1))
        else:    
            if dataFort96_x is None:
                dataFort96_x = dataTmpFort96[:cutOff96, 0]
#            makeDataset(nxdataResult, "dataFort96 ", dataFort96, axis=1,primary=1, units='number', long_name='dataFort96 Result')      
            dataFort96[:,index] = dataTmpFort96[:cutOff96, 1]
            dataFort96bis=dataFort96[:,1:];dataFort96bis
        os.remove("fort.96")
    # fort.97
    if os.path.exists("fort.97"):
        dataTmpFort97 = numpy.genfromtxt("fort.97")
        (dimTmp97x, dimTmp97y) = dataTmpFort97.shape
        print dataTmpFort97.shape
        if dataFort97 is None:
            dataFort97 = numpy.ndarray((cutOff97,n2-1))
        else:
            if dataFort97_x is None:
                dataFort97_x = dataTmpFort97[:cutOff97, 0]
#            makeDataset(nxdataResult, "dataFort97 ", dataTmpFort97, axis=1,primary=1, units='number', long_name='dataTmpFort97 Result')
        #print   dataFort97.shape
        #print dataTmpFort97.shape
        #print dataTmpFort97[:cutOff97, 1].shape
            dataFort97[:,index] = dataTmpFort97[:cutOff97, 1]
            dataFort97bis=dataFort97[:,1:];dataFort97bis
        os.remove("fort.97")
    os.remove("spectra.dat")

#print dataFort95_x
#print dataFort95
nxentryResult = makeGroup(nxentry, "Result", "NXentryResult")
nxDataFort95 = makeGroup(nxentryResult, "dataFort95", "NXdataResult", long_name='DataFort95')
makeDataset(nxDataFort95, "log [I0|I1] ", Imagesbis, axis=0,primary=2, units='IO/I1', long_name='log [I0/I1]') 
makeDataset(nxDataFort95, "Energy [KeV]", dataFort95_x, axis=1,primary=1, units='keV', long_name='Energy [KeV]')                  
makeDataset(nxDataFort95, "Absortion", dataFort95bis.transpose(), units='counts',
            signal='1', # Y axis of default plot
            axes='Image:k', # name of X and Y axes
            long_name='k  chi(k)')


#print dataFort96_x
#print dataFort96
nxDataFort96 = makeGroup(nxentryResult, "dataFort96", "NXdataResult", long_name='DataFort96')
makeDataset(nxDataFort96, "Photoelectron wavector, K[Angs.-1]", dataFort96_x, axis=1,primary=1, units='K', long_name='Photoelectron wavector, K[Angs.-1]')                  
makeDataset(nxDataFort96, "Fine Structure, chi*K*K [Angs.-1] ", Imagesbis, axis=0,primary=2, units='chi*K*K [Angs.-1]', long_name='Fine Structure, chi*K*K [Angs.-1]') 
makeDataset(nxDataFort96, "Fine Structure weight by k*k", dataFort96bis.transpose(), units='counts',
            signal='1', # Y axis of default plot
            axes='k:Image', # name of X and Y axes
            long_name='k  k^2.chi(k)')




nxDataFort97 = makeGroup(nxentryResult, "dataFort97", "NXdataResult", long_name='DataFort97')
makeDataset(nxDataFort97, "R[Angs.]", dataFort97_x, axis=1,  primary=1, units='R', long_name='R[Angs.]')                  
makeDataset(nxDataFort97, "IF.T.I", Imagesbis, axis=0, primary=2, units='IF.T.I', long_name='IF.T.I') 
makeDataset(nxDataFort97, "Modulus of Fourier Transform ", dataFort97bis.transpose(), units='counts',
            signal='1', # Y axis of default plot
            axes='R:Image number', # name of X and Y axes
            long_name='R  |chi(R)|')


nxEdge = makeGroup(nxentryResult, "Edge", "NXEDGE", long_name='EDGE')                
makeDataset(nxEdge, "Image number", Images, axis=0,primary=1, units='number', long_name='Image number')
makeDataset(nxEdge, "EDGE", Edge, axis=1,primary=2, units='Edge', long_name='Edge')


nxSlope = makeGroup(nxentryResult, "Slope", "NXSLOPE", long_name='SLOPE')                
makeDataset(nxSlope, "Image number", Images, axis=0,primary=1, units='number', long_name='Image number')
makeDataset(nxSlope, "SLOPE", Slope, axis=1,primary=2, units='Slope', long_name='Slope')


nxJump = makeGroup(nxentryResult, "Jump", "NXJUMP", long_name='JUMP')                
makeDataset(nxJump, "Image number", Images, axis=0,primary=1, units='number', long_name='Image number')
makeDataset(nxJump, "JUMP", Jump, axis=1,primary=2, units='Jump', long_name='Jump')


nxEwl = makeGroup(nxentryResult, "Ewl", "NXEWL", long_name='EWL')                
makeDataset(nxEwl, "Image number", Images, axis=0,primary=1, units='number', long_name='Image number')
makeDataset(nxEwl, "EWL", EWL, axis=1,primary=2, units='EWL', long_name='Ewl')


nxHwl = makeGroup(nxentryResult, "Hwl", "NXHWL", long_name='HWL')                
makeDataset(nxHwl, "Image number", Images, axis=0,primary=1, units='number', long_name='Image number')
makeDataset(nxHwl, "HWL", Hwl, axis=1,primary=2, units='Hwl', long_name='Hwl')

            

f.close() # be CERTAIN to close the file



print "wrote file:", fileName 


