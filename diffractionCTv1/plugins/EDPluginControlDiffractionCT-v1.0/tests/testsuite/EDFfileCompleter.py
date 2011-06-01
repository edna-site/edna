#!/usr/bin/env python
#
#This file is part of the EDNA project, it has been written by Jerome Kieffer 2009-10-08 and is released under the GPL license 
#

# Use the EDF image header reader plugin for localising the EdfFile module
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("EDPluginEDFReadHeaderv1_0")

import EdfFile as EDF
from CIFfile import CIF
import sys, os

#data from: http://wikiserv.esrf.fr/soft_group/index.php/Email_from_Alexander_Rack_20090722:_Sample_Data_Set_for_diffractionCT 
#in raw_diffraction_data_darkfields_EDFs and to do the azimuthal integration, in the moment
#performed via fit2d, the corresponding values used from the calibration are
#INFO: Refined Beam centre =      956.389     913.277 (pixels)
#INFO: Refined Beam centre =       45.165      42.770 (mm)
#INFO: Refined sample to detector distance =       80.637 mm
#INFO: Refined wavelength =      0.70848 Angstroms
#      Energy (keV) =     17.50014
#INFO: Refined tilt plane rotation angle =       86.421 degrees
#INFO: Refined tilt angle =       -0.750 degrees
#INFO: ROT X =       -0.047   ROT Y =       -0.749 degrees
#INFO: Stability indicator (proportional to D-spacing; Angstroms) =    0.82106

default_data = {"_diffrn_radiation_wavelength":           "0.70848",
              "_pd_instr_dist_spec/detc":               "80.637",
              "_diffrn_detector_element.center[1]":     "45.165",
              "_diffrn_detector_element.center[2]":     "42.770",
              "_pd_instr_special_details_tilt_angle":   "86.421",
              "_pd_instr_special_details_tilt_rotation":"-0.75",
# Those are optional keywords
#              "_pd_meas_2theta_range_min":              "0.0",
#              "_pd_meas_2theta_range_max":              "90.0",
#              "_pd_meas_2theta_range_inc":              "1.0"
              "_array_element_size[1]":                 "4.722e-5",
              "_array_element_size[2]":                 "4.683e-5",
              "_file_correction_image_dark-current" :   "DarkCurrent.edf",
              "_file_correction_image_flat-field":      "FlatField.edf",
              "_file_correction_spline_spatial-distortion": "spline.file",
              "_file_correction_image-mask":            "mask.edf",
              "_synchrotron_ring-intensity":            "100.1",
              "_synchrotron_photon-flux":               "1.0e10",
              "_tomo_scan_type Type of scan":           "Spiral",
              "_tomo_spec_displ_x":                     "1.0",
              "_tomo_spec_displ_x_min":                 "-10.0",
              "_tomo_spec_displ_x_max":                 "10.0",
              "_tomo_spec_displ_x_inc":                 "1.0",
              "_tomo_spec_displ_z":                     "0.0",
              "_tomo_spec_displ_z_min":                 "-10.0",
              "_tomo_spec_displ_z_max":                 "-10.0",
              "_tomo_spec_displ_z_inc":                 "1.0",
              "_tomo_spec_displ_rotation":                    "15.0" ,
              "_tomo_spec_displ_rotation_inc":                "3.0",
              "_tomo_scan_ampl":                        "180.0",


              "loop_": [   #List of all loops of the data-set
              [  #One loop is a 2-list, 
                 # in the first element is the list of all keywords with their order (important)
               [ "_pd_sum_2theta_range_min", "_pd_sum_2theta_range_max" ],
                 # The second element is a list of dictionaries
               [ { "_pd_sum_2theta_range_min": "10.0",
                   "_pd_sum_2theta_range_max": "15.0"},
                 { "_pd_sum_2theta_range_min": "20.0",
                   "_pd_sum_2theta_range_max": "25.0"}
                ]
              ],
    #     other loops here, with the same structure
              ]
             }


def edf_keywords_completion(edfin, keywords, edfout=None):
    """This procedure takes an EDF file and completes it with the keywords given as CIF dictionnary
    @param edfin: The name or the path of an EDF file to be read
    @type  edfin: Python String  
    @param keywords: dictionary containing the CIF-like data
    @type  keywords: Python dictionary
    @param edfout:  name or the path of an EDF file to be written. Caution, this WILL overwrite the file. If nothing is given, the name witll be edfin+keywords.edf
    @type  edfout: Python String  
    """
    if not edfout:edfout = os.path.splitext(edfin)[0] + "+keywords.edf"
    print "processing file %s --->%s " % (edfin, edfout)
    infile = EDF.EdfFile(edfin)
    data = infile.GetData(0)
    headers = infile.GetHeader(0)
    for key in keywords:
        if key.lower() == "loop_":
#As loops are not possible in EDF headers, we replace them by a kind of list
            loops = keywords [key]
            for oneLoop in   loops:
                oneLoopIdx = 0 #this is a index of the loop
                for   oneLoopdict in oneLoop[1]:
                    oneLoopIdx += 1
                    for loopKey in oneLoop[0]:
                        headers[ "%s[%i]" % (loopKey , oneLoopIdx) ] = oneLoopdict [ loopKey ]
        else:
            headers[key] = keywords[key]
    outfile = EDF.EdfFile(edfout)
    outfile.WriteImage(headers, data)



if __name__ == '__main__':
    EDF_to_process = []
    cif = CIF()
    if len(sys.argv) == 0:
        raise "Please enter the name of a EDF file to be completed"
    for i in sys.argv[1:]:
        if os.path.isfile(i):
            if os.path.splitext(i)[1].lower() == ".edf" :
                    EDF_to_process.append(i)
            elif os.path.splitext(i)[1].lower() == ".cif" :
                print "I agree with you: it would be nice to be allowed to give a CIF input file to feed the system"
                cif.loadCIF(i)
            else:
                print "Sorry I don't know what to do with this %s file" % i
        else:
            print "Sorry %s is not a readable file" % i

    if len(cif) == 0:
           #just use the default data instead !   
            for key in default_data:
                cif[key] = default_data[key]
            #cif.saveCIF("default.cif")


    for edfin in  EDF_to_process:
        edf_keywords_completion(edfin, cif, edfin[:-4] + "_completed.edf")



