def turn(cur, turn):
    lookup = {
        "N": ["W", "E"],
        "E": ["N", "S"],
        "S": ["E", "W"],
        "W": ["S", "N"]
    }

    i = 0 if turn == "L" else 1
    return lookup[cur][i]

def move(x, y, direction, distance):
    locations = []
    if direction == "N":
        for new_y in range(y+1, y+distance+1):
            locations.append((x, new_y))
        return locations
    if direction == "E":
        for new_x in range(x+1, x+distance+1):
            locations.append((new_x, y))
        return locations
    if direction == "S":
        for new_y in range(y-1, y-distance-1, -1):
            locations.append((x, new_y))
        return locations
    if direction == "W":
        for new_x in range(x-1, x-distance-1, -1):
            locations.append((new_x, y))
        return locations


"""
R4
0,0 -> 4,0
0,0 -> (1,0), (2,0), (3,0), (4,0)

Go north for 3 units
0,0 -> [(0,1), (0,2), (0,3)]

Go east for 3 units
0,0 -> [(1,0), (2,0), (3,0)]

Go south for 3 units
0,0 -> [(0,-1), (0,-2), (0,-3)]

locations = []
locations.append((0,1))
locations = [(0,1)]

visited = [(0,0)] # list of all locations visited previously
"""

instructions = input().split(", ")

x = 0
y = 0
direction = "N"

visited = set([(0,0)]) # list of every location we visit

count = 0

for instruction in instructions:
    turn_direction = instruction[0]
    distance = int(instruction[1:])

    direction = turn(direction, turn_direction)
    locations = move(x, y, direction, distance)

    for new_x, new_y in locations:
        if (new_x, new_y) in visited:
            # this is a repeated location
            # print(abs(new_x) + abs(new_y)) # this is our answer
            count += 1
        else:
            # new location
            visited.add((new_x, new_y))

    x, y = locations[-1]

print(count)