
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print suggestedStrategyComment
listValues = suggestedStrategyComment.split(" ")
phi_new = float(listValues[0].split("=")[1])
kap1_new = float(listValues[1].split("=")[1])
kap2_new =  float(listValues[2].split("=")[1])
print phi_new, kap1_new, kap2_new

possibleOrientations_Reference = possibleOrientations