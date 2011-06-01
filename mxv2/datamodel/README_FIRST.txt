Prelimiaries:
The MMXv2/Xv2Data and MXv2/XSDataCommon packages should have the following tags set:
 targetNamespace: http://www.edna-site.org
defaultNamespace: http://www.edna-site.org
schemaLocation: XSDataCommon.xsd
The MXv2/MXv2Data package should also have the following tag set:
EdnaXSDClassPrefix: XS
Make sure that there is a dependency relationship going from the top-level "MXv2" package to the XSData class in XSDataCommon, with the name "EdnaXSDAncestor".

Step 1: Transform MXv2 package into an XSD model:

Right-click on the top-level package "MXv2" in the project browser and select "Transform current package"
Check "XSD" under Transformations, and choose the package "XSD" as the target.
Check the "Include child packages" box, and make sure that all classes are selected.
Click on "Do Transform"
Wait until both the transform dialog and progress window close

Step 2: Generate XSD:

Right-click on the new package "XSD/MXv2/MXv2Data" in the project browser and select "Code Engineering" -> "Generate XML Schema..."
Enter filename if necessary and click "Generate"

The sub-package "XSD/MXv2" MUST be deleted before repetating Step 1, to avoid duplication of generated Generalisation connectors. Leave the empty parent package "XSD" in the model though.

