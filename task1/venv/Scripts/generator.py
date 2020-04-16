
import probability as prb
import matplotlib.pyplot as plt
import time
import showPlot

numberOfTests = 10000

favorableCount = 0;
possibleCount = 0;
graphList = []


for i in range(numberOfTests):
    firstIvanovHit = prb.doesIvanovHit();
    secondIvanovHit = prb.doesIvanovHit();
    firstPetrovHit = prb.doesPetrovHit();
    secondPetrovHit = prb.doesPetrovHit();
    if (prb.isHeads()):
        if (firstIvanovHit==False & firstPetrovHit==True):
            continue
        if (firstIvanovHit==False & secondIvanovHit==False):
            continue
        possibleCount += 1
        favorableCount += 1

        graphList.append(favorableCount/possibleCount)
    else:
        if (firstPetrovHit==True):
            continue
        if (firstIvanovHit==False & secondIvanovHit==False):
            continue
        possibleCount += 1
        graphList.append(favorableCount/possibleCount)
showPlot.showPlot(graphList)