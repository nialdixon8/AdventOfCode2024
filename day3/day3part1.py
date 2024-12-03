import re

total = 0

with open("day3.txt", "r") as file:
    for line in file:
        mults = re.findall("mul\([0-9]+,[0-9]+\)", line)
        for x in mults:
            nums = re.findall("[0-9]+", x)
            total += (int(nums[0]) * int(nums[1]))

print(total)