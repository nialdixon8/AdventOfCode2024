leftList = []
rightList = []
total = 0


with open("day1.txt", "r") as file:
    for line in file:
        line = line.split()
        leftList.append(int(line[0]))
        rightList.append(int(line[1]))

    leftList.sort()
    rightList.sort()

    for i in range(0, len(leftList)):
        total += abs(leftList[i]-rightList[i])

print(total)

