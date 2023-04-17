#Written by Calder
import math

def read_input():
    table = []
    num = int(input().strip())
    for i in range(num * 2):
        table.append(input().strip())
    newtable = []
    for i in range(len(table)):
        if i % 2 != 0:
            newtable.append(table[i])
    return newtable

def find_lcm(nums):
    numbers = []
    for item in nums.split(" "):
        numbers.append(int(item))
    nums = numbers
    if len(nums) == 1:
        print(nums[0])
    else:
        x = 1
        lcm = nums[0]
        while x < len(nums):
            lcm = (lcm * nums[x]) // math.gcd(lcm, nums[x])
            x += 1
        print(lcm)
#all gnomes have a pace of Gi
#at each int multiple of Gi the gnome(G) will do a dance move
#given a set of gnomes, what is the first point in time when all perform simultaneous dance move
for set in read_input():
    find_lcm(set)
