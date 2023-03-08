#https://en.wikipedia.org/wiki/Knapsack_problem
#Here's how this works, I understand it at the moment, but if I forget later let's be honest, me adding comments won't help
#This is amazing anyway I won't forget this. 

true = True
false = False


def file_reading():
  table = []
  with open("T.in", 'r') as f:
    num = int(f.readline().strip())
    table.append(num)
    for i in range(num):
      table.append(f.readline().strip())
      num2 = int(table[-1].split()[1])
      for j in range(num2):
        table.append(f.readline().strip())
  return table


def input_reading():
  table = []
  num = int(input().strip())
  table.append(num)
  for i in range(num):
    table.append(input().strip())
    num2 = int(table[-1].split()[1])
    for j in range(num2):
      table.append(input().strip())
  return table

class Knapsack:
  def __init__(self,max_weight):
    self.max_weight = max_weight
    self.weights = []
  
  def addWeight(self, weight):
    self.weights.append(weight)
    
  def init(self):
    self.W = self.max_weight
    self.n = len(self.weights)
    self.wt = [x.weight for x in self.weights]
    self.val = [x.value for x in self.weights]
    self.K = [[0 for w in range(self.W + 1)] for i in range(self.n + 1)]
    
  def run(self):
    self.init()
    W, n, wt, val, K = self.W, self.n, self.wt, self.val, self.K
    
    for i in range(n + 1):
      for w in range(W + 1):
        if i == 0 or w == 0:
          K[i][w] = 0
        elif wt[i - 1] <= w:
          K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
        else:
          K[i][w] = K[i - 1][w]
 
    ret = K[n][W]
    
    '''Debug
    for x in K:
      print(x)
    '''
    '''
    #Which weights are used Uncomment if uneeded
    res = ret
    ret = [ret]
    
    w = W
    for i in range(n, 0, -1):
      if res <= 0:
        break
      if res == K[i - 1][w]: #If comparing floats use math.isclose()
        continue
      else:
        ret.append(i - 1)
        res = res - val[i - 1]
        w = w - wt[i - 1]
    '''
    return ret #If not which weights used, just the best value, else first number is the weight, the next numbers are the weights used

class Weight:
  def __init__(self, weight, value):
    self.weight = weight
    self.value = value


datatable = file_reading()
# datatable = input_reading()
data = iter(datatable)

for i in range(next(data)):
  _ = next(data).split()
  maxWeight = int(_[0])
  knapsack = Knapsack(maxWeight)
  for j in range(int(_[1])):
    weight = next(data).split()
    knapsack.addWeight(Weight(int(weight[0]),int(weight[1]))) #Weight, Value

  answer = knapsack.run()
  print(answer)

