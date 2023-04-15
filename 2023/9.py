#Line 16
def file_reading():
  f = open(FILENAME, 'r')
  nums = [int(x) for x in f.readline().strip().split()]
  datatable = [f.readline().strip() for _ in range(nums[0]+nums[1])]
  datatable.insert(0,nums)
  f.close()
  return datatable

def input_reading():
  nums = [int(x) for x in input().strip().split()]
  datatable = [input().strip() for _ in range(nums[0]+nums[1])]
  datatable.insert(0,nums)
  return datatable

def sortFunc(key):
  return key[1]

FILENAME = "9.in"
READ = file_reading
#READ = input_reading

datatable = READ()

data = iter(datatable)

nums = next(data)

#init
arr = []
for i in range(nums[0]):
  event = next(data).split()
  arr.append([event[0],int(event[1].replace(":",""))])
arr.sort(key=sortFunc)

#output
#print("02:13".replace(":",""))
#print(int("02:13".replace(":","")))
for i in range(nums[1]):
  time = int(next(data).replace(":",""))
  ret = []
  for x in arr:
    #print(time)
    if time>=x[1]:
      ret.append(x[0])
  if len(ret) == 0:
    print("Why Don’t You Make Like a Tree and Get Outta Here?")
  else:
    print(" ".join(ret))
