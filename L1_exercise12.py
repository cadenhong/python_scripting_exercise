'''
Football Points

Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

wins get 3 points
draws get 1 point
losses get 0 points

Examples
football_points(3, 4, 2) ➞ 13
football_points(5, 0, 2) ➞ 15
football_points(0, 0, 1) ➞ 0

Notes
Inputs will be numbers greater than or equal to 0.
'''

def football_points(wins, draws, losses):
    if wins < 0 or draws < 0 or losses < 0:
        return "Invalid points! Must be greater than or equal to 0!"
    else:
        points =  (wins * 3) + (draws * 1) +  (losses * 0)
        return points

print(football_points(3, 4, 2))
print(football_points(5, 0, 2))
print(football_points(0, 0, 1))