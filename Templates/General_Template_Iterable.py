#Line 16
def file_reading():
  f = open(FILENAME, 'r')
  num = int(f.readline().strip())
  datatable = [f.readline().strip() for _ in range(num)]
  datatable.insert(0,num)
  f.close()
  return datatable

def input_reading():
  num = int(input().strip())
  datatable = [input().strip() for _ in range(num)]
  datatable.insert(0,num)
  return datatable

FILENAME = "letter.in"
READ = file_reading
#READ = input_reading

datatable = READ()

data = iter(datatable)

for i in range(next(data)):
  print(next(data))
