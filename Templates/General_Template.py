true = True
false = False

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

for iteration in datatable:
  
  print(iteration)
