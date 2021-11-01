IN = open("day3.1.in", "r")

def is_triangle(sides):
    sides.sort()
    return sides[0] + sides[1] > sides[2]

all_lines = IN.readlines()
all_lines = [[int(x) for x in line.split()] for line in all_lines]
n = len(all_lines)
count = 0

for row in range(0, n, 3):
    for col in range(3):
        if is_triangle([all_lines[row][col], all_lines[row+1][col], all_lines[row+2][col]]):
            count += 1

print(count)

IN.close()



