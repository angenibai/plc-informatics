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
    if direction == "N":
        return [(x, y+i) for i in range(1, distance+1)]
    if direction == "E":
        return [(x+i, y) for i in range(1, distance+1)]
    if direction == "S":
        return [(x, y-i) for i in range(1, distance+1)]
    if direction == "W":
        return [(x-i, y) for i in range(1, distance+1)]

instructions = [x for x in input().split(", ")]
visited = set()

x = 0
y = 0
direction = "N"
visited.add((x,y))
found = False

for instruction in instructions:
    turn_direction = instruction[0]
    distance = int(instruction[1:])

    direction = turn(direction, turn_direction)
    coords = move(x, y, direction, distance)
    for coord in coords:
        if coord in visited:
            found = True
            found_x = coord[0]
            found_y = coord[1]
            break
        visited.add(coord)

    if found:
        print(f"Overlap at ({found_x}, {found_y})")
        print(abs(found_x) + abs(found_y))
        break

    x = coords[-1][0]
    y = coords[-1][1]