import math

def input_reading():
    datatable = []
    num = int(input().strip())
    datatable = [input().strip() for _ in range(num*2)]
    datatable.insert(0,num)
    return datatable

def part(x,y):
    if x == 0 or y == 0:
        return 0
    return int(x*y/math.gcd(x,y))

def lcm(arr):
    if len(arr) == 0:
        return 1
    if len(arr) == 1:
        return arr[0]
    ret = part(arr[0],arr[1])
    for x in arr[2:]:
        ret = part(ret,x)
    return ret


data = iter(input_reading())

for x in range(int(next(data))):
    next(data)
    arr = [int(x) for x in next(data).split()]
    print(lcm(arr))

