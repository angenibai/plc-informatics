"""
Maximise value of items chosen without exceeding the weight limit
"""

n = 5
limit = 10
weights = [0, 1, 2, 2, 3, 7]
values = [0, 50, 60, 65, 80, 110]

sub_problems = [[0 for i in range(limit+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, limit+1):
        weight = weights[i]
        value = values[i]
        # the first i-1 items with weight limit of j
        dont_take = sub_problems[i-1][j]
        
        # this item + first i-1 items with weight limit of j - current_weight
        if j - weight >= 0:
            take = value + sub_problems[i-1][j-weight]
        else:
            take = value
        
        # take the best option
        sub_problems[i][j] = max(take, dont_take)

    print(sub_problems[i])       

print(sub_problems[n][limit])