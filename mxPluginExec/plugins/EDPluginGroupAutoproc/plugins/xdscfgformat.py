#some kw can be specified multiple times (values are accumulated in a
#list I guess). Those are: EXCLUDE_RESOLUTION_RANGE, SPOT_RANGE

REPEATABLE_PARAMS = ['UNTRUSTED_RECTANGLE=',
                     'UNTRUSTED_ELLIPSE=',
                     'UNTRUSTED_QUADRILATERAL=',
                     'EXCLUDE_RESOLUTION_RANGE=',
                     'SPOT_RANGE=']


# parsers

class List(object):
    # check length
    # apply the transform on items
    # default transform -> id
    def __init__(self, numargs, transform=lambda x: x):
        self.transform = transform
        self.numargs = numargs
    def __call__(self, chunks):
        if self.numargs is not None:
            if len(chunks) != self.numargs:
                raise ValueError, "not the right number of args"

        return [self.transform(elem) for elem in chunks]

class Image(object):
    # XXX check for allowed image formats
    # format is:
    # filepath optional_format
    def __call__(self, chunks):
        KNOWN_FORMATS = []

        if len(chunks) > 3 or len(chunks) < 1:
            raise ValueError, "wrong file spec: %s" % chunk
        if len(chunks) == 2:
            #2nd val is the format, check it
            if chunks[1] not in KNOWN_FORMATS:
                # log stuff?
                pass
        #XXX look into the 3 args version where the access is defined
        #in addition to the file path
        return chunks


class Enumeration(object):
    # check if the transformed value is an allowed value
    # default is used if no parameters to parse
    def __init__(self, possible_values, transform=lambda x: x, default=None):
        self.possible_values = possible_values
        self.transform = transform
        self.default = default
    def __call__(self, chunks):
        if len(chunks) == 0:
            if self.default is not None:
                return self.default
        vals = [self.transform(elem) for elem in chunks]
        for val in vals:
            if val not in self.possible_values:
                raise ValueError, "val %s not in %s" % (val, self.possible_values)
        return vals

class Jobs(Enumeration):
    # XDS jobs
    def __init__(self):
        JOBS = [ "ALL", "XYCORR", "INIT",
                 "COLSPOT", "IDXREF", "DEFPIX",
                 "XPLAN", "INTEGRATE", "CORRECT"]
        Enumeration.__init__(self, JOBS, default='ALL')

class Value(object):
    def __init__(self, transform=lambda x: x):
        self.transform = transform
    def __call__(self, chunks):
        if len(chunks) != 1:
            raise ValueError, 'more than one value to parse'
        return self.transform(chunks[0])

class BoundedList(object):
    def __init__(self, maxsize, transform=lambda x:x):
        self.maxsize= maxsize
        self.transform = transform
    def __call__(self, chunks):
        if not (0 < len(chunks) < self.maxsize):
            raise ValueError, "too many or too few args: %s" % chunks
        return [transform(elem) for elem in chunks]

class RefineJobs(Enumeration):
    def __init__(self):
        JOBS =[ 'ALL', 'DISTANCE', 'BEAM',
                'AXIS', 'ORIENTATION', 'CELL']

        Enumeration.__init__(self, JOBS, default='ALL')

class Corrections(Enumeration):
    def __init__(self):
        JOBS = [ 'ALL',  'DECAY',  'MODULATION',  'ABSORPTION' ]
        Enumeration.__init__(self, JOBS, default='ALL')

class Boolean(object):
    def __init__(self, default=None):
        self.default = default
    def __call__(self, chunks):
        if len(chunks) == 0:
            if self.default is not None:
                return self.default
            else:
                raise ValueError, 'empty param and no default value'
        param = chunks[0] # yep, we ignore trailing params
        if param == 'TRUE':
            return True
        elif param == 'FALSE':
            return False
        else:
            raise ValueError, 'Strange value for boolean: %s' % param

class Dataset(object):
    def __init__(self):
        pass
    def __call__(self, chunks):
        VALID_FORMATS = [ 'XDS_ASCII', 'DIRECT', 'ANOMAL',
                          'NORMAL', 'OLDHKL', 'UNIQUE']
        if len(chunks) == 1:
            return chunks
        if len(chunks) == 2:
            if chunks[1] not in VALID_FORMATS:
                raise ValueError, 'Invalid format %s' % chunks[1]
            return chunks
        raise ValueError, 'too few or many params: %s' % chunks

# return the float value and wether it is fixed or not in a list
class FittableDose(object):
    def __init__(self):
        pass
    def __call__(self, chunks):
        if len(chunks) != 1:
            raise ValueError, "wrong number of params: %s" % chunks
        val = chunks[0]
        if val.endswith('*'):
            return [float(val[:-1]), True]
        else:
            return [float(val), False]

# dispatch table, format is
# keyword: transform
# transform will be passed the raw param as is (after comments are removed)
CONFIGURATION_PARSERS = {
    #Job control:
    'JOB=': Jobs(),
    'MAXIMUM_NUMBER_OF_JOBS=': Value(int),
    'MAXIMUM_NUMBER_OF_PROCESSORS=': Value(int),
    'SECONDS=': Value(int),
    'TEST=': Value(int), # in [0, 2]
    #Detector hardware:
    'DETECTOR=': Value(str), # also restricted list
    'NX=': Value(int),
    'NY=': Value(int),
    'QX=': Value(float),
    'QY=': Value(float),
    'OVERLOAD=': Value(int),
    'MINIMUM_VALID_PIXEL_VALUE=': Value(float),#well i guess it's a float
    'TRUSTED_REGION=': List(2, transform=float),
    'UNTRUSTED_RECTANGLE=': List(4, transform=int),
    'UNTRUSTED_ELLIPSE=': List(4, transform=int),
    'UNTRUSTED_QUADRILATERAL=': List(8, transform=int),
    'SILICON=': Value(float),
    'SENSOR_THICKNESS=': Value(float),
    #Detector distortions:
    'ROFF=': Value(float), # i guess those two are floats
    'TOFF=': Value(float),
    'STOE_CALIBRATION_PARAMETERS=': List(8, transform=float),
    'BRASS_PLATE_IMAGE=': List(2),
    'HOLE_DISTANCE=': Value(float),
    'MXHOLE=': Value(int),
    'MNHOLE=': Value(int),
    'X-GEO_CORR=': Image(),
    'Y-GEO_CORR=': Image(),
    #Detector noise:
    'DARK_CURRENT_IMAGE=': Image(),
    'OFFSET=': Value(int),
    #Trusted detector region:
    'VALUE_RANGE_FOR_TRUSTED_DETECTOR_PIXELS=': List(2, transform=int),
    'INCLUDE_RESOLUTION_RANGE=': List(2, transform=float),
    'EXCLUDE_RESOLUTION_RANGE=': List(2, transform=float),
    'MINIMUM_ZETA=': Value(float),
    #Data images:
    'NAME_TEMPLATE_OF_DATA_FRAMES=': Image(), # except the filename
                                              # may contain the ?
                                              # wildcard
    'DATA_RANGE=': List(2, transform=int),
    'BACKGROUND_RANGE=': List(2, int),
    'SPOT_RANGE=': List(2, transform=int),
    #Detector position:
    'ORGX=': Value(float),
    'ORGY=': Value(float),
    'DETECTOR_DISTANCE=': Value(float),
    'DIRECTION_OF_DETECTOR_X-AXIS=': List(3, transform=float),
    'DIRECTION_OF_DETECTOR_Y-AXIS=': List(3, transform=float),
    #Rotation axis:
    'ROTATION_AXIS=': List(3, transform=float),
    'OSCILLATION_RANGE=': Value(float),
    #Incident beam:
    'X-RAY_WAVELENGTH=': Value(float),
    'INCIDENT_BEAM_DIRECTION=': List(3, transform=float),
    'FRACTION_OF_POLARIZATION=': Value(float),
    'POLARIZATION_PLANE_NORMAL=': List(3, float),
    'AIR=': Value(float),
    #Crystal:
    'SPACE_GROUP_NUMBER=': Value(int),
    'UNIT_CELL_CONSTANTS=': List(6, transform=float),
    'UNIT_CELL_A-AXIS=': List(3, transform=float),
    'UNIT_CELL_B-AXIS=': List(3, transform=float),
    'UNIT_CELL_C-AXIS=': List(3, transform=float),
    'REIDX=': List(12, transform=int),
    'FRIEDEL\'S_LAW=': Boolean(),
    'STARTING_ANGLE=': Value(float),
    'STARTING_FRAME=': Value(int),
    'STARTING_ANGLES_OF_SPINDLE_ROTATION=': List(3, transform=float),
    'TOTAL_SPINDLE_ROTATION_RANGES=': List(3, transform=float),
    'RESOLUTION_SHELLS=': BoundedList(13, transform=float),
    'REFERENCE_DATA_SET=': Value(str), # a filename in fact
    'MAX_CELL_AXIS_ERROR=': Value(float),
    'MAX_CELL_ANGLE_ERROR=': Value(float),
    'TEST_RESOLUTION_RANGE=': List(2, float),
    'MIN_RFL_Rmeas=': Value(int),
    'MAX_FAC_Rmeas=': Value(float),
    #Background and peak pixels:
    'NBX=': Value(int),
    'NBY=': Value(int),
    'BACKGROUND_PIXEL=': Value(float),
    'STRONG_PIXEL=': Value(float),
    'MAXIMUM_NUMBER_OF_STRONG_PIXELS=': Value(int),
    'MINIMUM_NUMBER_OF_PIXELS_IN_A_SPOT=': Value(int),
    'SPOT_MAXIMUM-CENTROID=': Value(float),
    'SIGNAL_PIXEL=': Value(float),
    #Indexing and refinement:
    'INDEX_ORIGIN=': List(3, float),
    'INDEX_ERROR=': Value(float),
    'INDEX_MAGNITUDE=': Value(int),
    'INDEX_QUALITY=': Value(float), # in [0 .. 1]
    'SEPMIN=': Value(float),
    'CLUSTER_RADIUS=': Value(int),
    'MAXIMUM_ERROR_OF_SPOT_POSITION=': Value(float),
    'MAXIMUM_ERROR_OF_SPINDLE_POSITION=': Value(float),
    'MINIMUM_FRACTION_OF_INDEXED_SPOTS=': Value(float),
    'REFINE(IDXREF)=': RefineJobs(),
    'REFINE(INTEGRATE)=': RefineJobs(),
    'REFINE(CORRECT)=': RefineJobs(),
    #Peak profiles:
    'REFLECTING_RANGE=': Value(float),
    'REFLECTING_RANGE_E.S.D.=': Value(float),
    'BEAM_DIVERGENCE=': Value(float),
    'BEAM_DIVERGENCE_E.S.D.=': Value(float),
    # the 2 following must be odd and in [0..22]
    # might check that constraint later if necessary
    'NUMBER_OF_PROFILE_GRID_POINTS_ALONG_ALPHA/BETA=': Value(int),
    'NUMBER_OF_PROFILE_GRID_POINTS_ALONG_GAMMA=': Value(int),
    'CUT=': Value(float),
    'DELPHI=': Value(float),
    'MINPK=': Value(float), #percentage
    'WFAC1=': Value(float),
    'PROFILE_FITTING=': Boolean(),
    #Correction factors:
    'STRICT_ABSORPTION_CORRECTION=': Boolean(),
    'PATCH_SHUTTER_PROBLEM=': Boolean(),
    'CORRECTIONS=': Corrections(),
    'MINIMUM_I/SIGMA=': Value(float),
    'NBATCH=': Value(int),
    'REFLECTIONS/CORRECTION_FACTOR=': Value(int),
    'REJECT_ALIEN=': Value(float),
    'FIXED_SCALE_FACTOR=': Boolean()
}
