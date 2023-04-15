

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
        


def is_common(nums, num):
    common = True
    for number in nums:
        if (num / number) % 1 != 0:
            common = False
    return common

def lcm(nums):
    nums = nums.split(" ")
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    largest = 0
    for num in nums:
        if num > largest:
            largest = num
    x = 1
    while is_common(nums, largest * x) != True:
        x += 1
    print(largest * x)

table = read_input()
for item in table:
    lcm(item)

#all gnomes have a pace of Gi
#at each int multiple of Gi the gnome(G) will do a dance move
#given a set of gnomes, what is the first point in time when all perform simultaneous dance move
