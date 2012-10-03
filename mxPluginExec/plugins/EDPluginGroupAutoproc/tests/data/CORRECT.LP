
 ***** CORRECT *****  (VERSION  December 6, 2010)            20-Sep-2011

 INPUT PARAMETER VALUES
 ----------------------
 SPACE_GROUP_NUMBER=    1 as used in the INTEGRATE step
 UNIT_CELL_CONSTANTS=    54.321    54.317   107.301  89.962  89.988 120.008 as used by INTEGRATE
 FRIEDEL'S_LAW=TRUE 
 PROFILE_FITTING= TRUE 
 OVERLOAD=   1048500     MINPK=  75.0    WFAC1=   1.0
 INCLUDE_RESOLUTION_RANGE=    50.000     0.000
 NAME_TEMPLATE_OF_DATA_FRAMES=../../tryp1_2_????.cbf CBF                        
 DATA_RANGE=       1     120
 ROTATION_AXIS=  0.999987 -0.001156  0.004882
 OSCILLATION_RANGE=  1.000000
 STARTING_ANGLE=   102.000     STARTING_FRAME=       1
 X-RAY_WAVELENGTH=  0.976270
 INCIDENT_BEAM_DIRECTION= -0.007989  0.004299  1.024267
 FRACTION_OF_POLARIZATION=   0.980
 POLARIZATION_PLANE_NORMAL=  0.000000  1.000000  0.000000
 AIR=   0.00031
 SILICON=  3.670588 SENSOR_THICKNESS=  0.320000
 DETECTOR=PILATUS                                           
 DIRECTION_OF_DETECTOR_X-AXIS=   1.00000   0.00000   0.00000
 DIRECTION_OF_DETECTOR_Y-AXIS=   0.00000   1.00000   0.00000
 DETECTOR_DISTANCE=   357.016
 ORGX=   1242.57  ORGY=   1246.63
 NX=  2463  NY=  2527    QX=  0.172000  QY=  0.172000
 BEAM_DIVERGENCE_E.S.D.=   0.044
 REFLECTING_RANGE_E.S.D.=   0.175
 MINIMUM_ZETA=     0.150
 MAXIMUM_ERROR_OF_SPOT_POSITION=   3.0
 MAXIMUM_ERROR_OF_SPINDLE_POSITION=   2.0
 MINIMUM_I/SIGMA=   3.0
 REFLECTIONS/CORRECTION_FACTOR=      50
 STRICT_ABSORPTION_CORRECTION=FALSE 
 CORRECTIONS= DECAY MODULATION ABSORPTION                      
 REFERENCE_DATA_SET=                                                  


  147072 REFLECTIONS ON FILE "INTEGRATE.HKL"
       0 CORRUPTED REFLECTION RECORDS (IGNORED)
       0 REFLECTIONS INCOMPLETE OR OUTSIDE IMAGE RANGE       1 ...     120
      25 OVERLOADED REFLECTIONS (IGNORED)
       0 REFLECTIONS OUTSIDE ACCEPTED RESOLUTION RANGES
                OR TOO CLOSE TO ROTATION AXIS (IGNORED)
  147047 REFLECTIONS ACCEPTED



 ******************************************************************************
                      AUTOMATIC SPACE GROUP ASSIGNMENT
 ******************************************************************************

 XDS adopts the following approach.
 (1) it looks for possible symmetries of the crystal lattice
 (2) it computes a redundancy independent R-factor for all enantiomorphous
     point groups compatible with the observed lattice symmetry.
 (3) it selects the group which explains the intensity data at an acceptable,
     redundancy-independent R-factor (Rmeas, Rrim) using a minimum number of
     unique reflections.

 This approach does not test for the presence of screw axes. Consequently,
 orthorhombic cell axes will be specified in increasing length (following
 conventions), despite the possibility that different assignments for the
 cell axes could become necessary for space groups P222(1) and P2(1)2(1)2
 containing one or two screw axes, respectively.

 The user can always override the automatic decisions by specifying the
 correct space group number and unit cell constants in XDS.INP and repeating
 the CORRECT step of XDS. This provides a simple way to rename orthorhombic
 cell constants if screw axes are present.

 In addition, the user has the option to specify in XDS.INP
 (a) a reference data set or
 (b) a reindexing transformation or
 (c) the three basis vectors (if known from processing a previous data set
 taken at the same crystal orientation in a multi-wavelength experiment).
 These features of XDS are useful for resolving the issue of alternative
 settings of polar or rhombohedral cells (like P4, P6, R3).

 =====> Specifications provided by the user in XDS.INP:
 SPACE_GROUP_NUMBER=  152 (0: unknown symmetry and unit cell)
 UNIT_CELL_CONSTANTS=    54.30    54.30   107.30  90.000  90.000 120.000
 UNIT_CELL_A-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_B-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_C-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 REIDX=  0  0  0  0  0  0  0  0  0  0  0  0 (all 0 : not specified)
 TEST_RESOLUTION_RANGE=   10.00    5.00 (Angstrom) for space group determination
 NUMBER OF ACCEPTED REFLECTIONS FOR CALCULATING Rmeas             4771
 NUMBER OF ACCEPTED UNIQUE REFLECTIONS FROM REFERENCE DATA SET       0


 *********** DETERMINATION OF LATTICE CHARACTER AND BRAVAIS LATTICE ***********

 The CHARACTER OF A LATTICE is defined by the metrical parameters of its
 reduced cell as described in the INTERNATIONAL TABLES FOR CRYSTALLOGRAPHY
 Volume A, p. 746 (KLUWER ACADEMIC PUBLISHERS, DORDRECHT/BOSTON/LONDON, 1989).
 Note that more than one lattice character may have the same BRAVAIS LATTICE.

 A lattice character is marked "*" to indicate a lattice consistent with the
 observed locations of the diffraction spots. These marked lattices must have
 low values for the QUALITY OF FIT and their implicated UNIT CELL CONSTANTS
 should not violate the ideal values by more than
 MAX_CELL_AXIS_ERROR=  0.03
 MAX_CELL_ANGLE_ERROR=           3.0 (Degrees)

 The REINDEXING TRANSFORMATION REIDX() consists of 12 integers that relate
 the original indices H,K,L from file INTEGRATE.HKL to the indices H',K',L'
 with respect to the new cell.
    H'=(REIDX(1)*H+REIDX( 2)*K+REIDX( 3)*L)/IDXV+REIDX( 4)
    K'=(REIDX(5)*H+REIDX( 6)*K+REIDX( 7)*L)/IDXV+REIDX( 8)
    L'=(REIDX(9)*H+REIDX(10)*K+REIDX(11)*L)/IDXV+REIDX(12)
 The value of the integer IDXV depends on the lattice type used for
 specifying reflections on file INTEGRATE.HKL; IDXV is
 1 for a primitive,
 2 for a face or body centred,
 3 for a rhombohedral,
 4 for a lattice centred on all faces.
 IDXV is set by XDS and cannot be input by the user.

  LATTICE-  BRAVAIS-   QUALITY  UNIT CELL CONSTANTS (ANGSTROEM & DEGREES)    REINDEXING TRANSFORMATION
 CHARACTER  LATTICE     OF FIT      a      b      c   alpha  beta gamma

 *  31        aP          0.0      54.3   54.3  107.4  90.0  90.0  60.0    0  1  0  0 -1  0  0  0  0  0  1  0
 *  44        aP          0.0      54.3   54.3  107.4  90.0  90.0 120.0    0 -1  0  0 -1  0  0  0  0  0 -1  0
 *  39        mC          0.2      94.1   54.3  107.4  90.0  90.0  90.0    2  1  0  0  0  1  0  0  0  0  1  0
 *  29        mC          0.3      54.3   94.1  107.4  90.0  90.0  90.0    1  0  0  0  1  2  0  0  0  0  1  0
 *  10        mC          0.3      94.1   54.4  107.4  90.0  90.0  90.0   -1  1  0  0  1  1  0  0  0  0 -1  0
 *  34        mP          0.4      54.3  107.4   54.3  90.0 120.0  90.0    0  1  0  0  0  0  1  0  1  0  0  0
 *  13        oC          0.5      54.4   94.1  107.4  90.0  90.0  90.0   -1 -1  0  0 -1  1  0  0  0  0 -1  0
 *  14        mC          0.5      54.4   94.1  107.4  90.0  90.0  90.0   -1 -1  0  0 -1  1  0  0  0  0 -1  0
 *  38        oC          0.6      54.3   94.1  107.4  90.0  90.0  90.0    0  1  0  0 -2 -1  0  0  0  0  1  0
 *  12        hP          0.6      54.3   54.3  107.4  90.0  90.0 120.0    0 -1  0  0 -1  0  0  0  0  0 -1  0
    35        mP        250.0      54.3   54.3  107.4  90.0  90.0 120.0    1  0  0  0  0  1  0  0  0  0  1  0
    33        mP        250.0      54.3   54.3  107.4  90.0  90.0 120.0    1  0  0  0  0  1  0  0  0  0  1  0
    32        oP        250.3      54.3   54.3  107.4  90.0  90.0 120.0    0 -1  0  0 -1  0  0  0  0  0 -1  0
    11        tP        250.3      54.3   54.3  107.4  90.0  90.0 120.0    0 -1  0  0 -1  0  0  0  0  0 -1  0
    28        mC        374.5      54.3  221.6   54.3  97.0 120.0  75.8    0 -1  0  0  0 -1  2  0 -1  0  0  0
    30        mC        374.5      54.3  221.6   54.3  97.0 120.0  75.8   -1  0  0  0 -1  0 -2  0  0 -1  0  0
    27        mC        499.2      94.1   54.3  120.4  77.0 113.0  90.0   -2 -1  0  0  0 -1  0  0  1  0  1  0
    41        mC        499.6     221.6   54.3   54.3 120.0  97.0  75.8    1  0  2  0  1  0  0  0  0  1  0  0
    37        mC        499.6     221.6   54.3   54.3 120.0  97.0  75.8    1  0  2  0  1  0  0  0  0  1  0  0
    40        oC        499.6      54.3  221.6   54.3  83.0 120.0 104.2    1  0  0  0 -1  0 -2  0  0  1  0  0
    36        oC        499.6      54.3  221.6   54.3  83.0 120.0 104.2    1  0  0  0 -1  0 -2  0  0  1  0  0
    26        oF        623.9      54.3   94.1  221.6  90.0 104.2  90.0    0  1  0  0 -2 -1  0  0  0 -1  2  0
     9        hR        748.9      54.3   54.4  335.7  90.0 104.1 120.0    0  1  0  0 -1 -1  0  0  1 -1  3  0
    17        mC        749.1      94.1   54.4  120.4  77.0 113.0  90.0    1 -1  0  0 -1 -1  0  0 -1  0 -1  0
    16        oF        749.5      54.4   94.1  221.6  90.0 104.2  90.0   -1 -1  0  0  1 -1  0  0  1  1  2  0
    42        oI        749.6      54.3   54.3  221.6  97.0  97.1 120.0    0  1  0  0  1  0  0  0 -1 -1 -2  0
    15        tI        749.6      54.3   54.3  221.6  83.0  82.9 120.0    0 -1  0  0 -1  0  0  0 -1 -1 -2  0
    43        mI        998.8      54.3  221.6   54.4  97.0 120.0  75.8    1  0  0  0  1  0  2  0 -1 -1  0  0
     1        cF        999.0     120.4  142.8  120.4 132.1  53.7 132.1    0  1  1  0 -2 -1 -1  0  0 -1  1  0
     2        hR        999.0      54.4  120.4  142.8 114.4  90.0 103.0    1  1  0  0 -1  0 -1  0 -1  1  1  0
     3        cP        999.0      54.3   54.3  107.4  90.0  90.0 120.0    1  0  0  0  0  1  0  0  0  0  1  0
     5        cI        999.0     120.4   54.4  120.4  77.0  46.0  77.0    0 -1 -1  0 -1 -1  0  0 -1  0 -1  0
     4        hR        999.0      94.1  120.4  120.4 134.0  90.0 113.0    1 -1  0  0 -1  0  1  0 -1 -1 -1  0
     6        tI        999.0     120.4  120.4   54.4  77.0  77.0  46.0    0  1  1  0  1  0  1  0  1  1  0  0
     7        tI        999.0     120.4   54.4  120.4  77.0  46.0  77.0    1  0  1  0  1  1  0  0  0  1  1  0
     8        oI        999.0      54.4  120.4  120.4  46.0  77.0  77.0   -1 -1  0  0 -1  0 -1  0  0 -1 -1  0
    18        tI        999.0     120.4  120.4   54.3  77.0 103.0 134.0    1  0  1  0  1  1 -1  0  0  1  0  0
    19        oI        999.0      54.3  120.4  120.4  46.0  77.0  77.0    0 -1  0  0  1  0  1  0 -1 -1  1  0
    20        mC        999.0     120.4  120.4   54.3 103.0 103.1 126.3    0 -1 -1  0  0 -1  1  0 -1  0  0  0
    21        tP        999.0      54.3  107.4   54.3  90.0 120.0  90.0   -1  0  0  0  0  0 -1  0  0 -1  0  0
    22        hP        999.0      54.3  107.4   54.3  90.0 120.0  90.0   -1  0  0  0  0  0 -1  0  0 -1  0  0
    23        oC        999.0     120.4  120.4   54.3  77.0 103.0  53.7   -1  0 -1  0  1  0 -1  0  0 -1  0  0
    24        hR        999.0     142.8  120.4   54.3  77.0  90.0  65.6    1  2  1  0  0 -1  1  0  1  0  0  0
    25        mC        999.0     120.4  120.4   54.3  77.0 103.1  53.7    0  1  1  0  0 -1  1  0  1  0  0  0

 ****** LATTICE SYMMETRY IMPLICATED BY SPACE GROUP SYMMETRY ******

BRAVAIS-            POSSIBLE SPACE-GROUPS FOR PROTEIN CRYSTALS
  TYPE                     [SPACE GROUP NUMBER,SYMBOL]
  aP      [1,P1]
  mP      [3,P2] [4,P2(1)]
 mC,mI    [5,C2]
  oP      [16,P222] [17,P222(1)] [18,P2(1)2(1)2] [19,P2(1)2(1)2(1)]
  oC      [21,C222] [20,C222(1)]
  oF      [22,F222]
  oI      [23,I222] [24,I2(1)2(1)2(1)]
  tP      [75,P4] [76,P4(1)] [77,P4(2)] [78,P4(3)] [89,P422] [90,P42(1)2]
          [91,P4(1)22] [92,P4(1)2(1)2] [93,P4(2)22] [94,P4(2)2(1)2]
          [95,P4(3)22] [96,P4(3)2(1)2]
  tI      [79,I4] [80,I4(1)] [97,I422] [98,I4(1)22]
  hP      [143,P3] [144,P3(1)] [145,P3(2)] [149,P312] [150,P321] [151,P3(1)12]
          [152,P3(1)21] [153,P3(2)12] [154,P3(2)21] [168,P6] [169,P6(1)]
          [170,P6(5)] [171,P6(2)] [172,P6(4)] [173,P6(3)] [177,P622]
          [178,P6(1)22] [179,P6(5)22] [180,P6(2)22] [181,P6(4)22] [182,P6(3)22]
  hR      [146,R3] [155,R32]
  cP      [195,P23] [198,P2(1)3] [207,P432] [208,P4(2)32] [212,P4(3)32]
          [213,P4(1)32]
  cF      [196,F23] [209,F432] [210,F4(1)32]
  cI      [197,I23] [199,I2(1)3] [211,I432] [214,I4(1)32]


 Several solutions exist for the given space group that explain the data. The
 selected solution (marked "*") correlates best with the given reference data set.
 The independent settings of the cell can be obtained by application of the
 REINDEXING TRANSFORMATION to the original indices H,K,L from file INTEGRATE.HKL

 CORRELATION = correlation factor with the reference data set
 NPAIR       = number of unique reflection pairs correlated 
 Rmeas=Rrim  = redundancy independent R-factor (intensities)
               For definition see:
               Rmeas : Diederichs & Karplus,
                       Nature Struct. Biol. 4, 269-275 (1997);
               Rrim  : Weiss & Hilgenfeld,
                       J.Appl.Cryst. 30,203-205 (1997).
 COMPARED    = number of reflections used for calculating Rmeas
 ESD         = Agreement with given unit cell geometry

 CORRELATION  NPAIR  Rmeas  COMPARED  ESD       REINDEX TRANSFORMATION

      0.00        0   18.2    3974    0.20 -1 -1  0  0  1  0  0  0  0  0  1  0
  *   0.00        0   18.2    3974    0.19  0 -1  0  0  1  1  0  0  0  0  1  0

 ************ SELECTED SPACE GROUP AND UNIT CELL FOR THIS DATA SET ************

 SPACE_GROUP_NUMBER=  152
 UNIT_CELL_CONSTANTS=    54.30    54.30   107.30  90.000  90.000 120.000
 UNIT_CELL_A-AXIS=    26.918    -0.633    47.207
 UNIT_CELL_B-AXIS=   -38.886    36.994    -8.629
 UNIT_CELL_C-AXIS=   -73.067   -67.348    40.755
 REFLECTIONS H,K,L FROM "INTEGRATE.HKL" WILL BE REINDEXED BY
 H' = (  0*H + -1*K +  0*L)/ 1 +  0
 K' = (  1*H +  1*K +  0*L)/ 1 +  0
 L' = (  0*H +  0*K +  1*L)/ 1 +  0

 *****  6 EQUIVALENT POSITIONS IN SPACE GROUP #152 *****

    If x',y',z' is an equivalent position to x,y,z, then
        x'=x*ML(1)+y*ML( 2)+z*ML( 3)+ML( 4)/12.0
        y'=x*ML(5)+y*ML( 6)+z*ML( 7)+ML( 8)/12.0
        z'=x*ML(9)+y*ML(10)+z*ML(11)+ML(12)/12.0

    #    1  2  3  4    5  6  7  8    9 10 11 12 
    1    1  0  0  0    0  1  0  0    0  0  1  0
    2    0  1  0  0    1  0  0  0    0  0 -1  0
    3    0 -1  0  0    1 -1  0  0    0  0  1  4
    4   -1  0  0  0   -1  1  0  0    0  0 -1  4
    5   -1  1  0  0   -1  0  0  0    0  0  1  8
    6    1 -1  0  0    0 -1  0  0    0  0 -1  8

 ******************************************************************************
      MEAN DISCREPANCIES BETWEEN OBSERVED AND CALCULATED SPOT LOCATIONS
 ******************************************************************************

 The discrepancies in X- and Y-coordinates of the spots are depicted in the
 two images DX-CORRECTIONS.cbf and DY-CORRECTIONS.cbf for inspection with
 the XDS-Viewer.



 ******************************************************************************
  REFINEMENT OF DIFFRACTION PARAMETERS USING ALL IMAGES
 ******************************************************************************


 REFINED PARAMETERS:  DISTANCE BEAM ORIENTATION CELL AXIS                   
 USING  113190 INDEXED SPOTS
 STANDARD DEVIATION OF SPOT    POSITION (PIXELS)     0.70
 STANDARD DEVIATION OF SPINDLE POSITION (DEGREES)    0.15
 CRYSTAL MOSAICITY (DEGREES)     0.175
 DIRECT BEAM COORDINATES (REC. ANGSTROEM)  -0.007784  0.004180  1.024269
 DETECTOR COORDINATES (PIXELS) OF DIRECT BEAM    1226.30   1255.30
 DETECTOR ORIGIN (PIXELS) AT                     1242.08   1246.83
 CRYSTAL TO DETECTOR DISTANCE (mm)       357.05
 LAB COORDINATES OF DETECTOR X-AXIS  1.000000  0.000000  0.000000
 LAB COORDINATES OF DETECTOR Y-AXIS  0.000000  1.000000  0.000000
 LAB COORDINATES OF ROTATION AXIS  0.999987 -0.000645  0.004975
 COORDINATES OF UNIT CELL A-AXIS    26.908    -0.609    47.233
 COORDINATES OF UNIT CELL B-AXIS   -38.924    36.956    -8.634
 COORDINATES OF UNIT CELL C-AXIS   -73.055   -67.426    40.749
 REC. CELL PARAMETERS   0.021240  0.021240  0.009307  90.000  90.000  60.000
 UNIT CELL PARAMETERS     54.364    54.364   107.442  90.000  90.000 120.000
 E.S.D. OF CELL PARAMETERS  4.2E-02 4.2E-02 7.5E-02 0.0E+00 0.0E+00 0.0E+00
 SPACE GROUP NUMBER    152


 THE DATA COLLECTION STATISTICS REPORTED BELOW ASSUMES:
 SPACE_GROUP_NUMBER=  152
 UNIT_CELL_CONSTANTS=    54.36    54.36   107.44  90.000  90.000 120.000


 ******************************************************************************
        MEAN INTENSITY AS FUNCTION OF SPINDLE POSITION WITHIN DATA IMAGE
 ******************************************************************************

 This statistics could serve as a diagnostic tool for detecting
 shutter problems (suggested by Kay Diederichs).
 Data are corrected for this effect if PATCH_SHUTTER_PROBLEM=TRUE in XDS.INP.
 ===> Selected : PATCH_SHUTTER_PROBLEM=FALSE

 INTERVAL = Angular interval in units of the oscillation range
            covered by a data image.
 NUMBER   = Number of reflections in each interval
 INTENSITY= Mean intensity of the reflections in each interval
 FACTOR   = Correction factor applied to intensities;
            INTENSITY(overall)/INTENSITY(interval)

   INTERVAL     NUMBER      INTENSITY      FACTOR
 -0.05  0.05     14523       1327.825       1.073
  0.05  0.15     14679       1392.045       1.024
  0.15  0.25     14633       1432.553       0.995
  0.25  0.35     14700       1463.565       0.974
  0.35  0.45     14659       1476.966       0.965
  0.45  0.55     14726       1435.941       0.993
  0.55  0.65     14791       1447.478       0.985
  0.65  0.75     14994       1438.521       0.991
  0.75  0.85     14692       1427.076       0.999
  0.85  0.95     14650       1410.114       1.011
 
 -0.05  0.95    147047       1425.360       1.000
 

 ******************************************************************************
           CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & RESOLUTION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: XDS_ASCII.HKL                                     

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED      480
 DEGREES OF FREEDOM OF CHI^2 FIT             91463.1
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      1.021
 NUMBER OF CYCLES CARRIED OUT                      4

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY.cbf           
 XMIN=     0.1 XMAX=   119.9 NXBIN=   24
 YMIN= 0.00045 YMAX= 0.49904 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     112900


 ******************************************************************************
  CORRECTION FACTORS AS FUNCTION OF X (fast) & Y(slow) IN THE DETECTOR PLANE
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: XDS_ASCII.HKL                                     

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED     2256
 DEGREES OF FREEDOM OF CHI^2 FIT             91432.8
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      1.004
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX.cbf          
 XMIN=     3.5 XMAX=  2459.5 NXBIN=   47
 YMIN=    13.2 YMAX=  2514.8 NYBIN=   48
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     112900


 ******************************************************************************
   CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & DETECTOR SURFACE POSITION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: XDS_ASCII.HKL                                     

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED      312
 DEGREES OF FREEDOM OF CHI^2 FIT             91475.0
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.994
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP.cbf          
 XMIN=     0.1 XMAX=   119.9 NXBIN=   24
 DETECTOR_SURFACE_POSITION=    1232    1264
 DETECTOR_SURFACE_POSITION=    1649    1689
 DETECTOR_SURFACE_POSITION=     814    1689
 DETECTOR_SURFACE_POSITION=     814     839
 DETECTOR_SURFACE_POSITION=    1649     839
 DETECTOR_SURFACE_POSITION=    2175    1662
 DETECTOR_SURFACE_POSITION=    1623    2226
 DETECTOR_SURFACE_POSITION=     840    2226
 DETECTOR_SURFACE_POSITION=     288    1662
 DETECTOR_SURFACE_POSITION=     288     866
 DETECTOR_SURFACE_POSITION=     840     302
 DETECTOR_SURFACE_POSITION=    1623     302
 DETECTOR_SURFACE_POSITION=    2175     866
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     112900


 ******************************************************************************
    CORRECTION PARAMETERS FOR THE STANDARD ERROR OF REFLECTION INTENSITIES
 ******************************************************************************

 The variance v0(I) of the intensity I obtained from counting statistics is
 replaced by v(I)=a*(v0(I)+b*I^2). The model parameters a, b are chosen to
 minimize the discrepancies between v(I) and the variance estimated from
 sample statistics of symmetry related reflections. This model implicates
 an asymptotic limit ISa=1/SQRT(a*b) for the highest I/Sigma(I) that the
 experimental setup can produce (Diederichs (2010) Acta Cryst D66, 733-740).

     a        b          ISa
 2.282E+00  8.450E-04   22.77


 ******************************************************************************
      STANDARD ERROR OF REFLECTION INTENSITIES AS FUNCTION OF RESOLUTION
      FOR DATA SET  XDS_ASCII.HKL                                     
 ******************************************************************************

  I/Sigma  = mean intensity/Sigma of a reflection in shell
  Chi^2    = goodness of fit between sample variances of
             symmetry-related intensities and their errors
             (Chi^2 = 1 for perfect agreement)
  R-FACTOR
  observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
  expected = expected R-FACTOR derived from Sigma(I)

   NUMBER  = number of reflections in resolution shell
             used for calculation of R-FACTOR
  ACCEPTED = number of accepted reflections
  REJECTED = number of rejected reflections (MISFITS),
             recognized by comparison with symmetry-related
             reflections.

 RESOLUTION RANGE  I/Sigma  Chi^2  R-FACTOR  R-FACTOR  NUMBER ACCEPTED REJECTED
                                   observed  expected

   47.080  13.562    21.12   1.46      3.38      3.18     256     256      18
   13.562   9.795    21.90   1.19      3.44      3.25     483     484      25
    9.795   8.056    21.88   1.17      3.07      3.15     456     458      25
    8.056   7.002    21.33   0.99      2.91      3.27     653     654      18
    7.002   6.277    20.79   1.21      3.23      3.29     771     771      27
    6.277   5.739    20.59   1.08      3.11      3.29     833     833      25
    5.739   5.319    20.52   1.22      3.13      3.30     910     910      48
    5.319   4.979    20.90   1.16      3.08      3.28     958     958      32
    4.979   4.697    21.18   1.15      2.95      3.24     950     953      52
    4.697   4.458    21.30   1.15      3.18      3.23     898     899      36
    4.458   4.253    21.03   1.12      3.08      3.27    1109    1109      52
    4.253   4.073    21.22   1.18      3.36      3.28    1193    1193      47
    4.073   3.914    21.05   1.20      3.31      3.28    1224    1224      45
    3.914   3.773    20.84   1.12      3.08      3.31    1297    1297      38
    3.773   3.646    20.36   1.20      3.09      3.33    1369    1369      54
    3.646   3.531    20.16   1.16      3.21      3.34    1453    1454      50
    3.531   3.426    20.37   1.12      3.07      3.37    1429    1429      48
    3.426   3.330    19.42   1.16      3.36      3.38    1479    1479      55
    3.330   3.241    19.42   1.16      3.24      3.38    1320    1322      47
    3.241   3.160    19.16   1.21      3.48      3.41    1414    1415      46
    3.160   3.084    19.19   1.17      3.37      3.45    1579    1579      63
    3.084   3.013    18.52   1.16      3.52      3.50    1490    1490      62
    3.013   2.947    18.09   1.16      3.54      3.57    1701    1702      65
    2.947   2.885    16.83   1.10      3.65      3.69    1754    1754      36
    2.885   2.827    16.97   1.17      3.86      3.74    1671    1671      49
    2.827   2.773    16.60   1.09      3.72      3.80    1846    1846      35
    2.773   2.721    16.33   1.16      3.99      3.82    1716    1717      47
    2.721   2.672    15.94   1.09      3.90      3.87    1964    1964      50
    2.672   2.626    15.34   1.13      4.13      3.98    1944    1944      37
    2.626   2.582    15.53   1.09      4.09      3.98    1921    1921      43
    2.582   2.540    15.86   1.08      3.90      3.94    1872    1875      40
    2.540   2.500    15.21   1.23      4.43      4.03    1735    1737      66
    2.500   2.462    14.26   1.15      4.55      4.23    1714    1718      44
    2.462   2.426    14.20   1.07      4.39      4.16    2096    2097      49
    2.426   2.391    14.17   1.12      4.55      4.25    1962    1962      47
    2.391   2.357    13.93   1.10      4.46      4.31    1948    1949      39
    2.357   2.325    12.94   1.11      4.89      4.61    2238    2238      36
    2.325   2.295    13.65   1.08      4.60      4.41    2166    2166      50
    2.295   2.265    13.14   1.09      4.85      4.57    2113    2113      39
    2.265   2.237    12.92   1.11      5.05      4.67    2182    2183      50
    2.237   2.209    12.02   1.04      4.97      4.84    2293    2293      39
    2.209   2.183    11.89   1.03      5.01      5.03    2260    2260      33
    2.183   2.157    12.20   1.01      5.02      4.96    2419    2419      28
    2.157   2.133    11.98   1.08      5.26      5.03    2342    2342      26
    2.133   2.109    11.46   1.04      5.50      5.32    2329    2331      32
    2.109   2.086    11.23   1.02      5.45      5.34    2130    2132      51
    2.086   2.064    11.14   1.08      5.65      5.38    2257    2262      54
    2.064   2.042    10.87   0.98      5.47      5.52    2115    2116      42
    2.042   2.021    10.02   0.99      6.06      5.94    2351    2355      42
    2.021   2.001     9.79   0.93      5.97      6.14    2405    2406      27
    2.001   1.981     9.57   0.91      6.23      6.36    2583    2584      28
    1.981   1.962     8.75   0.87      6.61      6.93    2386    2386      15
    1.962   1.944     8.35   0.83      6.72      7.16    2462    2462      12
    1.944   1.926     9.09   0.86      6.47      6.89    2662    2662      24
    1.926   1.908     8.14   0.92      7.50      7.59    2679    2679      19
    1.908   1.891     8.08   0.86      7.21      7.53    2528    2528      24
    1.891   1.874     7.38   0.74      7.31      8.37    2547    2547      10
    1.874   1.858     7.24   0.79      7.72      8.51    2832    2832      19
    1.858   1.842     6.99   0.76      7.72      8.76    2816    2817      12
    1.842   1.827     6.54   0.74      8.34      9.65    2650    2652       8
    1.827   1.812     6.64   0.73      8.23      9.54    2380    2382      14
    1.812   1.797     6.07   0.71      8.68     10.19    2340    2352       7
    1.797   1.783     5.85   0.74      9.16     10.44    2184    2198       6
    1.783   1.769     5.87   0.67      8.75     10.46    1982    1999      14
    1.769   1.755     5.34   0.68      9.56     11.42    1790    1813       5
    1.755   1.742     5.26   0.56      8.58     11.40    1754    1775       5
    1.742   1.729     4.83   0.62      9.73     12.43    1766    1796       5
    1.729   1.716     4.69   0.63     10.25     12.82    1481    1519       3
    1.716   1.704     4.73   0.61     10.12     12.89    1468    1498       2
    1.704   1.692     4.60   0.59     10.26     13.31    1374    1410       7
    1.692   1.680     4.13   0.56     10.89     14.66    1373    1416       1
    1.680   1.668     4.15   0.55     10.79     14.40    1320    1371       1
    1.668   1.657     3.93   0.58     11.32     14.74    1111    1163       1
    1.657   1.645     4.10   0.55     10.87     14.91    1073    1133       2
    1.645   1.634     3.92   0.59     11.64     14.94    1126    1182       1
    1.634   1.624     3.42   0.61     13.46     16.99     986    1051       1
    1.624   1.613     3.44   0.50     11.92     17.29     974    1047       0
    1.613   1.603     3.09   0.57     14.12     18.83     805     886       3
    1.603   1.592     3.39   0.53     12.70     17.26     895     961       2
    1.592   1.582     3.39   0.54     12.63     17.35     780     870       3
    1.582   1.573     3.03   0.53     13.74     19.20     751     840       0
    1.573   1.563     2.90   0.49     13.98     19.93     645     747       2
    1.563   1.554     2.72   0.57     16.01     21.53     555     673       0
    1.554   1.544     2.55   0.52     16.65     23.07     574     677       1
    1.544   1.535     2.39   0.60     19.11     24.56     498     630       2
    1.535   1.526     2.56   0.47     16.55     23.61     495     601       0
    1.526   1.518     2.38   0.53     18.61     25.76     345     464       1
    1.518   1.509     2.29   0.73     21.49     25.00     306     432       0
    1.509   1.500     2.23   0.57     18.37     24.45     326     455       0
    1.500   1.492     2.00   0.51     19.34     27.45     273     393       1
    1.492   1.484     2.36   0.63     20.42     25.40     239     356       0
    1.484   1.476     1.99   0.58     21.12     28.36     207     319       0
    1.476   1.468     2.05   0.77     23.09     25.80     161     255       0
    1.468   1.460     1.93   0.76     25.99     29.22     158     272       0
    1.460   1.452     1.91   0.48     18.84     26.28      96     174       0
    1.452   1.445     1.47   0.62     30.81     38.30      84     151       0
    1.445   1.437     1.67   0.62     38.28     48.93      36     104       2
    1.437   1.430     1.71   0.86     33.54     32.79      12      58       0
    1.430   1.423     1.55   0.00    -99.90    -99.90       0      19       2
    1.423   1.416     1.98   0.00    -99.90    -99.90       0      14       0
   --------------------------------------------------------------------------
   47.080   1.416    11.25   0.94      3.96      4.09  141836  144614    2374
 


 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR VARIOUS SUBSETS OF INCLUDED DATA IMAGES
 ******************************************************************************

 Data set statistics is reported below several times, each with a different
 upper limit on the number of images included. This provides the user with
 the information for deciding which data images should be excluded from the
 final data set because of radiation damage or other defects. If the user
 decides for a subset of "good" images that differs from the specification
 as given by the input parameter (see DATA_RANGE= in XDS.INP) the CORRECT-
 step of XDS must be repeated with the new parameter values for DATA_RANGE=.


 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1      14
 ******************************************************************************


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) of this data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     4.23         954     703      1481       47.5%       2.3%      2.6%      477   24.16     3.2%     2.4%    69%   0.924       2
     3.00        1710    1308      2507       52.2%       2.4%      2.6%      801   22.23     3.4%     2.6%     0%   0.000       0
     2.45        2311    1747      3197       54.6%       3.0%      3.0%     1116   17.70     4.2%     3.7%     0%   0.000       0
     2.12        2810    2042      3748       54.5%       3.8%      3.8%     1457   14.34     5.3%     4.8%   -33%   0.591       9
     1.90        3120    2225      4196       53.0%       4.7%      5.1%     1652   10.81     6.4%     6.5%   -41%   0.704       8
     1.73        2967    2146      4614       46.5%       6.7%      7.7%     1475    7.28     8.9%     9.9%   -30%   0.596      13
     1.60        1620    1408      4993       28.2%       9.2%     12.1%      385    4.32    12.3%    12.9%     4%   0.900       4
     1.50         861     849      5386       15.8%      13.0%     19.7%       24    2.83    18.4%    28.6%     0%   0.000       0
     1.42         260     260      5680        4.6%     -99.9%    -99.9%        0  -99.00   -99.9%   -99.9%     0%   0.000       0
    total       16613   12688     35802       35.4%       3.0%      3.2%     7387   12.21     4.1%     4.5%   -13%   0.671      36


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES   17068
 NUMBER OF REJECTED MISFITS                             455
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                  0
 NUMBER OF ACCEPTED OBSERVATIONS                      16613
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                12688



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1      27
 ******************************************************************************


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) of this data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     4.23        1851     954      1481       64.4%       2.4%      2.8%     1487   28.56     3.1%     2.1%   -22%   0.714      39
     3.00        3392    1717      2507       68.5%       2.5%      2.8%     2823   27.09     3.3%     2.5%   -31%   0.570      34
     2.45        4489    2288      3197       71.6%       3.4%      3.3%     3772   21.37     4.5%     3.6%   -32%   0.579      46
     2.12        5457    2776      3748       74.1%       4.1%      4.0%     4557   17.21     5.4%     4.7%   -32%   0.635      94
     1.90        6021    3159      4196       75.3%       5.2%      5.4%     4809   12.57     6.7%     6.5%   -16%   0.722     148
     1.73        5746    3212      4614       69.6%       7.3%      8.0%     4299    8.28     9.6%     9.4%    -5%   0.660     129
     1.60        3164    2432      4993       48.7%       9.0%     12.2%     1386    4.63    12.4%    14.0%   -25%   0.642       8
     1.50        1670    1550      5386       28.8%      13.5%     20.3%      240    2.89    19.2%    26.2%     0%   0.000       0
     1.42         501     485      5680        8.5%      14.3%     25.0%       32    2.02    20.2%    25.5%     0%   0.000       0
    total       32291   18573     35802       51.9%       3.2%      3.4%    23405   13.65     4.1%     4.5%   -18%   0.664     498


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES   33053
 NUMBER OF REJECTED MISFITS                             762
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                  0
 NUMBER OF ACCEPTED OBSERVATIONS                      32291
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                18573



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1      41
 ******************************************************************************


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) of this data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     4.23        2824    1039      1481       70.2%       2.7%      3.0%     2549   33.35     3.2%     1.9%    -3%   0.808     214
     3.00        5213    1862      2507       74.3%       2.9%      3.1%     4807   31.95     3.4%     2.3%   -15%   0.754     323
     2.45        6849    2445      3197       76.5%       3.7%      3.5%     6373   25.49     4.5%     3.2%    -9%   0.806     354
     2.12        8302    2952      3748       78.8%       4.5%      4.3%     7799   20.59     5.4%     4.2%    -7%   0.813     407
     1.90        9144    3391      4196       80.8%       5.7%      5.7%     8507   15.00     6.9%     5.9%   -11%   0.734     440
     1.73        8753    3628      4614       78.6%       7.6%      8.5%     7815    9.57     9.3%     8.7%    -4%   0.654     331
     1.60        4823    3073      4993       61.5%       9.0%     12.2%     3143    5.13    12.1%    14.2%   -11%   0.580      26
     1.50        2547    2155      5386       40.0%      11.5%     17.4%      784    3.00    16.3%    21.3%     0%   0.000       0
     1.42         742     713      5680       12.6%      13.2%     26.0%       58    2.12    18.7%    23.4%     0%   0.000       0
    total       49197   21258     35802       59.4%       3.5%      3.7%    41835   15.36     4.3%     4.5%    -8%   0.758    2095


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES   50295
 NUMBER OF REJECTED MISFITS                            1098
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                  0
 NUMBER OF ACCEPTED OBSERVATIONS                      49197
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                21258



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1      54
 ******************************************************************************


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) of this data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     4.23        3750    1121      1481       75.7%       2.9%      3.1%     3519   36.87     3.3%     1.9%    -8%   0.795     420
     3.00        6900    2037      2507       81.3%       3.1%      3.2%     6491   34.93     3.5%     2.2%   -11%   0.770     781
     2.45        9055    2646      3197       82.8%       3.9%      3.7%     8592   28.11     4.5%     3.0%    -7%   0.812    1042
     2.12       10967    3160      3748       84.3%       4.7%      4.4%    10536   22.99     5.5%     3.9%    -2%   0.844    1293
     1.90       12040    3597      4196       85.7%       5.9%      5.9%    11557   16.78     6.9%     5.4%    -4%   0.752    1320
     1.73       11532    3914      4614       84.8%       7.7%      8.7%    10777   10.64     9.1%     8.0%     0%   0.680    1068
     1.60        6379    3447      4993       69.0%       9.5%     12.7%     4847    5.51    12.2%    13.9%    -4%   0.620     202
     1.50        3376    2548      5386       47.3%      12.3%     17.6%     1562    3.18    16.9%    20.6%     0%   0.000       0
     1.42         982     903      5680       15.9%      15.0%     25.6%      153    2.12    20.9%    32.7%     0%   0.000       0
    total       64981   23373     35802       65.3%       3.7%      3.8%    58034   16.71     4.4%     4.4%    -4%   0.770    6127


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES   66312
 NUMBER OF REJECTED MISFITS                            1331
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                  0
 NUMBER OF ACCEPTED OBSERVATIONS                      64981
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                23373



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1      67
 ******************************************************************************


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) of this data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     4.23        4680    1248      1481       84.3%       3.0%      3.1%     4506   39.21     3.4%     1.8%   -11%   0.777     553
     3.00        8609    2231      2507       89.0%       3.1%      3.2%     8311   37.49     3.6%     2.1%   -17%   0.753    1111
     2.45       11266    2882      3197       90.1%       3.9%      3.7%    10952   30.18     4.5%     2.8%    -8%   0.823    1538
     2.12       13644    3465      3748       92.4%       4.7%      4.5%    13289   24.55     5.4%     3.6%    -6%   0.809    1892
     1.90       14917    3932      4196       93.7%       6.0%      6.0%    14515   17.96     6.9%     5.0%    -2%   0.759    2009
     1.73       14324    4250      4614       92.1%       7.8%      8.8%    13756   11.33     9.1%     7.8%    -3%   0.681    1780
     1.60        7885    3728      4993       74.7%       9.8%     13.0%     6618    5.83    12.4%    13.5%     1%   0.610     343
     1.50        4207    2790      5386       51.8%      13.0%     17.9%     2559    3.36    17.6%    21.4%    27%   0.606       4
     1.42        1207    1025      5680       18.0%      17.1%     25.1%      354    2.16    23.9%    33.5%     0%   0.000       0
    total       80739   25551     35802       71.4%       3.8%      3.9%    74860   17.87     4.4%     4.3%    -6%   0.760    9230


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES   82277
 NUMBER OF REJECTED MISFITS                            1538
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                  0
 NUMBER OF ACCEPTED OBSERVATIONS                      80739
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                25551



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1      80
 ******************************************************************************


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) of this data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     4.23        5613    1360      1481       91.8%       3.0%      3.2%     5512   41.42     3.4%     1.8%    -7%   0.791     710
     3.00       10316    2377      2507       94.8%       3.1%      3.2%    10177   40.13     3.6%     2.0%   -16%   0.750    1413
     2.45       13468    3081      3197       96.4%       3.9%      3.7%    13243   32.24     4.4%     2.7%    -6%   0.819    1845
     2.12       16290    3651      3748       97.4%       4.8%      4.5%    16077   26.38     5.4%     3.4%    -1%   0.832    2333
     1.90       17817    4112      4196       98.0%       6.0%      6.0%    17556   19.41     6.8%     4.8%    -2%   0.759    2512
     1.73       17100    4443      4614       96.3%       7.9%      9.0%    16725   12.14     9.0%     7.4%    -3%   0.679    2304
     1.60        9419    3957      4993       79.3%      10.0%     13.2%     8331    6.18    12.4%    13.9%    -3%   0.601     633
     1.50        5014    3019      5386       56.1%      13.5%     18.2%     3460    3.53    17.9%    22.1%   -16%   0.555     103
     1.42        1447    1165      5680       20.5%      18.3%     25.4%      530    2.20    25.2%    33.4%   -41%   0.420       9
    total       96484   27165     35802       75.9%       3.8%      3.9%    91611   19.10     4.4%     4.2%    -5%   0.758   11862


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES   98221
 NUMBER OF REJECTED MISFITS                            1737
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                  0
 NUMBER OF ACCEPTED OBSERVATIONS                      96484
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                27165



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1      94
 ******************************************************************************


 AVERAGE INTENSITY FOR      19 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS    -0.1% OF MEAN INTENSITY


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) of this data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     4.23        6609    1447      1481       97.7%       3.0%      3.2%     6539   43.67     3.4%     1.8%    -8%   0.788     846
     3.00       12163    2484      2507       99.1%       3.2%      3.3%    12075   42.87     3.6%     1.9%   -16%   0.738    1736
     2.45       15859    3188      3197       99.7%       3.9%      3.8%    15751   34.73     4.3%     2.4%    -7%   0.806    2286
     2.12       19139    3730      3748       99.5%       4.8%      4.5%    19035   28.60     5.3%     3.2%    -4%   0.813    2821
     1.90       20920    4181      4196       99.6%       6.1%      6.1%    20788   21.14     6.8%     4.4%     0%   0.771    3047
     1.73       20073    4486      4614       97.2%       8.0%      9.1%    19828   13.26     9.0%     7.1%    -3%   0.673    2859
     1.60       11087    4003      4993       80.2%      10.3%     13.6%    10293    6.69    12.5%    13.2%    -4%   0.601    1083
     1.50        5895    3128      5386       58.1%      14.3%     19.2%     4578    3.75    18.5%    22.1%   -16%   0.536     247
     1.42        1692    1246      5680       21.9%      20.6%     26.5%      815    2.28    28.0%    33.7%   -54%   0.391      17
    total      113437   27893     35802       77.9%       3.9%      4.0%   109702   20.66     4.3%     4.1%    -5%   0.746   14942


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES  115371
 NUMBER OF REJECTED MISFITS                            1915
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                 19
 NUMBER OF ACCEPTED OBSERVATIONS                     113437
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                27893



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1     107
 ******************************************************************************


 AVERAGE INTENSITY FOR      41 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     0.5% OF MEAN INTENSITY


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) of this data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     4.23        7520    1476      1481       99.7%       3.0%      3.2%     7481   46.18     3.4%     1.7%    -6%   0.806     948
     3.00       13872    2501      2507       99.8%       3.2%      3.3%    13845   45.82     3.6%     1.8%   -13%   0.755    1929
     2.45       18086    3192      3197       99.8%       3.9%      3.8%    18059   37.35     4.3%     2.3%    -8%   0.802    2560
     2.12       21814    3743      3748       99.9%       4.8%      4.6%    21797   30.66     5.3%     3.0%    -5%   0.802    3138
     1.90       23829    4188      4196       99.8%       6.1%      6.2%    23799   22.69     6.7%     4.2%     0%   0.766    3458
     1.73       22854    4494      4614       97.4%       8.1%      9.3%    22711   14.15     9.0%     6.7%    -3%   0.675    3307
     1.60       12629    4017      4993       80.5%      10.7%     14.0%    12015    7.14    12.6%    13.1%    -5%   0.594    1436
     1.50        6706    3193      5386       59.3%      14.7%     19.8%     5549    3.95    18.5%    21.2%   -14%   0.540     352
     1.42        1926    1333      5680       23.5%      22.0%     27.4%     1057    2.33    29.5%    35.2%   -60%   0.390      21
    total      129236   28137     35802       78.6%       3.9%      4.0%   126313   22.03     4.3%     4.0%    -5%   0.742   17149


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES  131402
 NUMBER OF REJECTED MISFITS                            2125
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                 41
 NUMBER OF ACCEPTED OBSERVATIONS                     129236
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                28137



 ******************************************************************************
  STATISTICS OF SAVED DATA SET "XDS_ASCII.HKL" (DATA_RANGE=       1     120)
 FILE TYPE:         XDS_ASCII      MERGE=FALSE          FRIEDEL'S_LAW=TRUE 
 ******************************************************************************

   REFLECTIONS OF TYPE H,0,0  0,K,0  0,0,L OR EXPECTED TO BE ABSENT (*)
   --------------------------------------------------------------------

   H    K    L  RESOLUTION  INTENSITY     SIGMA    INTENSITY/SIGMA  #OBSERVED

    0    0    4    26.860   0.4071E+01  0.1181E+01         3.45           2*
    0    0    5    21.488   0.8742E+01  0.1485E+01         5.89           2*
    0    0    6    17.907   0.8009E+04  0.2497E+03        32.07           2 
    0    0    7    15.349   0.2481E+01  0.1941E+01         1.28           2*
    0    0    8    13.430   0.5693E+01  0.2193E+01         2.60           2*
    0    0    9    11.938   0.6227E+03  0.2085E+02        29.87           2 
    0    0   10    10.744   0.1186E+02  0.3016E+01         3.93           2*
    0    0   11     9.767   0.4049E+02  0.4112E+01         9.85           2*
    0    0   12     8.953   0.2928E+05  0.9112E+03        32.13           2 
    0    0   13     8.265   0.8087E+01  0.3547E+01         2.28           2*
    0    0   14     7.674   0.1263E+02  0.5166E+01         2.45           1*
    0    0   15     7.163   0.1272E+04  0.5922E+02        21.48           1 
    0    0   16     6.715   0.2554E+01  0.5639E+01         0.45           1*
    0    0   17     6.320   0.1184E+02  0.4600E+01         2.57           2*
    0    0   18     5.969   0.1739E+04  0.5707E+02        30.47           2 
    0    0   19     5.655   0.7242E+01  0.5255E+01         1.38           2*
    0    0   20     5.372   0.2294E+00  0.5052E+01         0.05           2*
    0    0   21     5.116   0.2779E+04  0.8972E+02        30.98           2 
    0    0   22     4.884   0.2679E+02  0.6470E+01         4.14           2*
    0    0   23     4.671   0.9567E+01  0.6138E+01         1.56           2*
    0    0   24     4.477   0.2176E+05  0.6791E+03        32.04           2 
    0    0   25     4.298   0.1539E+02  0.1016E+02         1.51           2*
    0    0   26     4.132   0.4094E+02  0.1102E+02         3.72           2*
    0    0   27     3.979   0.5240E+05  0.1631E+04        32.12           2 
    0    0   28     3.837   0.6999E+01  0.1030E+02         0.68           2*
    0    0   29     3.705   0.2633E+02  0.1564E+02         1.68           1*
    0    0   30     3.581   0.1246E+03  0.1497E+02         8.32           1 
    0    0   32     3.358  -0.1235E+02  0.1773E+02        -0.70           1*
    0    0   33     3.256   0.3139E+04  0.1457E+03        21.54           1 
    0    0   34     3.160   0.5825E+01  0.1591E+02         0.37           1*
    0    0   35     3.070   0.6462E+01  0.1785E+02         0.36           1*
    0    0   36     2.984   0.1174E+05  0.5229E+03        22.44           1 
    0    0   37     2.904  -0.2352E+01  0.1577E+02        -0.15           1*
    0    0   38     2.827   0.1575E+02  0.1846E+02         0.85           1*
    0    0   39     2.755   0.1177E+04  0.6255E+02        18.82           1 
    0    0   40     2.686   0.1872E+02  0.1735E+02         1.08           1*
    0    0   41     2.621  -0.1096E+02  0.1686E+02        -0.65           1*
    0    0   42     2.558   0.1757E+04  0.8726E+02        20.13           1 
    0    0   43     2.499  -0.1463E+02  0.1753E+02        -0.83           1*
    0    0   45     2.388   0.2975E+03  0.2714E+02        10.96           1 
    0    0   46     2.336   0.1612E+02  0.2075E+02         0.78           1*
    0    0   47     2.286   0.2789E+02  0.2151E+02         1.30           1*
    0    0   48     2.238   0.5187E+04  0.2382E+03        21.78           1 
    0    0   49     2.193  -0.2620E+02  0.2022E+02        -1.30           1*
    0    0   50     2.149   0.2486E+01  0.1735E+02         0.14           1*
    0    0   52     2.066   0.1574E+02  0.2093E+02         0.75           1*
    0    0   53     2.027   0.1099E+02  0.1830E+02         0.60           1*
    0    0   54     1.990   0.5296E+02  0.2145E+02         2.47           1 
    0    0   55     1.953   0.9938E+01  0.1975E+02         0.50           1*
    0    0   56     1.919  -0.4456E+02  0.2056E+02        -2.17           1*
    0    0   58     1.852   0.1020E+02  0.1766E+02         0.58           1*
    0    0   59     1.821   0.3497E+01  0.1981E+02         0.18           1*
    0    0   60     1.791   0.2912E+02  0.1981E+02         1.47           1 
    0    0   61     1.761   0.3351E+01  0.1738E+02         0.19           1*
    0    0   62     1.733  -0.1330E+02  0.2053E+02        -0.65           1*
    0    0   63     1.705   0.6850E+03  0.4619E+02        14.83           1 
    0    0   64     1.679  -0.1313E+02  0.2004E+02        -0.66           1*
    0    0   65     1.653  -0.9644E+01  0.2156E+02        -0.45           1*
    0    0   66     1.628   0.1385E+02  0.2233E+02         0.62           1 
    0    0   67     1.604  -0.1080E+02  0.2344E+02        -0.46           1*
    0    0   69     1.557   0.6164E+02  0.2686E+02         2.29           1 
    0    0   70     1.535  -0.1159E+01  0.2623E+02        -0.04           1*
    0    0   71     1.513   0.2190E+02  0.2589E+02         0.85           1*
    0    0   72     1.492   0.3814E+02  0.3034E+02         1.26           1 
    0    0   73     1.472  -0.7128E+01  0.2628E+02        -0.27           1*
    1    0    0    47.080   0.4463E+04  0.9851E+02        45.31           4 
    2    0    0    23.540   0.1692E+03  0.4446E+01        38.05           4 
    3    0    0    15.693   0.1135E+03  0.3655E+01        31.06           4 
    4    0    0    11.770   0.5821E+04  0.1292E+03        45.06           4 
    5    0    0     9.416   0.4426E+03  0.1589E+02        27.86           2 
    6    0    0     7.847   0.2871E+04  0.9186E+02        31.26           2 
    7    0    0     6.726   0.1893E+04  0.4386E+02        43.16           4 
    8    0    0     5.885   0.1348E+02  0.4046E+01         3.33           4 
    9    0    0     5.231   0.4094E+04  0.9303E+02        44.01           4 
   10    0    0     4.708   0.4525E+04  0.1453E+03        31.14           2 
   11    0    0     4.280   0.5340E+03  0.2003E+02        26.66           3 
   12    0    0     3.923   0.1572E+03  0.1715E+02         9.17           2 
   13    0    0     3.622   0.1592E+05  0.3542E+03        44.94           4 
   14    0    0     3.363   0.4602E+04  0.1063E+03        43.32           4 
   15    0    0     3.139   0.3922E+04  0.9156E+02        42.84           4 
   16    0    0     2.943   0.1239E+04  0.3442E+02        36.00           4 
   17    0    0     2.769   0.7319E+04  0.1917E+03        38.18           3 
   18    0    0     2.616   0.6055E+02  0.1027E+02         5.90           4 
   19    0    0     2.478   0.6042E+02  0.1065E+02         5.67           4 
   20    0    0     2.354   0.2290E+03  0.1598E+02        14.33           3 
   21    0    0     2.242   0.2298E+03  0.1532E+02        15.00           4 
   22    0    0     2.140   0.4156E+03  0.2186E+02        19.01           3 
   23    0    0     2.047   0.3043E+01  0.1117E+02         0.27           4 
   24    0    0     1.962   0.2306E+03  0.1531E+02        15.06           4 
   25    0    0     1.883   0.1694E+03  0.1301E+02        13.03           4 
   26    0    0     1.811   0.9912E+02  0.1986E+02         4.99           2 
   27    0    0     1.744   0.1575E+03  0.1903E+02         8.28           2 
   28    0    0     1.681   0.1027E+03  0.1341E+02         7.66           3 
   29    0    0     1.623   0.1306E+02  0.1120E+02         1.17           3 
   30    0    0     1.569   0.7327E+02  0.1895E+02         3.87           2 

 AVERAGE INTENSITY FOR      59 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     0.7% OF MEAN INTENSITY


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) of this data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     4.23        8403    1476      1481       99.7%       3.1%      3.3%     8395   48.96     3.4%     1.7%    -3%   0.825     994
     3.00       15495    2502      2507       99.8%       3.3%      3.4%    15491   48.52     3.6%     1.7%   -13%   0.759    1987
     2.45       20249    3193      3197       99.9%       3.9%      3.9%    20238   39.59     4.3%     2.2%    -8%   0.792    2670
     2.12       24408    3745      3748       99.9%       4.8%      4.6%    24405   32.50     5.3%     2.8%    -5%   0.807    3252
     1.90       26675    4188      4196       99.8%       6.1%      6.2%    26659   24.07     6.7%     3.9%    -1%   0.765    3629
     1.73       25620    4494      4614       97.4%       8.2%      9.5%    25507   14.97     9.0%     6.3%    -2%   0.669    3594
     1.60       14088    4081      4993       81.7%      10.9%     14.4%    13514    7.43    12.7%    12.1%    -6%   0.598    1709
     1.50        7524    3375      5386       62.7%      15.1%     20.5%     6336    4.00    18.7%    21.4%   -11%   0.574     499
     1.42        2152    1430      5680       25.2%      21.9%     27.7%     1291    2.36    29.3%    36.1%   -48%   0.428      30
    total      144614   28484     35802       79.6%       4.0%      4.1%   141836   23.07     4.3%     3.9%    -5%   0.739   18364


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES  147047
 NUMBER OF REJECTED MISFITS                            2374
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                 59
 NUMBER OF ACCEPTED OBSERVATIONS                     144614
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                28484



 ******************************************************************************
    WILSON STATISTICS OF DATA SET  "XDS_ASCII.HKL"
 ******************************************************************************

 Data is divided into resolution shells and a straight line 
 A - 2*B*SS is fitted to log<I>, where
   RES    = mean resolution (Angstrom) in shell
   SS     = mean of (sin(THETA)/LAMBDA)**2 in shell
   <I>    = mean reflection intensity in shell
   BO     = (A - log<I>)/(2*SS)
    #     = number of reflections in resolution shell

   WILSON LINE (using all data) : A=   8.957 B=  22.334 CORRELATION=  0.99
      #      RES      SS        <I>       log(<I>)       BO
     519     8.008   0.004  3.9334E+03       8.277      87.2
     850     4.973   0.010  5.2767E+03       8.571      19.1
    1066     3.880   0.017  6.4562E+03       8.773       5.6
    1261     3.286   0.023  3.9150E+03       8.273      14.8
    1387     2.901   0.030  2.0369E+03       7.619      22.5
    1547     2.627   0.036  1.3720E+03       7.224      23.9
    1665     2.416   0.043  1.0602E+03       6.966      23.3
    1779     2.251   0.049  8.6610E+02       6.764      22.2
    1901     2.114   0.056  6.6980E+02       6.507      21.9
    1973     2.000   0.062  4.5916E+02       6.129      22.6
    2089     1.903   0.069  3.3005E+02       5.799      22.9
    2165     1.819   0.076  2.1798E+02       5.384      23.6
    2081     1.745   0.082  1.6254E+02       5.091      23.5
    1942     1.679   0.089  1.2669E+02       4.842      23.2
    1864     1.621   0.095  1.0464E+02       4.650      22.6
    1697     1.568   0.102  8.1390E+01       4.399      22.4
    1400     1.520   0.108  6.4536E+01       4.167      22.1
     990     1.477   0.115  5.6200E+01       4.029      21.5
     308     1.442   0.120  4.2891E+01       3.759      21.6


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF  CENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         3<I>**2     15<I>**3    105<I>**4 

     196     8.008        0.693        0.521        0.362
     198     4.973        0.765        0.477        0.248
     206     3.880        1.318        1.725        2.272
     209     3.286        0.596        0.400        0.259
     197     2.901        0.968        0.904        0.766
     207     2.627        0.643        0.502        0.362
     209     2.416        1.070        0.941        0.697
     202     2.251        0.870        0.614        0.360
     201     2.114        1.019        1.018        0.913
     206     2.000        0.692        0.562        0.424
     209     1.903        0.903        0.764        0.595
     192     1.819        0.560        0.378        0.236
     166     1.745        0.773        0.596        0.401
     149     1.679        0.534        0.393        0.301
     136     1.621        0.782        0.709        0.599
     117     1.568        0.674        0.467        0.297
      98     1.520        0.529        0.287        0.132
      69     1.477        0.975        0.733        0.455
      21     1.442        0.466        0.200        0.071
    3188   overall        0.807        0.685        0.565


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF ACENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         2<I>**2      6<I>**3     24<I>**4 

     323     8.008        1.142        1.190        1.171
     652     4.973        1.064        1.128        1.138
     860     3.880        0.897        0.820        0.730
    1052     3.286        1.070        1.216        1.643
    1190     2.901        0.999        1.023        1.070
    1340     2.627        1.038        1.064        1.094
    1456     2.416        1.003        1.051        1.108
    1577     2.251        0.985        0.969        0.969
    1700     2.114        0.956        0.898        0.826
    1767     2.000        1.043        1.059        1.025
    1880     1.903        0.988        0.961        0.893
    1973     1.819        1.047        1.097        1.124
    1915     1.745        1.024        1.061        1.096
    1793     1.679        1.003        0.958        0.882
    1728     1.621        1.078        1.196        1.357
    1580     1.568        1.001        0.962        0.895
    1302     1.520        1.041        1.103        1.278
     921     1.477        0.995        0.963        0.914
     287     1.442        1.180        1.367        1.558
   25296   overall        1.018        1.037        1.062

   ======= CUMULATIVE INTENSITY DISTRIBUTION =======
 DEFINITIONS:
   <I>    = mean reflection intensity
 Na(Z)exp = expected number of acentric reflections with I <= Z*<I>
 Na(Z)obs = observed number of acentric reflections with I <= Z*<I>
 Nc(Z)exp = expected number of  centric reflections with I <= Z*<I>
 Nc(Z)obs = observed number of  centric reflections with I <= Z*<I>



 Nc(Z)obs/Nc(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

     196     8.008  0.76  0.94  1.08  1.07  1.08  1.11  1.09  1.07  1.05  1.03
     198     4.973  0.98  0.96  1.01  0.97  0.91  0.94  0.95  0.96  0.97  0.98
     206     3.880  1.00  1.02  0.98  0.98  0.92  0.93  0.91  0.91  0.90  0.91
     209     3.286  0.81  0.95  1.01  0.99  1.03  1.01  1.01  0.99  1.02  1.02
     197     2.901  1.04  1.01  1.02  1.01  1.05  1.00  1.00  1.00  1.01  1.00
     207     2.627  0.89  0.87  0.86  0.98  0.98  1.05  1.06  1.06  1.05  1.06
     209     2.416  0.87  0.94  0.99  1.02  1.01  0.98  0.98  0.98  0.98  0.98
     202     2.251  0.86  0.99  0.96  0.97  0.95  0.93  1.00  0.99  0.98  0.98
     201     2.114  0.84  0.91  0.92  0.93  0.94  1.01  1.06  1.05  1.05  1.04
     206     2.000  0.84  1.02  1.00  1.06  1.07  1.06  1.03  1.02  1.01  1.01
     209     1.903  0.79  0.86  0.87  0.90  0.95  1.01  1.00  1.02  1.01  1.02
     192     1.819  0.86  0.98  1.03  1.07  1.09  1.13  1.10  1.13  1.11  1.08
     166     1.745  0.73  0.94  0.88  0.92  0.95  0.99  1.04  1.03  1.02  1.06
     149     1.679  1.03  1.05  1.02  1.08  1.06  1.04  1.01  1.05  1.07  1.09
     136     1.621  0.98  1.17  1.15  1.15  1.10  1.09  1.07  1.10  1.10  1.09
     117     1.568  0.76  0.89  0.82  0.90  0.92  0.91  0.97  0.97  0.96  0.99
      98     1.520  0.95  1.03  1.05  0.99  1.00  0.98  1.01  1.02  1.01  1.02
      69     1.477  0.99  0.88  0.94  0.92  0.97  1.01  1.00  0.95  0.95  0.98
      21     1.442  0.96  0.96  0.80  0.81  0.91  0.93  0.96  0.98  1.01  0.98
    3188   overall  0.88  0.97  0.98  0.99  1.00  1.01  1.02  1.02  1.02  1.02


 Na(Z)obs/Na(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

     323     8.008  0.81  0.91  0.87  0.87  0.85  0.90  0.89  0.91  0.94  0.95
     652     4.973  0.98  0.99  0.97  1.06  1.08  1.07  1.05  1.04  1.03  1.02
     860     3.880  0.78  0.85  0.94  0.97  0.98  0.98  0.97  1.00  1.01  1.02
    1052     3.286  0.73  0.94  0.93  0.94  0.99  0.99  1.00  0.96  0.98  0.99
    1190     2.901  0.84  0.87  0.86  0.94  0.95  0.98  1.02  1.03  1.02  1.02
    1340     2.627  0.72  0.88  0.93  0.96  0.94  0.96  0.99  0.99  0.99  1.00
    1456     2.416  0.83  0.90  0.99  1.01  1.00  1.00  1.02  1.03  1.02  1.01
    1577     2.251  0.95  0.98  1.00  1.00  1.02  1.02  0.99  1.00  0.99  0.99
    1700     2.114  0.83  0.90  0.91  0.92  0.95  0.98  0.99  0.99  0.99  0.98
    1767     2.000  0.92  0.92  0.93  0.98  0.99  1.00  1.01  1.02  1.01  1.01
    1880     1.903  0.84  0.92  0.95  0.98  0.97  0.99  0.99  1.00  1.00  1.00
    1973     1.819  0.68  0.79  0.89  0.92  0.97  0.99  0.99  1.00  1.00  1.00
    1915     1.745  0.93  0.93  0.96  0.98  1.00  1.01  0.99  1.00  1.00  1.00
    1793     1.679  0.87  0.90  0.92  0.93  0.99  0.98  0.98  0.97  0.98  0.97
    1728     1.621  0.96  0.96  0.96  0.97  0.98  1.00  1.00  1.01  1.02  1.02
    1580     1.568  1.08  0.91  0.95  0.97  0.97  1.00  0.97  0.98  0.99  0.99
    1302     1.520  1.11  0.92  0.90  0.90  0.94  0.95  0.97  0.96  0.97  0.97
     921     1.477  1.24  0.95  0.90  0.93  0.90  0.94  0.94  0.95  0.97  0.98
     287     1.442  1.94  1.23  1.08  0.93  0.95  1.00  0.96  0.99  0.97  0.96
   25296   overall  0.90  0.91  0.94  0.96  0.97  0.99  0.99  0.99  1.00  1.00


 List of      1 reflections *NOT* obeying Wilson distribution (Z> 10.0)

   h    k    l     RES      Z     Intensity    Sigma

   10   -3  -23    3.50   11.63  0.4554E+05  0.7098E+03 "alien"


 List of      1 reflections *NOT* obeying Wilson distribution (sorted by resolution)
 Ice rings could occur at (Angstrom):
 3.897,3.669,3.441, 2.671,2.249,2.072, 1.948,1.918,1.883,1.721

   h    k    l     RES      Z     Intensity    Sigma

   10   -3  -23    3.50   11.63  0.4554E+05  0.7098E+03

 NUMBER OF UNIQUE ALIEN REFLECTIONS WITH A Z-SCORE ABOVE LIMIT         0
 (ALIENS ABOVE LIMIT (REJECT_ALIEN=      20.0) ARE MARKED INVALID)

 NUMBER OF REFLECTION RECORDS ON OUTPUT FILE "XDS_ASCII.HKL"      147047
 NUMBER OF ACCEPTED OBSERVATIONS (INCLUDING SYSTEMATIC ABSENCES)  144673
 NUMBER OF REJECTED MISFITS & ALIENS (marked by -1*SIGMA(IOBS))     2374


 cpu time used                 24.7 sec
 elapsed wall-clock time        5.6 sec
