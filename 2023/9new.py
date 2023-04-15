def timetofloat(time):
    return float(time[0] + "." + time[1])

def read_input():
    fl = input().strip().split(" ")
    n = int(fl[0])
    q = int(fl[1])
    events = []
    times = []
    for i in range(n):
        events.append(input().strip())
    for i in range(q):
        time = input().strip().split(":")
        total = timetofloat(time)
        times.append(float(total))
    sorted = []
    for x in range(len(events)):
        max = 0
        maxindex = 0
        for y in range(len(events)):
            if timetofloat(events[y].split(" ")[1].split(":")) > max:
                max = timetofloat(events[y].split(" ")[1].split(":"))
                maxindex = y
        sorted.insert(0, events[maxindex])
        events.pop(maxindex)
    events = sorted
    for time in times:
        if time < timetofloat(events[0].split(" ")[1].split(":")):
            print("Why Don’t You Make Like a Tree and Get Outta Here?")
        else:
            highest = 0
            while timetofloat(events[highest].split(" ")[1].split(":")) <= time and highest + 1 < len(events):
                highest += 1
            string = ""
            for i in range(highest):
                string += events[i].split(" ")[0] + " "
            if time == timetofloat(events[len(events) - 1].split(" ")[1].split(":")):
                string += events[len(events) - 1].split(" ")[0]
            print(string.strip())

read_input()

