EDPluginSPD
===========

Author: Jerome Kieffer (kieffer@esrf.fr)

This is the documentation for the EDNA execution plugins around SPD, including image 
correction, azimuthal transformation (Caking) regrouping and azimuthal integration.

== EDPluginSPDCorrectv10 ==
Image correction by SPD, keeping a certain number of workers under control.
this is pretty fast (<1sec/image) 

== EDPluginSPDCakev1_5 ==
Based on the same concepts as EDPluginSPDCorrectv10, EDPluginSPDCakev1_5 offers azimuthal 
regrouping (x,y)-> (r,chi) with EDF output at the moment but this should be improved

There are elder plugins EDPluginSPDCakev1_0 and 1_1, but they are no more maintened as they are much slower, 
i.e. on SPD instance per image, we loose all performances gained with the lookup-table kept in memory.
  