'''
Basketball Points

You are counting points for a basketball game, given the amount of 3-pointers scored and 2-pointers scored, find the final points for the team and return that value ([2 -pointers scored, 3-pointers scored]).

Examples
points(1, 1) ➞ 5
points(7, 5) ➞ 29
points(38, 8) ➞ 100
'''

def points(twoPointers, threePointers):
    return (twoPointers*2) + (threePointers*3)

print(points(1, 1))
print(points(7, 5))
print(points(38, 8))