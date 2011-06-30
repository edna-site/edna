#suggestedStrategyComment = suggestedStrategyComment.split("\n")[0]
print suggestedStrategyComment
listValues = suggestedStrategyComment.split(" ")
phi_reference = phi
kap1_reference = kap1
kap2_reference = kap2
phi = float(listValues[0].split("=")[1])
kap1 = float(listValues[1].split("=")[1])
kap2 =  float(listValues[2].split("=")[1])
strategy =  str(listValues[3].split("=")[1].split()[0])
print listValues, phi, kap1, kap2, [strategy]

possibleOrientations_Reference = possibleOrientations

run_number = run_number + 1
