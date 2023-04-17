#Written By Calder
#pebble game
#must drag piano across path of 1 meter long strips of road
#piano is 2 meters long
#cannot move over a gap longer than 2 meters
#find minimum number of meter long strips of road that he must fill it to safely move the piano
def numpaved(road):
    r = []
    for tile in road:
        r.append(tile)
    x = 2
    total = 0
    if len(road) > 2:
        while x < len(r):
            if r[x] == "." and r[x - 1] == "." and r[x - 2] == ".":
                total += 1
                r[x] = "-"
            x += 1
        print(total)
    else:
        print(0)

def readinput():
    num = int(input().strip())
    table = []
    for i in range(num*2):
        line = input().strip()
        if not line.isnumeric():
            table.append(line)
    return table

table = readinput()
for road in table:
    numpaved(road)


            
                
