numberCases = int(input())
typesOfCoins = []
valuesOfCoins = []
cost = []
def getInputs():
    typesOfCoins.append(input())
    valuesOfCoins.append(input().split(" "))
    cost.append(input())
getInputs()
getInputs()
getInputs()

for i in range(3):
    