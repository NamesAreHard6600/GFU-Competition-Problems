count = int(input())
data = []
numberCorrect = 0
for i in range(count):
    data.append(input())
for j in range(len(data)):
    if data[i].lower().find("minor") != -1:
        location = data[i].lower().find("minor")
        if data[i].lower().find("minor", location + 5):
            print("It\'s over Vee Valdee! I have the high ground!")
        else:
            print("You underestimate my music!")