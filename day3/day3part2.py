import re

total = 0
do = True

with open("day3.txt", "r") as file:
    
    f = file.read()
    # found the pattern on https://github.com/tomfran/aoc-24
    pattern = r"(mul|do|don\'t)\((\d+,\d+|)\)"

    matches = re.findall(pattern, f)
    for x in matches:
        if x[0] == "do":
            do = True
        elif x[0] == "don't":
            do = False
        nums = x[1].split(",")
        if do and (3 >= len(nums[0]) >= 1) and (3 >= len(nums[1]) >= 1):
            total += int(nums[0]) * int(nums[1])

print(total)