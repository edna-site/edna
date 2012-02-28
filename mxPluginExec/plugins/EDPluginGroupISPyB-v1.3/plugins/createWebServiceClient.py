strEdml = """
complex type XSDataISPyBScreeningOutputLattice extends XSData {
    screeningOutputLatticeId : XSDataInteger optional
    screeningOutputId : XSDataInteger
    spaceGroup : XSDataString
    pointGroup : XSDataString
    bravaisLattice : XSDataString
    rawOrientationMatrix_a_x : XSDataDouble
    rawOrientationMatrix_a_y : XSDataDouble
    rawOrientationMatrix_a_z : XSDataDouble
    rawOrientationMatrix_b_x : XSDataDouble
    rawOrientationMatrix_b_y : XSDataDouble
    rawOrientationMatrix_b_z : XSDataDouble
    rawOrientationMatrix_c_x : XSDataDouble
    rawOrientationMatrix_c_y : XSDataDouble
    rawOrientationMatrix_c_z : XSDataDouble
    unitCell_a : XSDataDouble
    unitCell_alpha : XSDataDouble
    unitCell_b : XSDataDouble
    unitCell_beta : XSDataDouble
    unitCell_c : XSDataDouble
    unitCell_gamma : XSDataDouble
    timeStamp : XSDataString
}
"""

# Parse XML
bDefiningWebService = False
for strLine in strEdml.split("\n"):
    if strLine.find("complex type") != -1:
        bDefiningWebService = True
    if strLine.find("}") and bDefiningWebService:
        bDefiningWebService = False
    print strLine, bDefiningWebService
