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
  datatable = [READ().strip() for _ in range(num)]
  #Formatting Ends Here
  if f: 
    f.close()
  return datatable

FILENAME = "#.in"
datatable = read("file")

for itr in datatable:
  print(itr)
