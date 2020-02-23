print("input sudoku: ")
grid = []
for i in range(9): 
    grid.append([int(e) for e in list(input()) if e != " "]) # input with/without space

def print2dlist(ls):
    for i in range(len(ls)):
        print(ls[i])

def solver():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                nums = set(range(10))
                # check 3x3 grid
                x = (row // 3) * 3
                y = (col // 3) * 3
                for i in range(3):
                    for j in range(3):
                        nums.discard(grid[x + i][y + j])
                # check row and col
                for i in range(9):
                    nums.discard(grid[row][i])
                    nums.discard(grid[i][col])
                # remove 0
                nums.discard(0)
                # try all 
                for e in nums:
                    grid[row][col] = e
                    solver()
                    grid[row][col] = 0
                return
    print2dlist(grid)
    input("Continue?")
                
solver()   