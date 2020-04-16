import probability as prb
import model
import plot



numberOfTests = 1000
list = []
favorableNumber = 0;
possibleNumber = 0;

for i in range(numberOfTests):
    a = prb.getRandomPoint()
    b = prb.getRandomPoint()
    if ((b>=a*a) & (b<=pow(a, 0.5))):
        favorableNumber += 1
    possibleNumber += 1
    list.append([a,b,favorableNumber, possibleNumber])
plot.showPlot(list)
model.showModel(list)
