#Line 17
def read(t):
  f = None
  if t == "file":
    f = open(FILENAME, 'r')
    READ = f.readline
  else:
    READ = input
  #Formatting Starts Here
  num = int(READ().strip())
  datatable = [input().strip() for _ in range(num)]
  #Formatting Ends Here
  if f: 
    f.close()
  return datatable

FILENAME = "6.in"
datatable = read("")

FILENAME = "letter.in"
READ = file_reading
#READ = input_reading

datatable = READ()

for itr in datatable:
  print(itr)
