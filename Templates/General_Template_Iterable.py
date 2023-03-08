true = True
false = False

def fileReading():
  f = open("letter.in", 'r')
  num = int(f.readline().strip())
  datatable = [f.readline().strip() for _ in range(num)]
  datatable.insert(0,num)
  f.close()
  return datatable

def inputReading():
  num = int(input().strip())
  datatable = [input().strip() for _ in range(num)]
  datatable.insert(0,num)
  return datatable

# datatable = fileReading()
datatable = inputReading()

data = iter(datatable)

for i in range(next(data)):
  
  print(next(data))
