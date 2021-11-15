"""
Start from bottom left - find shortest path to top right
"""

IN = open('phonein.txt', 'r')

L = []
F = []
R = []

n = int(IN.readline())

for i in range(n-1):
    l, f, r = map(int, IN.readline().split(" "))
    L.append(l)
    F.append(f)
    R.append(r)

f = int(IN.readline())
F.append(f)

def find_left(prev_left, prev_right, level):
    """
    Find the shortest time you can get to the left side of the given level
    """
    from_left = prev_left + L[level-1] + F[level]
    from_right = prev_right + R[level-1]
    return min(from_left, from_right)

def find_right(prev_left, prev_right, level):
    """
    Find the shortest time you can get to the right side of the given level
    """
    from_left = prev_left + L[level-1]
    from_right = prev_right + R[level-1] + F[level]
    return min(from_left, from_right)

# Starting on the left side of the bottom level
prev_left = 0
# Crossing the bottom floor to get the shortest time to reach the right side of the bottom level
prev_right = F[0]
for level in range(1,n):
    # DP approach - finding shortest times to left and right sides of each level
    cur_left = find_left(prev_left, prev_right, level)
    cur_right = find_right(prev_left, prev_right, level)
    prev_left, prev_right = cur_left, cur_right

# Reach the end at right side of top level
ans = prev_right

OUT = open('phoneout.txt', 'w')
print(ans, file=OUT)

IN.close()
OUT.close()