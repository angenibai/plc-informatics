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
        return (x, y+distance)
    if direction == "E":
        return (x+distance, y)
    if direction == "S":
        return (x, y-distance)
    if direction == "W":
        return (x-distance, y)

instructions = [x for x in input().split(", ")]

x = 0
y = 0
direction = "N"

for instruction in instructions:
    turn_direction = instruction[0]
    distance = int(instruction[1:])

    direction = turn(direction, turn_direction)
    x, y = move(x, y, direction, distance)

print(abs(x) + abs(y))