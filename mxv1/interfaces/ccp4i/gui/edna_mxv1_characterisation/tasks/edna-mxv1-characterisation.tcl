#
# procedure which is run automatically before drawing the interface
# used to set up variables, menus etc
#---------------------------------------------------------------------
proc edna-mxv1-characterisation_setup { typedefVar arrayname } {
#---------------------------------------------------------------------

  upvar #0 $typedefVar typedef
  upvar #0 $arrayname array

  SetProgramHelpFile [FileJoin [GetEnvPath EDNA_HOME] mxv1 interfaces ccp4i gui edna_mxv1_characterisation help edna-mxv1-characterisation.html ]

  set typedef(_image_file)         { file IMG "*.cbf,.img,*.mccd,*.image,*.mar????" "image file" "{View Image}" "ImageViewer" }
  set typedef(_mtv_file)           { file MTV ".mtv" "mtv plot file" "{View Plot}" "MtvViewer" }
  set typedef(_xml_file)           { file XML ".xml" "xml file" "{View XML}" "open_url" }
  set typedef(_jpg_file)           { file JPG ".jpg" "jpg file" "{View jpg image}" "open_url" }

#
#  images, and MTV files are not the standard file type in ccp4, 
#  and I could not find out how to add inherit default "file_types", so redefine them all
#
  set typedef(file_types)	   { _any_file _MTZ_file _na4_file _sca_file _hkl_file _map_file _mask_file _q_map_file _o_map_file _pdb_file _CIF_file _html_file _xml_file _tls_file _lib_file _def_file _run_file _log_file _log_graph_file _ps_file _plot84_file _dic_file _xmgr_file _graph_file _data_file _txt_file _pck_file _tab_file _mr_file _ha_file _molrep_file _seq_file _pir_file _image_file _mtv_file _jpg_file }

 DefineMenu _menu_input_type       [list "Images" "EDNA XML File"] \
                                   [list  images  ednaxml]

 DefineMenu _menu_complexity       [list  "single wedge" "few sub-wdges" "many sub-wedges"] \
                                   [list  "none" "min" "full"]

 DefineMenu _menu_tento        [list 10^8 10^9 10^10 10^11 10^12 10^13 10^14] \
                               [list 8 9 10 11 12 13 14 ]

 DefineMenu _menu_chemicalCompositionInput  [list "of an average protein crystal" "input" ] \
                               [list default input  ]

  DefineMenu _menu_chain_type   [list "protein" "DNA" "RNA" ] \
                               [list "protein" "DNA" "RNA" ]
 
 return 1 
}
#
#--------------------------------------------------------------
proc edna-mxv1-characterisation_run { arrayname } {
#--------------------------------------------------------------
    upvar #0 $arrayname array 
  
    set array(XMLtmp) [FileJoin [ GetDefaultDirPath ] EDPluginControlCCP4iv10_dataInput_[GetPid].xml]
    set array(projectDirectory) [FileJoin [ GetDefaultDirPath ]]
#    set array(listOfOutputFiles) [FileJoin [ GetDefaultDirPath ] characterizationOutputFiles_[GetPid].txt]
#    if { $array(CharacterizationOutputFile) == "" } {
#	WarningMessage "Undefined Characterization Output File name "
#	return 0
#    }	
    append xstr [xmlHeader]
    append xstr [xmlOpenObject  "XSDataInputCCP4i"] 
    if { $array(InputType) == "Images"   } {
	if { $array(NumberOfSubWedges) <= 0 } {
	    WarningMessage "Need at least one data set"
	    return 0
	}
	for  {set n 1} { $n <= $array(NumberOfSubWedges) } { incr n } {
	    append xstr [xmlOpenObject  "dataSet"]
	    set m 0
	    set x [makeImageList $arrayname $n]
	    foreach file $x {
		incr m
		append xstr [xmlOpenObject   "imageFile" ]
#		append xstr [xmlAddValue   "number" $m]
		append xstr [xmlAddValue   "path" $file]
		append xstr [xmlCloseObject  "imageFile" ]
	    }
    	    if { $m == 0 } {
		WarningMessage "No images in data set $n"
		return 0
	    }
	    append xstr [xmlCloseObject  "dataSet"]
	}
    }
    if { $array(InputType) == "EDNA XML File"   } {
	for  {set n 1} { $n <= $array(NumberOfXMLFiles) } { incr n } {
	    set file [GetFullFileName1 $array(XMLInput,$n) $array(DIR_XMLInput,$n) ] 
	    if { ! [file exists $file ] } {
		WarningMessage "Can not open input XML file \"$file\" "
		return 0
	    }
	    append xstr [xmlOpenObject   "dataFile" ]
	    append xstr [xmlAddValue   "path" $file ]
	    append xstr [xmlCloseObject  "dataFile" ]
	}
    }
#
# 
    append xstr [xmlOpenObject   "diffractionPlan" ]
    append xstr [xmlAddValue  "complexity" [GetValue $arrayname Complexity] ]
    if { $array(doForceSpaceGroup) } {
	set sg [GetSpaceGroupCode $array(forcedSpaceGroup) ]
	if { $sg == 0 } {
	    set sg [GetSpaceGroupNumber $array(forcedSpaceGroup) ]
	    set sg [GetSpaceGroupCode $sg ]
	}
	if { $sg == 0 } {
	    WarningMessage "Invalid value for forced Space group $array(forcedSpaceGroup)"
	    return 0
	} {
	    set array(forcedSpaceGroup) $sg 
            append xstr [xmlAddValue  "forcedSpaceGroup" $sg]
	}
    }
# check numerical diffraction plan things
# 
    if { [catch { expr $array(maxExposureTimePerDataCollection) } ] || $array(maxExposureTimePerDataCollection) <= 0 } {
	WarningMessage "Invalid value for maximum exposure time per data collection"
	return 0
    }
    if { [catch { expr $array(aimedIOverSigmaAtHighestResolution) } ] || $array(aimedIOverSigmaAtHighestResolution) <= 0 } {
	WarningMessage "Invalid value for aimed I over Sigma at highest resolution "
	return 0
    }
    append xstr [xmlAddValue  "maxExposureTimePerDataCollection" $array(maxExposureTimePerDataCollection)]
    append xstr [xmlAddValue  "aimedIOverSigmaAtHighestResolution" $array(aimedIOverSigmaAtHighestResolution)]
#
    if { [catch { expr $array(minExposureTimePerImage) } ] || $array(minExposureTimePerImage) <= 0 } {
	WarningMessage "Invalid value for minimum exposure time per image"
	return 0
    }
    # written out at "beam"
    if { $array(useAimedCompleteness) } {
	if { [catch { expr $array(aimedCompleteness) } ] || $array(aimedCompleteness) <= 0 || $array(aimedCompleteness) >= 1 } {
	    WarningMessage "Invalid value for aimed completeness"
	    return 0
	}
	append xstr [xmlAddValue  "aimedCompleteness" $array(aimedCompleteness)]
    }
    if { $array(useAimedResolution) } {
	if { [catch { expr $array(aimedResolution) } ] || $array(aimedResolution) <= 0 || $array(aimedResolution) >= 9.0 } {
	    WarningMessage "Invalid value for aimed resolution"
	    return 0
	}
	append xstr [xmlAddValue  "aimedResolution" $array(aimedResolution)]
    }
    if { $array(useAimedMultiplicity) } {
	if { [catch { expr $array(aimedMultiplicity) } ] || $array(aimedMultiplicity) <= 0 || $array(aimedMultiplicity) >= 97 } {
	    WarningMessage "Invalid value for aimed multiplicity"
	    return 0
	}
	append xstr [xmlAddValue  "aimedMultiplicity" $array(aimedMultiplicity)]
    }
    if { $array(anomalousData) } {
	append xstr [xmlAddValue "anomalousData" "true"] 
    } else {
	append xstr [xmlAddValue "anomalousData" "false"] 
    }
    append xstr [xmlCloseObject  "diffractionPlan"]
#
#
    append xstr [xmlOpenObject   "experimentalCondition"]
    append xstr [xmlOpenObject   "goniostat"]
    append xstr [xmlAddValue  "minOscillationWidth" $array(minOscillationWidth)]
    append xstr [xmlAddValue  "maxOscillationSpeed" $array(maxOscillationSpeed)]
    append xstr [xmlCloseObject  "goniostat"]
    append xstr [xmlOpenObject  "beam"]
    append xstr [xmlAddValue  "minExposureTimePerImage" $array(minExposureTimePerImage)]
# check beam only if RadiationDamege is needed
    if { $array(RadiationDamage) } {
	#
	# check beam numericals
	#
	if { [catch { expr $array(Flux) } ] || $array(Flux) <= 0 } {
	    WarningMessage "Invalid value for the flux"
	    return 0
	}
	if { [catch { expr $array(beamSizeHorizontal) } ] || $array(beamSizeHorizontal) <= 0 } {
	    WarningMessage "Invalid value for the beam Size Horizontal"
	    return 0
	}
	if { [catch { expr $array(beamSizeVertical) } ] || $array(beamSizeVertical) <= 0 } {
	    WarningMessage "Invalid value for beam Size Vertical"
	    return 0
	}
	# those can be xmled in one chunk	
	append xstr [xmlAddValue  "flux" $array(Flux)e[GetValue $arrayname fluxTenTo]]
	append xstr [xmlOpenObject  "size"]
        append xstr [xmlAddValue  "x" [expr 0.001*$array(beamSizeHorizontal)] ]
	append xstr [xmlAddValue  "y" [expr 0.001*$array(beamSizeVertical)  ] ]
	append xstr [xmlCloseObject  "size"]
    } 
    append xstr [xmlCloseObject  "beam"]
    append xstr [xmlCloseObject  "experimentalCondition"]    
    if { $array(RadiationDamage) } {
        #
        # check sample numericals
	#
	if { [catch { expr $array(sampleSizeX) } ] || $array(sampleSizeX) <= 0 } {
	    WarningMessage "Invalid value for sample SizeX"
	    return 0
	}	
	if { [catch { expr $array(sampleSizeY) } ] || $array(sampleSizeY) <= 0 } {
	    WarningMessage "Invalid value for sample SizeY"
	    return 0
	}	
	if { [catch { expr $array(sampleSizeZ) } ] || $array(sampleSizeZ) <= 0 } {
	    WarningMessage "Invalid value for sample SizeZ"
	    return 0
	}	
	if { [catch { expr $array(sampleShape) } ] || $array(sampleShape) <= 0 } {
	    WarningMessage "Invalid value for sample Shape Factor"
	    return 0
	}	
 	if { [catch { expr $array(sampleSusceptibility) } ] || $array(sampleSusceptibility) <= 0 } {
	    WarningMessage "Invalid value for sample Susceptibility"
	    return 0
	}
	#
	append xstr [xmlOpenObject  "sample"]
	append xstr [xmlOpenObject  "size"]
        append xstr [xmlAddValue  "x" [expr 0.001*$array(sampleSizeX)] ]
	append xstr [xmlAddValue  "y" [expr 0.001*$array(sampleSizeY)] ]
	append xstr [xmlAddValue  "z" [expr 0.001*$array(sampleSizeZ)] ]
	append xstr [xmlCloseObject  "size"]
	append xstr [xmlAddValue  "shape" $array(sampleShape)]
	append xstr [xmlAddValue  "susceptibility" $array(sampleSusceptibility)]
	
	#
	#  further checks are only if chemical composition input
	#
	if { $array(chemicalCompositionInputType) == "input" } {
	    if { [catch { expr $array(structureNumberOfCopiesInAsymmetricUnit) } ] || $array(structureNumberOfCopiesInAsymmetricUnit) <= 0 } {
		WarningMessage "Invalid value for structure Number Of Copies In Asymmetric Unit"
		return 0
	    }
	    append xstr [xmlOpenObject  "chemicalComposition"]
	    #
	    # check solvent
	    append xstr [xmlOpenObject  "solvent"]
	    append xstr [xmlOpenObject  "atoms"]
	    for {set n 1} { $n <= $array(numberOfSoventAtomTypes) } { incr n } {
		if {! [isHeavyAtomName  $array(solventAtomType,$n)] } {
		    WarningMessage "Invalid solvent heavy atom type \"$array(solventAtomType,$n)\""
		    return 0
		}
		if { [catch { expr $array(solventAtomConcentration,$n) } ] || $array(solventAtomConcentration,$n) <= 0 } {
		    WarningMessage "Invalid value for solvent atom $array(solventAtomType,$n) concentration"
		    return 0
		}	    
		append xstr [xmlOpenObject  atom]
		append xstr [xmlAddValue  "concentration" $array(solventAtomConcentration,$n)]
		append xstr [xmlAddValue  "symbol" $array(solventAtomType,$n)]
		append xstr [xmlCloseObject  "atom"]
	    }
	    append xstr [xmlCloseObject  "atoms"]
	    append xstr [xmlCloseObject  "solvent"]
	    #
	    # check chains
	    if { $array(numberOfChains) <= 0 } {
		WarningMessage "At least one Chain should be defined"
		return 0
	    }
	    append xstr [xmlOpenObject  "structure"]
	    append xstr [xmlAddValue  "numberOfCopiesInAsymmetricUnit" $array(structureNumberOfCopiesInAsymmetricUnit)]
	    for {set n 1} { $n <= $array(numberOfChains) } { incr n } {
		if { [catch { expr $array(chainNumberOfCopies,$n) } ] || $array(chainNumberOfCopies,$n) <= 0 } {
		    WarningMessage "Invalid value for Number Of Copies of chain $n"
		    return 0
		}	
		if { [catch { expr $array(chainNumberOfMonomers,$n) } ] || $array(chainNumberOfMonomers,$n) <= 1 } {
		    WarningMessage "Invalid value for Number of residues/nucleotides in chain $n"
		    return 0
		}
		append xstr [xmlOpenObject  "chain"]
		append xstr [xmlAddValue  "numberOfCopies" $array(chainNumberOfCopies,$n)]
		append xstr [xmlAddValue  "numberOfMonomers" $array(chainNumberOfMonomers,$n)]
		append xstr [xmlAddValue  "type" $array(chainType,$n)]
		if { $array(chainType,$n) == "protein" } {
		    append xstr [xmlOpenObject  "heavyAtoms"]
		    for {set m 1} { $m <= $array(chainNumberOfHeavyAtomTypes,$n) } { incr m } {
			if {! [isHeavyAtomName  $array(chainHeavyAtomType,[subst $n]_[subst $m])] } {
			    WarningMessage "Invalid heavy atom type \"$array(solventAtomType,$n)\ in chain $n"
			    return 0
			}
			if { [catch { expr $array(chainHeavyAtomCount,[subst $n]_[subst $m]) } ] || $array(chainHeavyAtomCount,[subst $n]_[subst $m]) <= 0 } {
			    WarningMessage "Invalid value for number of $array(chainHeavyAtomType,[subst $n]_[subst $m]) atoms in chain $n"
			    return 0
			}
			append xstr [xmlOpenObject  "atom"]
			append xstr [xmlAddValue  "numberOf" $array(chainHeavyAtomCount,[subst $n]_[subst $m])]
			append xstr [xmlAddValue  "symbol" $array(chainHeavyAtomType,[subst $n]_[subst $m])]
			append xstr [xmlCloseObject   "atom"]
		    }
		    append xstr [xmlCloseObject  "heavyAtoms"]		
		}
		append xstr [xmlCloseObject  "chain"]
	    }
	    #
	    # check ligands
	    for {set n 1} { $n <= $array(numberOfLigands) } { incr n } {
		append xstr [xmlOpenObject  "ligand"]		
		if { [catch { expr $array(ligandNumberOfCopies,$n) } ] || $array(ligandNumberOfCopies,$n) <= 0 } {
		    WarningMessage "Invalid value for Number Of Copies of ligand $n"
		    return 0
		}	
		if { [catch { expr $array(ligandNumberOfLightAtoms,$n) } ] || $array(ligandNumberOfLightAtoms,$n) <= -1 } {
		    WarningMessage "Invalid value for Number Of Light Atoms in lignad $n"
		    return 0
		}
		append xstr [xmlAddValue  "numberOfCopies" $array(ligandNumberOfCopies,$n)]
		append xstr [xmlAddValue  "numberOfLightAtoms" $array(ligandNumberOfLightAtoms,$n)]
		append xstr [xmlOpenObject  "heavyAtoms"]
		for {set m 1} { $m <= $array(ligandNumberOfHeavyAtomTypes,$n) } { incr m } {
		    if {! [isHeavyAtomName  $array(ligandHeavyAtomType,$n)] } {
			WarningMessage "Invalid heavy atom type \"$array(solventAtomType,$n)\ in ligand $n"
			return 0
		    }
		    if { [catch { expr $array(ligandHeavyAtomCount,[subst $n]_[subst $m]) } ] || $array(ligandHeavyAtomCount,[subst $n]_[subst $m]) <= 0 } {
			WarningMessage "Invalid value for number of $array(ligandHeavyAtomType,[subst $n]_[subst $m]) atoms in ligand $n"
			return 0
		    }
		    append xstr [xmlOpenObject  "atom"]
		    append xstr [xmlAddValue  "numberOf" $array(ligandHeavyAtomCount,[subst $n]_[subst $m])]
		    append xstr [xmlAddValue  "symbol" $array(ligandHeavyAtomType,[subst $n]_[subst $m])]
		    append xstr [xmlCloseObject  "atom"]
		}
		append xstr [xmlCloseObject  "heavyAtoms"]		
		append xstr [xmlCloseObject  "ligand"]	
	    }
	    append xstr [xmlCloseObject  "structure"]
	    append xstr [xmlCloseObject  "chemicalComposition"]
	} 
	append xstr [xmlCloseObject  "sample"]
    }
    append xstr [xmlCloseObject  "XSDataInputCCP4i"]
    WriteFile $array(XMLtmp) $xstr -overwrite
    return 1
}
#
#
#
proc edna-mxv1-characterisation_task_window { arrayname } {
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
  upvar #0 $arrayname array
#
# numbered gui folders, #0="Protocol",#1="file"  others incremented
# starting from 1!
#
  if { [CreateTaskWindow $arrayname  \
	    "Run EDNA Characterization" "EDNA" \
	    [ list "Diffraction Plan" \
		   "Beam" \
		   "Sample" \
		   "Goniostat" ]
         ] == 0 } return


#=PROTOCOL==============================================================
 
  OpenFolder protocol

  CreateLine line \
     message "Enter a title for this job (TITLE)" \
     help "Title" \
     label "Title" \
     widget TITLE -width 80
# 
# "help tag" points browser to html tags in an html help file defined by _setup
#
  CreateLine line \
      message "Choose the type of input" \
      help "GUI_Run_EDNA_Characterization_using" \
      label "Run EDNA Characterization using " \
      widget InputType label "input"

  CreateLine line \
      toggle_display RadiationDamage open 0 \
      message "Enable or disable radiation damage model" \
      help "GUI_Account_for_radiation_damage_using_chemical_composition" \
      widget RadiationDamage label "Account for radiation damage" 
 
  CreateLine line \
      toggle_display RadiationDamage open 1 \
      message "Choose between using average protein structure composition and exact definition" \
      help "GUI_Account_for_radiation_damage_using_chemical_composition" \
      widget RadiationDamage label \
       "Account for radiation damage" \
      label "using chemical composition" \
      widget chemicalCompositionInputType
 
#=FILES================================================================
#======================================================================

  OpenFolder file
  OpenSubFrame frame -toggle_display InputType open "images"
     CreateToggleFrame \
         NumberOfSubWedges \
         listSubWedge \
	 "Define a data set" "Data set #" "Add data set"  \
	 [list NumberOfImages Image DIR_Image ]  \
         -child listImg
  CloseSubFrame

  OpenSubFrame frame -toggle_display InputType open "ednaxml"
     CreateExtendingFrame \
         NumberOfXMLFiles \
         listXMLFile \
         "Add input XML file" \
         "Add file" \
         [list XMLInput DIR_XMLInput]
  CloseSubFrame

  CreateOutputFileLine line \
      "Characterization Output XML file" \
      "XML Output" \
      CharacterizationOutputFile \
      DIR_CharacterizationOutputFile \
      -help "GUI_XML_ouput_file"

#=Diffraction plan================================================================
#======================================================================
  OpenFolder 1 doForceSpaceGroup open { 0 1 } open
  CreateLine line \
      help "GUI_Force_Space_Group" \
      message "Define known space group for indexing and strategy calulation" \
      toggle_display doForceSpaceGroup open 0 \
      widget doForceSpaceGroup \
      label "Force Space Group "

  CreateLine line \
      help "GUI_Force_Space_Group" \
      message "Input space group IT number or symbol" \
      toggle_display doForceSpaceGroup open 1 \
      widget doForceSpaceGroup  -oblig\
      label "Force Space Group " \
      widget forcedSpaceGroup  -oblig

  CreateLine line \
      help "GUI_Strategy_complexity" \
      message "Choose between single wedge and multi-subwedge strategies" \
      label "Strategy complexity " \
      widget Complexity

  CreateLine line \
      help "GUI_Maximum_exposure_time_per_data_collection" \
      message "Enter maximum total exposure time per data collection, in seconds" \
      label "Maximum Exposure time per data collection " \
      widget maxExposureTimePerDataCollection  -oblig\
      label "seconds"

  CreateLine line \
      help "GUI_Aimed_I_Over_Sigma_at_highest_resolution" \
      message "Define I/Sigma in a last resolution shell you want to have in you final data set" \
      label "Aimed I Over Sigma at highest resolution " \
      widget aimedIOverSigmaAtHighestResolution  -oblig

  CreateLine line \
      help "GUI_Anomalous" \
      message "Anomalous scattering data?" \
      widget anomalousData \
      label "Anomalous data" 

  CreateLine line \
      help "GUI_Minimum_oscillation_width" \
      message "Define the smallest oscillation width you want to permit for this data collection" \
      label "Minimum oscillation width " \
      widget minOscillationWidth  -oblig \
      label "degree(s)"

  CreateLine line \
      help "GUI_Define_Aimed_Completeness" \
      message "Default strategy is for 0.99 ocverall completeness. Check to re-define." \
      toggle_display useAimedCompleteness open 0 \
      widget useAimedCompleteness \
      label "Define Aimed Completeness (default >= 0.99 )" 
  CreateLine line \
      help "GUI_Define_Aimed_Completeness" \
      message "Input an overal completeness (in fraction) that you want to have" \
      toggle_display useAimedCompleteness open 1 \
      widget useAimedCompleteness \
      label "Define Aimed Completeness" \
      widget aimedCompleteness  -oblig 

  CreateLine line \
      help "GUI__Define_Aimed_Resolution" \
      message "Check this button to lower the resolution" \
      toggle_display useAimedResolution open 0 \
      widget useAimedResolution \
      label "Define Aimed Resolution (default - highest possible)" 
  CreateLine line \
      help "GUI__Define_Aimed_Resolution" \
      message "Input the resolution limit above which you do not want to collect the data even if it is possible" \
      toggle_display useAimedResolution open 1 \
      widget useAimedResolution \
      label "Define Aimed Resolution" \
      widget aimedResolution  -oblig \
      label "Angstroem"

  CreateLine line \
      help "GUI_Define_Aimed_Multiplicity" \
      message "Check this button if you want to collect data with high multiplicity" \
      toggle_display useAimedMultiplicity open 0 \
      widget useAimedMultiplicity \
      label "Define Aimed Multiplicity (default - optimized)"
  CreateLine line \
      help "GUI_Define_Aimed_Multiplicity" \
      message "Give a value of multiplicity you want for this data (sensfull in conjunction with I/Sigma > 10 or higher)." \
      toggle_display useAimedMultiplicity open 1 \
      widget useAimedMultiplicity \
      label "Define Aimed Multiplicity" \
      widget aimedMultiplicity  -oblig 


#=Beam Parameters================================================================
#======================================================================
  OpenFolder 2 RadiationDamage hide 0 
  CreateLine line label "X-ray beam" -italic
  CreateLine line \
      help "GUI_Flux" \
      message "Input incident beam flux in photon/second" \
      label "Flux" widget Flux  -oblig label "x" \
      widget fluxTenTo \
      label "photons/second"

  CreateLine line \
      help "GUI_Beam_size" \
      message "Define beam size (full width at half maximum, FWHM)" \
      label "Beam size (Horizontal x Verical)" \
      widget beamSizeHorizontal  -oblig \
      label "x" \
      widget beamSizeVertical  -oblig \
      label "micron^2"


#=Sample================================================================
#======================================================================
  OpenFolder 3 RadiationDamage hide 0 

  #=Generic Sample Parameters============================================
  #======================================================================
  CreateLine line \
      help "GUI_Sample_Dimensions_and_Susceptibility" \
      message "Define approximate sample dimensions and relative radiation sensitivity" \
      label "Dimensions (across spindle axis)"  \
      widget sampleSizeY -oblig \
      label "x" \
      widget sampleSizeZ -oblig \
      label "micron" \
      label "Radiation susceptibiliy" \
      widget sampleSusceptibility -oblig
   
#      label "x" \
#      widget sampleSizeZ -oblig \     
#  CreateLine line \
#      label "Shape factor"  \
#      widget sampleShape \
#      label "Radiation susceptibiliy" \
#      widget sampleSusceptibility      

  #=Chemical Composition=================================================
  #======================================================================

  #======================================================================
  # Full Input
  #======================================================================
  OpenSubFrame frame -toggle_display chemicalCompositionInputType open "input"
#      CreateLine line label "--" # need to find a proper separator...
      CreateLine line label "Chemical composition" -italic
      #======================================================================
      # Solvent
      #======================================================================
#      CreateLine line label "--" # need to find a proper separator...
      CreateLine line label "Solvent (Only atoms heavier than oxygen need to be specified)" -italic
      CreateExtendingFrame \
            numberOfSoventAtomTypes \
            listSolventAtoms \
            "Add solven constituent:" "Add heavy atom" \
            [list solventAtomType solventAtomConcentration]
 
      #======================================================================
      # Chains
      #======================================================================
#      CreateLine line label "--" # need to find a proper separator...
      CreateLine line label "Structure" -italic
      CreateLine line \
         help "GUI_Number_of_copies"\
         message "Enter number of structures in asymetric unit. A multiplier is applied to chains and ligands." \
         label "Number of copies in asymetric unit" \
         widget structureNumberOfCopiesInAsymmetricUnit -oblig 
      CreateToggleFrame \
         numberOfChains \
            listChains \
            "Add chain:" "Chain number"  "Add chain" \
             [list chainNumberOfCopies \
		   chainNumberOfMonomers \
		   chainType \
		   chainNumberOfHeavyAtomTypes \
		   chainHeavyAtomType \
		   chainHeavyAtomCount ] \
            -child listChainHeavyAtoms
      #======================================================================
      # Ligands
      #======================================================================
      #CreateLine line label "Ligands" -italic
      CreateToggleFrame \
         numberOfLigands \
            listLigands \
            "Add ligand:" "Ligand number"  "Add Ligand" \
             [list ligandNumberOfCopies \
		   ligandNumberOfLightAtoms \
		   ligandNumberOfHeavyAtomTypes \
		   ligandHeavyAtomType \
		   ligandHeavyAtomCount ] \
            -child listLigandHeavyAtoms      

  CloseSubFrame
  WriteCredits [list "EDNA developers" ] -link "http://www.edna-site.org" http://www.edna-site.org

#=Goniostat================================================================
#======================================================================
  OpenFolder 4 
  CreateLine line \
      help "GUI_Maximum_rotation_speed"\
      message "Define maximum rotation speed. This affects attenuation in strategy."\
      label "Maximum rotation speed" \
      widget maxOscillationSpeed \
      label "degree(s)/second"

  CreateLine line \
      help ""\
      message "Define minimum exposure time per frame. This affects attenuation in strategy."\
      label "Minimum Exposure time per frame" \
      widget minExposureTimePerImage \
      label "second(s)"
  
}
#
#
#--------------------------------------------------------------------
proc ImageViewer { file } {
#--------------------------------------------------------------------
  if { ![ catch {set x [GetEnvPath CCP4I_IMAGEVIEWER]  } ] } {
      set status [expr 1 - [ catch { eval exec $x $file & } ] ]
      PleaseWait
      ExitFileViewer
      return $status
  }
  return 1
}

#--------------------------------------------------------------------
proc MtvViewer { file } {
#--------------------------------------------------------------------
  PleaseWait "Displaying plot with plotmtv"
  set status [expr 1 - [ catch { eval exec plotmtv $file & } ] ]
  PleaseWait
  ExitFileViewer
  return $status
}
#
#--------------------------------------------------------------------
proc XMLViewer { file } {
#--------------------------------------------------------------------
  PleaseWait "Displaying XML with firefox"
  set status [expr 1 - [ catch { eval exec firefox $file & } ] ]
  PleaseWait
  ExitFileViewer
  return $status
}
#
#--------------------------------------------------------------------
proc JPGViewer { file } {
#--------------------------------------------------------------------
  PleaseWait "Displaying XML with firefox"
  set status [expr 1 - [ catch { eval exec display $file & } ] ]
  PleaseWait
  ExitFileViewer
  return $status
}
#
#----------------------------------------------------------------------
#----------------------------------------------------------------------
proc listXMLFile { arrayname counter } {
#----------------------------------------------------------------------
  upvar #0 $arrayname array
     CreateInputFileLine line \
        "Enter XML file" \
        "EDNA XML file" \
         XMLInput DIR_XMLInput -help "GUI_EDNA_XML_file"\
      -fileout CharacterizationOutputFile DIR_CharacterizationOutputFile "_ednaCharacterization"
}
#----------------------------------------------------------------------
#----------------------------------------------------------------------
proc listImg { arrayname c1 c2 } {
#----------------------------------------------------------------------
  upvar #0 $arrayname array

  CreateInputFileLine line \
      "Enter image file name" \
      "image #$c1 in" \
       Image DIR_Image -help "GUI_Images" \
      -fileout CharacterizationOutputFile DIR_CharacterizationOutputFile "_ednaCharacterization"
}
#
#----------------------------------------------------------------------
#----------------------------------------------------------------------
#
proc listSubWedge { arrayname counter } {
#----------------------------------------------------------------------
  upvar #0 $arrayname array
    CreateExtendingFrame \
      NumberOfImages \
      listImg \
      "Add an image" \
      "Add an image" \
       [list NumberOfImages Image DIR_Image] \
      -counter $counter
     CreateLine line \
      help "GUI_glob_and_clean" \
      button "glob" \
      -command "globImg $arrayname $counter" \
      button "clean" \
      -command "cleanImg $arrayname $counter" 
}
#
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc listSolventAtoms { arrayname counter } {
#-------------------------------------------------------------------------
  upvar #0 $arrayname array
      CreateLine line  \
         help "GUI_Solvent" \
         message "Enter solvent constituent atom type and concentration (in millimol)" \
         message "Input chemical name of solvent constituent and its concentration in milliMol" \
         label "Atom:" widget solventAtomType -width 2 -oblig\
         label " Concentration:" widget solventAtomConcentration -width 4 -oblig label "mM" 
}
#
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc listChains { arrayname counter } {
#-------------------------------------------------------------------------
  upvar #0 $arrayname array

      CreateLine line \
         toggle_display $array(chainType,$counter) open protein \
         help "GUI_Chains "\
         message "Define a protein/DNA/RNA chain " \
         label "Number of copies" widget chainNumberOfCopies -width 3 -oblig\
         label "   Number of residues (or nucleotides) in chain" widget chainNumberOfMonomers -oblig\
         label "   Type" widget chainType 

      OpenSubFrame frame -toggle_display chainType,$counter open "protein"
 
          CreateLine line \
          label "Number and type of heavy atoms (S,Se) in the chain"
#              label "Indicate heavy atoms (like S,Se,...) that belong to this chain"

          CreateExtendingFrame chainNumberOfHeavyAtomTypes \
               listChainHeavyAtoms \
               "List heavy atoms (S,Se,...) in the chain" \
               "Add heavy atom" \
               [list chainHeavyAtomType chainHeavyAtomCount] \
               -counter $counter 
      CloseSubFrame
}
#
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc listLigands { arrayname counter } {
#-------------------------------------------------------------------------
  upvar #0 $arrayname array

      CreateLine line \
         help "GUI_Ligands" \
         message "Define ligand" \
         label "Number of copies" \
         widget ligandNumberOfCopies -width 3 -oblig\
         label "   Number of light atoms (O,C,N)" \
         widget ligandNumberOfLightAtoms -oblig

      CreateLine line \
          label "Number and type of heavy atoms in this ligand"

      CreateExtendingFrame ligandNumberOfHeavyAtomTypes \
          listLigandHeavyAtoms \
          "List heavy atoms (S,Se,...) in the chain" \
           "Add heavy atom" \
           [list ligandHeavyAtomType ligandHeavyAtomCount] \
           -counter $counter
}
#
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc listChainHeavyAtoms { arrayname c2 c1 } {
#-------------------------------------------------------------------------
  upvar #0 $arrayname array
      CreateLine line  \
         help "GUI_Chains" \
         message "Bound heavy atoms (S,Se,...)" \
         label "Atom type" \
         widget chainHeavyAtomType -width 2 -oblig\
         label "Number of atoms" \
      widget chainHeavyAtomCount -oblig
}
#
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc listLigandHeavyAtoms { arrayname c4 c3 } {
#-------------------------------------------------------------------------
  upvar #0 $arrayname array
      CreateLine line  \
         help "GUI_Ligands" \
         message "Bound heavy atoms (S,Se,...)" \
         label "Atom type" \
         widget ligandHeavyAtomType -width 2 -oblig\
         label "Number of atoms" \
         widget ligandHeavyAtomCount -oblig
}
#
#
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc isHeavyAtomName { name } {
#-------------------------------------------------------------------------
    #
    # No H,He,C,O,N allowed among heavy atoms
    # though He is $0 in a list, > 0's are permitted
    #
    set ha [list he li be b f ne \
                 na mg  al si p s cl ar \
                 k ca sc ti v cr mn fe co ni cu zn ga ge as se br kr\
                 rb sr y  zr nb mo tc ru rh pd ag cd in sn sb te  xe \
                 cs ba lu hf ta w  re os ir pt au hg tl pb bi po at rn \
                 fr ra lr rf db sg bh hs mt ds  rg \
                 la ce pr nd pm sm eu gd tb dy ho er tm yb 
	   ]  
    if { [lsearch -regexp $ha (?i)^[subst ${name}]$ ] <= 0 } {
	return 0
    } {
	return 1
    }
}
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc xmlHeader {} {
    set x "<?xml version=\"1.0\" ?>"
    return $x
}
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc xmlOpenObject { name } {
    set x "<$name>"
    return $x
}
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc xmlCloseObject { name } {
    set x "</$name>"
    return $x
}
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc xmlAddValue { name value } {
    set x  "<$name><value>$value</value></$name>"
    return $x
}
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
proc globImg { arrayname counter} {
    upvar #0 $arrayname array
    set fullNameList [makeImageList $arrayname $counter]
	if { $fullNameList == " " } return
    if { [llength $fullNameList] > 30 } {
        WarningMessage "Warning: Too many files ( [llength $fullNameList] ) in a list, globing cancelled"
	return
    }
	cleanImg $arrayname $counter
    delete_frame $arrayname listImg $counter 1
	set n 0
    foreach fullName $fullNameList {
		incr n
		set dir [file dirname $fullName]
		set Image $fullName
		set DIR_Image "Full path.."
		foreach projectAlias [ListProjectsBothCCP4Is] {
			set projectDir [GetFullDirName $projectAlias]
			if { $projectDir == $dir } {
				set Image [file tail $fullName]
				set DIR_Image $projectAlias
				break
			} 
		}
	   	set array(Image,${counter}_${n}) $Image
		set array(DIR_Image,${counter}_${n}) $DIR_Image
		UpdateExtendingFrame listImg $counter $arrayname 1
    }
}
#
#-------------------------------------------------------------------------
proc ListProjectsBothCCP4Is { } {
#-------------------------------------------------------------------------
	set x 0
	catch {set x [using_dbccp4i]}
	if { $x } {
	 	 return [lsort -dictionary [dbccp4i_list_projects]]
	} else {	
		# Direct access
		global directories
		set projects {}
		set n 0
		catch {set n $directories(N_PROJECTS)}
		for { set i 1 } { $i<=$n } { incr i } {
			lappend projects $directories(PROJECT_ALIAS,$i)
		}
		return [lsort -dictionary $projects]
	}
}	
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc cleanImg { arrayname counter} {
    upvar #0 $arrayname array
    while { $array(NumberOfImages,$counter) >= 1 } {
		delete_frame $arrayname listImg $counter 1
    }
    set array(Images,${counter}_1) "" 
    set array(Dir_image,${counter}_2) "PROJECT"
    UpdateExtendingFrame listImg $counter $arrayname 1
}
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
proc makeImageList { arrayname counter} {
    upvar #0 $arrayname array
    set x " "
    set z " " 
    for {set n  1} { $n <= $array(NumberOfImages,$counter) } { incr n } {
	    append x " " [glob -nocomplain [GetFullFileName1 $array(Image,${counter}_$n) $array(DIR_Image,${counter}_$n)]]
    }
    set x [lsort -uniq $x]
    foreach y $x {
		if {[file isfile $y]} {
	    	append z " " $y
		}	
    }	
	return $z		
}
#-----------------------------------------------------------------------
