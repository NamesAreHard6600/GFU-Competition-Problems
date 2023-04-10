#Line 16
def input_reading():
  datatable = []
  num = int(input().strip())
  datatable = [input().strip() for _ in range(num)]
  return datatable
  
def file_reading():
  datatable = []
  f = open(FILENAME, 'r')
  num = int(f.readline().strip())
  datatable = [f.readline().strip() for _ in range(num)]
  f.close()
  return datatable

FILENAME = "letter.in"
READ = file_reading
#READ = input_reading

datatable = READ()

for itr in datatable:
  print(itr)
