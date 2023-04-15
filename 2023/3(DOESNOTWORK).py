numMembers = int(input())
answer = []
longestSequence = 0
for i in range(numMembers):
    answer.append(0)
for i in range(len(answer)):
    lowestZero = answer.index(0)
    for j in range(lowestZero, len(answer)):
        if answer[j] == 0:
            longestSequence += 1
        else:
            lowestZero = answer.index(0, lowestZero)

for i in range(numMembers):
    if (longestSequence) % 2 != 0:
        answer[int(((1 + longestSequence) / 2))] = i
    else:
        answer[int(((longestSequence) / 2))] = i