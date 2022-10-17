'''
Minesweeper I — Grid

This challenge is based on the game Minesweeper.

Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot. Return a list where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).

Examples
num_grid([
["-", "-", "-", "-", "-"],
["-", "-", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "-", "-", "-", "-"],
["-", "-", "-", "-", "-"]
]) ➞ [
["0", "0", "0", "0", "0"],
["0", "1", "1", "1", "0"],
["0", "1", "#", "1", "0"],
["0", "1", "1", "1", "0"],
["0", "0", "0", "0", "0"],
]

num_grid([
["-", "-", "-", "-", "#"],
["-", "-", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "-", "-", "-", "-"],
["#", "-", "-", "-", "-"]
]) ➞ [
["0", "0", "0", "1", "#"],
["0", "1", "1", "2", "1"],
["0", "1", "#", "1", "0"],
["1", "2", "1", "1", "0"],
["#", "1", "0", "0", "0"]
]

num_grid([
["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"]
]) ➞ [
["1", "1", "2", "#", "#"],
["1", "#", "3", "3", "2"],
["2", "4", "#", "2", "0"],
["1", "#", "#", "2", "0"],
["1", "2", "2", "1", "0"],
]
'''
def num_grid(grid):
    converted = grid
    for row in range(len(grid)):
        ctr = 0
        for col in range(len(grid[row])):
            if grid[row][col] == "#":
                converted[row][col] = "#"
            else:
                # if (row == 0 and col == 0) or (row == 0 and col == 4) or (row == 4 and col == 0) or (row == 4 and col == 4):
                #     continue
                if row == 0 or col == 0 or row == 4 or col == 4:
                    continue
                else:
                    # if row == 0 or col == 0:
                    #     if grid[row][col+1] == "#": ctr += 1
                    #     if grid[row+1][col] == "#": ctr += 1
                    #     if grid[row+1][col+1] == "#": ctr += 1
                    # elif row == 4 or col == 4:
                    #     if grid[row][col-1] == "#": ctr += 1
                    #     if grid[row-1][col] == "#": ctr += 1
                    #     if grid[row-1][col-1] == "#": ctr += 1
                    # else:
                        if grid[row][col+1] == "#": ctr += 1
                        if grid[row][col-1] == "#": ctr += 1
                        if grid[row+1][col] == "#": ctr += 1
                        if grid[row-1][col] == "#": ctr += 1
                        if grid[row-1][col-1] == "#": ctr += 1
                        if grid[row+1][col+1] == "#": ctr += 1
            converted[row][col] = str(ctr)
    return converted

        #     else:
        #         if grid[x].index("-") == 0 or i == 0:
        #             if grid[x][i+1] == "#" or grid[x+1][i] == "#" or grid[x+1][i+1] == "#":
        #                 ctr += 1
        #         elif grid[x].index("-") == 4 or i == 4: # If last row or last col
        #             if grid[x][i-1] == "#" or grid[x-1][i] == "#" or grid[x-1][i-1] == "#":
        #                 ctr += 1
        #         else:                           # If in between
        #             if grid[x][i+1] == "#" or grid[x][i-1] == "#" or grid[x+1][i] == "#" or grid[x-1][i] == "#" or grid[x-1][i-1] == "#" or grid[x+1][i+1] == "#":
        #                 ctr += 1
        # x += 1

    # for row in range(len(grid)):
    #     for col in range(len(grid[row])):
    #         ctr = 0
    #         if grid[row][col] == "#":
    #             print(grid[row][col])#converted[row][col] = "#"
    #         elif grid[row][col] == "-":
    #             if row == 0 or col == 0:        # If first row or first col
    #                 if grid[row][col+1] == "#" or grid[row+1][col] == "#" or grid[row+1][col+1] == "#":
    #                     ctr += 1
    #             elif row == int(len(grid) - 1) or col == int(len(grid) - 1): # If last row or last col
    #                 if grid[row][col-1] == "#" or grid[row-1][col] == "#" or grid[row-1][col-1] == "#":
    #                     ctr += 1
    #             else:                           # If in between
    #                 if grid[row][col+1] == "#" or grid[row][col-1] == "#" or grid[row+1][col] == "#" or grid[row-1][col] == "#" or grid[row-1][col-1] == "#" or grid[row+1][col+1] == "#":
    #                     ctr += 1
    #         converted[row][col] = str(ctr)
    # return converted

print(num_grid([
["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"]
]))

'''
Sample Code:

def num_grid(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == '-':
                lst[i][j] = str(sum(1 for u in range(i-1,i+2) for v in range(j-1,j+2) if 0 <= v < len(lst[i]) and 0 <= u < len(lst) and lst[u][v] == '#'))
    return lst
'''