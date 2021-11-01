IN = open("day3.1.in", "r")

all_lines = IN.readlines()
count = 0

for line in all_lines:
    nums = [int(x) for x in line.split()]
    nums.sort()
    if nums[0] + nums[1] > nums[2]:
        count += 1

print(count)

IN.close()
