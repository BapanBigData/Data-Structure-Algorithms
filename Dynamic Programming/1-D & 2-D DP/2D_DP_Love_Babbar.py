import math

## 0/1 Knapsack Problem:
def knapsack_problem(weights: list, costs: list, W: int):
    
    def solve_memo(memo, i, W):
        ## base case
        if i == 0:
            if (W-weights[i]) >= 0:
                return costs[i]
            else:
                return 0
        
        ## check if the state is already computed
        if memo[i][W] is not None:
            return memo[i][W]
        
        ## for the current element i, we have two options
        ## either include that element or exclude it
        incl = 0
        if (W-weights[i]) >= 0:
            incl = costs[i] + solve_memo(memo, i-1, W-weights[i])
            
        excl = 0 + solve_memo(memo, i-1, W)
        
        memo[i][W] = max(incl, excl)
        
        return memo[i][W]
    
    def solve_tabulation(W, n):
        ## initializing the dp array
        dp = [[None]*(W+1) for _ in range(n)]
        
        ## base case
        for w in range(W+1):
            dp[0][w] = costs[0] if (w-weights[0]) >= 0 else 0
        
        for i in range(1, n):
            for w in range(W+1):
                incl, excl = 0, 0
                if (w-weights[i]) >= 0:
                    incl = costs[i] + dp[i-1][w-weights[i]]
                excl = 0 + dp[i-1][w]
                
                dp[i][w] = max(incl, excl)
                
        return dp[n-1][W]
    
    def solve_space_optimal(W, n):
        ## initializing prev and curr arrays
        prev = [None] * (W+1)
        curr = [None] * (W+1)
        
        for w in range(W+1):
            prev[w] = costs[0] if (w-weights[0]) >= 0 else 0
        
        for i in range(1, n):
            for w in range(W+1):
                incl, excl = 0, 0
                if (w-weights[i]) >= 0:
                    incl = costs[i] + prev[w-weights[i]]
                excl = 0 + prev[w]
                
                curr[w] = max(incl, excl)  
                
            prev = curr[:]
        
        return prev[W]
        
    
    n = len(weights)
    
    ## initializing the memo array
    memo = [[None]*(W+1) for _ in range(n)]
    solve_memo(memo, n-1, W)
    
    tab = solve_tabulation(W, n)
    opt = solve_space_optimal(W, n)
    
    return memo[n-1][W], tab, opt

# W = 1000
# # weights = [1, 2, 4, 5]
# # values = [5, 4, 8, 6]
# values = [89, 90, 95, 100, 90, 79, 50, 10]
# weights = [123, 154, 258, 354, 365, 150, 95, 195]
# memo, tab, opt = knapsack_problem(weights, values, W)
# print(memo)
# print(tab)
# print(opt)
# for e in memo:
#     print(e)
# print()
# for f in tab:
#     print(f)
##---------------------------------------------------------------------------------------------------------
## Maximal Square: Largest Square Area In Matrix
def maximal_square(mat):
    
    def solve(i, j, maxi):
        ## base case
        if i >= len(mat) or j >= len(mat[0]):
            return 0
        
        move_right = solve(i, j+1, maxi)
        move_down = solve(i+1, j, maxi)
        move_diagonal = solve(i+1, j+1, maxi)
        
        if mat[i][j] == 1:
            ans = 1 + min(move_right, move_down, move_diagonal)
            maxi[0] = max(maxi[0], ans)
            return ans
        else:
            return 0
    
    def solve_memo(memo, i, j, maxi):
        ## base case
        if i >= len(mat) or j >= len(mat[0]):
            return 0
        
        ## check if the state is already computed
        if memo[i][j] is not None:
            return memo[i][j]
        
        move_right = solve_memo(memo, i, j+1, maxi)
        move_down = solve_memo(memo, i+1, j, maxi)
        move_diagonal = solve_memo(memo, i+1, j+1, maxi)
        
        if mat[i][j] == 1:
            memo[i][j] = 1 + min(move_right, move_down, move_diagonal)
            maxi[0] = max(maxi[0], memo[i][j])
            return memo[i][j]
        else:
            memo[i][j] = 0
            return memo[i][j]
        
    def solve_tabulation(mat):
        n, m = len(mat), len(mat[0])
        
        ## initializing the dp array
        dp = [[None]*(m+1) for _ in range(n+1)]
        
        ## base case
        for j in range(m+1):
            dp[n][j] = 0
        
        for i in range(n+1):
            dp[i][m] = 0
        
        ## initializing the maxi var
        maxi = 0
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                move_right = dp[i][j+1]
                move_down = dp[i+1][j]
                move_diagonal = dp[i+1][j+1]
                
                if mat[i][j] == 1:
                    dp[i][j] = 1 + min(move_right, move_down, move_diagonal)
                    maxi = max(maxi, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return maxi
    
    def solve_space_optimal(mat):
        n, m = len(mat), len(mat[0])
        
        maxi = 0
        
        ## initializing current raw and next row
        curr = [None] * (m+1)
        curr[m] = 0
        nxt = [0] * (m+1) 
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                move_right = curr[j+1]
                move_down = nxt[j]
                move_diagonal = nxt[j+1]
                
                if mat[i][j] == 1:
                    curr[j] = 1 + min(move_right, move_down, move_diagonal)
                    maxi = max(maxi, curr[j])
                else:
                    curr[j] = 0
                    
            nxt = curr[:]
        
        return maxi         
        
    # maxi = [0]
    # solve(0, 0, maxi)
    # return maxi[0]
    
    n, m = len(mat), len(mat[0])
    maxi = [0]
    
    ## initializing the memo array
    memo = [[None]*(m) for _ in range(n)]
    solve_memo(memo, 0, 0, maxi)
    
    tab = solve_tabulation(mat)
    opt = solve_space_optimal(mat)
    
    return maxi[0], tab, opt

mat = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1], 
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0]
]

mat1 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
# memo, tab, opt = maximal_square(mat1)
# print(memo)
# print(tab)
# print(opt)
# for e in memo:
#     print(e)
# print(res)
# for f in dp:
#     print(f)
# print(tab)
##--------------------------------------------------------------------------------------------------
## Minimum Score Triangulation Of Polygon:
def min_score_triangulation(values: list):
    
    def solve_memo(memo, i, j):
        ## base case
        if i+1 == j:
            memo[i][j] = 0
            return memo[i][j]
        
        ## check if the state is already computed
        if memo[i][j] != -1:
            return memo[i][j]
        
        ans = math.inf
        for k in range(i+1, j):
            f = values[i]*values[k]*values[j] + solve_memo(memo, i, k) + solve_memo(memo, k, j)
            ans = min(ans, f)
        
        memo[i][j] = ans
        
        return memo[i][j]
    
    
    def solve_tabulation(n):
        ## initializing the dp array
        dp = [[-1]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                ## base case
                if j == i+1:
                    dp[i][j] = 0
                else:
                    ans = math.inf
                    for k in range(i+1, j):
                        f = values[i]*values[k]*values[j] + dp[i][k] + dp[k][j]
                        ans = min(ans, f)
                            
                    dp[i][j] = ans
        
        return dp[0][n-1]
    
    n = len(values)
    
    ## initializing the memo array
    memo = [[-1]*n for _ in range(n)]
    solve_memo(memo, 0, n-1)
    
    tab = solve_tabulation(n)
    
    return memo[0][n-1], tab

# values = [1, 3, 1, 4, 1, 5, 2, 6, 7, 9, 1, 5, 7, 1, 2, 3, 4, 5, 9, 8, 7, 6, 4, 3, 1, 3, 5, 8, 1, 4]
# memo, tab = min_score_triangulation(values)
# print(memo)
# print(tab)
# for e in memo:
#     print(e)
# print()
# for f in tab:
#     print(f)
##--------------------------------------------------------------------------------------------
## Minimum Sideway Jump:
def min_sideway_jump(obstacles: list):
    
    def solve_memo(memo, pos, currlane, n):
        ## base case
        if pos == n:
            memo[pos][currlane] = 0
            return memo[pos][currlane]
        
        ## check if the state is already computed
        if memo[pos][currlane] is not None:
            return memo[pos][currlane]
        
        jump = 0
        if obstacles[pos+1] != currlane:
            ## go straight
            jump += 0 + solve_memo(memo, pos+1, currlane, n)
        else:
            ## S.W jump
            ans = math.inf
            for i in range(1, 4):
                if currlane != i and obstacles[pos] != i:
                    ## update the jump
                    ans = min(ans, 1 + solve_memo(memo, pos, i, n))
            jump += ans
        
        memo[pos][currlane] = jump
        
        return memo[pos][currlane]
    
    def solve_tabulation(n):
        ## initializing the dp array
        dp = [[None]*4 for _ in range(n)]
        
        ## base case
        dp[n-1][0] = 0
        dp[n-1][1] = 0
        dp[n-1][2] = 0
        dp[n-1][3] = 0
        
        for pos in range(n-2, -1, -1):
            for currlane in range(1, 4):
                if obstacles[pos+1] != currlane:
                    ## go straight
                    dp[pos][currlane] = 0 + dp[pos+1][currlane]
                else:
                    ## S.W jump
                    ans = math.inf
                    for i in range(1, 4):
                        if currlane != i and obstacles[pos] != i:
                            ## update the jump
                            ans = min(ans, 1 + dp[pos+1][i])
                    dp[pos][currlane]= ans        
        
        return min(dp[0][2], 1 + dp[0][1], 1 + dp[0][3])
    
    def solve_optimal_space(n):
        ## initializing the curr and nxt array
        curr = [None] * 4
        nxt = [0] * 4
        
        for pos in range(n-2, -1, -1):
            for currlane in range(1, 4):
                if obstacles[pos+1] != currlane:
                    ## go straight
                    curr[currlane] = 0 + nxt[currlane]
                else:
                    ## S.W jump
                    ans = math.inf
                    for i in range(1, 4):
                        if currlane != i and obstacles[pos] != i:
                            ## update the jump
                            ans = min(ans, 1 + nxt[i])
                            
                    curr[currlane]= ans
            
            nxt = curr[:]
        
        return min(nxt[2], 1 + nxt[1], 1 + nxt[3])
        
    
    n = len(obstacles)
    
    # ## initializing the memo array
    # memo = [[None]*4 for _ in range(n)]
    # solve_memo(memo, 0, 2, n-1)
    
    tab = solve_tabulation(n)
    opt = solve_optimal_space(n)
    
    return opt, tab

# obstacles = [0,2,1,0,3,0]
# res = min_sideway_jump(obstacles)
# print(res)
# print(jump)
# for e in memo:
#     print(e)
    
# print()

# for f in tab:
#     print(f)
##--------------------------------------------------------------------------------------------------------------
## Reducing Dishes:
def max_satisfaction(satisfaction: list):
    
    satisfaction.sort()
    
    def solve_memo(memo, i, t, n):
        ## base case
        if i == n:
            return 0
        
        ## check if the state is already computed
        if memo[i][t] is not None:
            return memo[i][t]
        
        ## for each i there is a two option, either incl or excl
        incl = satisfaction[i]*(t) + solve_memo(memo, i+1, t+1, n)
        excl = 0 + solve_memo(memo, i+1, t, n)
        
        memo[i][t] = max(incl, excl)
        
        return memo[i][t]
    
    def solve_tabulation(satisfaction, n):
        
        ## initializing the dp array
        dp = [[-math.inf]*(n+2) for _ in range(n+1)]
        
        ## base case
        for time in range(n+2):
            dp[n][time] = 0
        
        for i in range(n-1, -1, -1):
            for t in range(n, 0, -1):
                incl = satisfaction[i]*(t) + dp[i+1][t+1]
                excl = 0 + dp[i+1][t]
                
                dp[i][t] = max(incl, excl)
        
        return dp[0][1]
    
    def solve_space_optimal(n):
        ## initializing the curr and nxt arrays
        curr = [-math.inf] * (n+2)
        nxt = [0] * (n+2)
        
        for i in range(n-1, -1, -1):
            for t in range(n, 0, -1):
                incl = satisfaction[i]*(t) + nxt[t+1]
                excl = 0 + nxt[t]
                
                curr[t] = max(incl, excl)
            
            nxt = curr[:]
        
        return nxt[1]
    
    n = len(satisfaction)
    
    ## initializing the memo array
    memo = [[None]*(n+1) for _ in range(n)]
    solve_memo(memo, 0, 1, n)
    
    tab = solve_tabulation(satisfaction, n)
    opt = solve_space_optimal(n)
    
    return tab, opt

satisfaction = [4,3,2]
tab, opt = max_satisfaction(satisfaction)
print(tab)
print(opt)
# print(res)
# for e in memo:
#     print(e)

# for f in tab:
#     print(f)