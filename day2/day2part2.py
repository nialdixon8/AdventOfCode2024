total = 0

with open("day2.txt", "r") as file:
    for line in file:
        line = line.split()
        possible = False
        for i in range(-1, len(line)):
            if i == -1:
                continue
            else:
                val = line.pop(i)
            increasing = True
            decreasing = True
            l = 1
            r = len(line) - 2
            while (increasing or decreasing) and (l < len(line) and r >= 0):
                if (int(line[l]) > int(line[l-1])) and int(line[l]) - int(line[l-1]) <= 3:
                    l+=1
                else:
                    increasing = False
                if (int(line[r+1]) < int(line[r])) and int(line[r]) - int(line[r+1]) <= 3:
                    r-=1
                else:
                    decreasing = False

            if increasing or decreasing:
                possible = True
            if i != -1:
                line.insert(i, val)
        if possible:
            total += 1


print(total)