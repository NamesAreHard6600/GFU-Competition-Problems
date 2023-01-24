import itertools
import re
#Recursion all combinations of ships 
#Numbers are too big for a knapsack (and decimals)

class Ship: #More like a collection of ships
  def __init__(self,names,weight,value):
    self.names = names
    self.weight = weight
    self.value = value
  
  def __repr__(self): #Prints it out as expected
    ret = ""
    for name in sorted(self.names):
      ret += f"{name}\n"
    return ret + f"{self.weight} tons - ${self.value}"
  
  def __add__(self,otherShip): #Just adds all values of ship
    return Ship(self.names+otherShip.names,self.weight+otherShip.weight,self.value+otherShip.value)
  
#Take Input of all ships
ships = []
file = "JB.in" #File to read from
with open(file,"r") as f:
  read = f.readline #You can change this to input for "real" inputs
  num = read()
  for i in range(int(num)):
    data = read().strip()
    data = re.split("-|/",data) #Split my multiple, - and /
    ships.append(Ship([data[0]],int(data[1]),float(data[2])))

emptyShip = Ship([],0,0)
best = emptyShip
max_weight = 100000 #Given in problem
for i in range(1,len(ships)+1):
  for combo in itertools.combinations(ships,i): #All combinations of every length
    curr = sum(combo,emptyShip) #Add all ships
    if curr.weight <= max_weight and curr.value > best.value: #See if it's the best and not overweight
      best = curr
print(best)
