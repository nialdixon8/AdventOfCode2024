leftList = []
rightList = []
total = 0
with open("day1.txt", "r") as file:
    for line in file:
        line = line.split()
        leftList.append(int(line[0]))
        rightList.append(int(line[1]))
    

for x in leftList:
    similarity = rightList.count(x) * x
    total += similarity

print(total)