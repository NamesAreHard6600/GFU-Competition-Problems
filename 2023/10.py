#pebble game
#must drag piano across path of 1 meter long strips of road
#piano is 2 meters long
#cannot move over a gap longer than 2 meters
#find minimum number of meter long strips of road that he must fill it to safely move the piano
def numpaved(road):
    total = 0
    gaps = []
    ongap = False
    currentgap = []
    for i in range(len(road)):
        if road[i] == ".":
            if not ongap:
                ongap = True
            currentgap.append(".")
        elif road[i] == "-":
            if ongap:
                ongap = False
                currentgap = []
                gaps.append(currentgap)
    if ongap:
        gaps.append(currentgap)
    for gap in gaps:
        if len(gap) > 2:
            total += int(len(gap) / 3)
    print(total)

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


            
                