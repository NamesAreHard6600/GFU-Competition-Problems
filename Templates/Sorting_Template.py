true = True
false = False
datatable = []

def sortFunc(item): #NEEDS: how it is orgainzied
  return (item[0],item[1],item[2])

def fileReading():
  datatable = []
  f = open("letter.in", 'r')
  num = int(f.readline().strip())
  datatable = [f.readline().strip() for _ in range(num)]
  f.close()
  return datatable

def inputReading():
  datatable = []
  num = int(input().strip())
  datatable = [input().strip() for _ in range(num)]
  return datatable

datatable = fileReading()
# datatable = inputReading()

for i in range(len(datatable)): #This could be list comprehension, but if there's a lot going on it doesn't help
  datatable[i] = datatable[i].split(",") #NEEDS: some sort of split
  
finalTable = sorted(datatable,key=sortFunc)

for iter in finalTable:
  print(iter[0] + " - (" + iter[1] + "/" + iter[2] + ")") #NEEDS: how it is orgainzied