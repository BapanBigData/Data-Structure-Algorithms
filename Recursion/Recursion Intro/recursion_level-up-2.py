## -- backtracking --
## sudoku solver

def is_safe(mat, i, j, num, n):
    ## check in the row and column
    for k in range(n):
        if mat[i][k] == num or mat[k][j] == num:
            return False
    
    ## check in the sub-grid
    sx = (i // 3) * 3
    sy = (j // 3) * 3
    
    for x in range(sx, sx+3):
        for y in range(sy, sy+3):
            if mat[x][y] == num:
                return False
    
    return True
        

def can_sudoku_solve(mat, i, j, n) -> bool:
    ## base case
    if i == n:
        for e in mat:
            print(e)
        print()
        return True
    
    if j == n:
        return can_sudoku_solve(mat, i+1, 0, n)
    
    ## skip the pre-fill cells
    if mat[i][j] != 0:
        return can_sudoku_solve(mat, i, j+1, n)
    
    ## cell to be filled
    ## try out with all possibilities
    for num in range(1, n+1):
        if is_safe(mat, i, j, num, n):
            mat[i][j] = num
            solve_sub_problem = can_sudoku_solve(mat, i, j+1, n)
            
            if solve_sub_problem:
                return True
    
    ## if no option (num) works
    mat[i][j] = 0
    return False

## -----------------------------------------------------------------------------------------------------

def sudoku_solver(mat, i, j, n) -> None:
    ## base case
    if i == n:
        for e in mat:
            print(e)
        print()
        return 
    
    if j == n:
        return can_sudoku_solve(mat, i+1, 0, n)
    
    ## skip the pre-fill cells
    if mat[i][j] != 0:
        return can_sudoku_solve(mat, i, j+1, n)
    
    ## cell to be filled
    ## try out with all possibilities
    for num in range(1, n+1):
        if is_safe(mat, i, j, num, n):
            mat[i][j] = num
            can_sudoku_solve(mat, i, j+1, n)
    
    ## if no option (num) works
    mat[i][j] = 0
    
    return
    

n = 9
# mat = [
    
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]


# sudoku_matrix = [
    
#     [0, 0, 5, 0, 0, 1, 0, 8, 0],
#     [0, 1, 6, 0, 0, 2, 0, 0, 0],
#     [0, 0, 7, 0, 0, 0, 0, 4, 3],
#     [0, 0, 0, 8, 6, 0, 0, 3, 0],
#     [0, 3, 0, 0, 0, 0, 0, 2, 0],
#     [0, 2, 0, 0, 7, 5, 0, 0, 0],
#     [8, 7, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 3, 0, 0, 7, 9, 0],
#     [0, 9, 0, 6, 0, 0, 3, 0, 0]
# ]

# sudoku_matrix = [
    
#     [8, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 3, 0, 0, 8, 0, 0, 0, 4],
#     [2, 0, 0, 6, 0, 7, 0, 8, 0],
#     [0, 0, 0, 2, 7, 0, 4, 0, 0],
#     [4, 0, 0, 0, 0, 0, 0, 0, 3],
#     [0, 0, 9, 0, 3, 5, 0, 0, 0],
#     [0, 4, 0, 9, 0, 1, 0, 0, 7],
#     [7, 0, 0, 0, 4, 0, 0, 6, 0],
#     [0, 0, 8, 0, 0, 0, 0, 0, 9]
# ]

board = [
    [0, 1, 0, 4, 0, 0, 0, 0, 0],
    [7, 0, 5, 3, 0, 0, 0, 0, 0],
    [6, 3, 0, 0, 0, 9, 0, 0, 0],
    [3, 0, 0, 0, 5, 0, 0, 2, 0],
    [4, 0, 8, 0, 0, 0, 1, 0, 6],
    [0, 6, 0, 0, 3, 0, 0, 0, 7],
    [0, 0, 0, 6, 0, 0, 0, 7, 8],
    [0, 0, 0, 0, 0, 8, 3, 0, 9],
    [0, 0, 0, 0, 0, 3, 0, 5, 0]
]


print(can_sudoku_solve(board, 0, 0, n))
# sudoku_solver(sudoku_matrix, 0, 0, n)