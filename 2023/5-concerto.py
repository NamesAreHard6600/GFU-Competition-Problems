#Written by Jacob

count = int(input())
data = []
numberCorrect = 0
for i in range(count):
    data.append(input())
for j in range(count):
    if data[j].count("minor") > 2:
        print("It\'s over Vee Valdee! I have the high ground!")
    else:
        print("You underestimate my music!")
