## ---- Backtracking ----
## N Queens 

def is_safe(mat, row, col):
    ## column
    for r in range(row):
        if mat[r][col] == 1:
            return False
        
    ## left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if mat[r][c] == 1:
            return False
        r -= 1
        c -= 1
        
    ## right diagonal
    r, c = row, col
    while r >= 0 and c < len(mat[col]):
        if mat[r][c] == 1:
            return False
        r -= 1
        c += 1
    
    return True    

def can_n_queens_placed_solver(mat, row, n):
    if row == n:
        for e in mat:
            print(e)
        print()
        return True
    
    for col in range(len(mat[row])):
        ## check whether we can place the queen at (row, col)
        if is_safe(mat, row, col):
            mat[row][col] = 1
            success = can_n_queens_placed_solver(mat, row+1, n)
            if success:
                return True
            
            ## backtrack
            mat[row][col] = 0
            
    ## after all columns have been checked in the current row       
    return False
            

def can_n_queens_placed(n: int) -> bool:
    mat = [[0]*n for _ in range(n)]
    
    return can_n_queens_placed_solver(mat, 0, n)
## ---------------------------------------------------------------------------------------------------------

def n_queens_all_configs_solver(mat, row, n):
    if row == n:
        for e in mat:
            print(e)
        print()
        return 1
    
    cnt = 0
    
    for col in range(len(mat[row])):
        if is_safe(mat, row, col):
            mat[row][col] = 1
            cnt += n_queens_all_configs_solver(mat, row+1, n)
            
            ## backtrack
            mat[row][col] = 0
            
    return cnt

def n_queens_all_configs(n: int) -> int:
    mat = [[0]*n for _ in range(n)]
    
    return n_queens_all_configs_solver(mat, 0, n)

print(n_queens_all_configs(8))