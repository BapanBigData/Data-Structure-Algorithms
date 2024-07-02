## Longest Common Subsequence
## Top-Down approach, which will return the length of LCS
def longest_common_subseqs_top_down_len(s1: str, s2: str) -> int:
    
    def top_down_dp(memo, i, j, n, m):
        ## base case
        if i == n or j == m:
            return 0
        
        ## check if the sate is already computed
        if memo[i][j] is not None:
            return memo[i][j]
        
        if s1[i] == s2[j]:
            memo[i][j] = 1 + top_down_dp(memo, i+1, j+1, n, m)
            return memo[i][j]
        
        op_1 = top_down_dp(memo, i+1, j, n, m)
        op_2 = top_down_dp(memo, i, j+1, n, m)
        
        memo[i][j] = max(op_1, op_2)
        
        return memo[i][j]
    
    n, m = len(s1), len(s2)
    i, j = 0, 0
    
    ## memo array of size (n X m)
    memo = [[None]*(m) for _ in range(n)]    
    top_down_dp(memo, i, j, n, m)
    
    return memo[0][0]


## Top-Down approach, which will return the LCS
def longest_common_subseqs_top_down(s1: str, s2: str) -> str:
    
    def top_down_dp(memo, i, j, n, m):
        ## base case
        if i == n or j == m:
            return ''
        
        ## check if the state is already computed
        if memo[i][j] is not None:
            return memo[i][j]
        
        if s1[i] == s2[j]:
            memo[i][j] = s1[i] + top_down_dp(memo, i+1, j+1, n, m)
            return memo[i][j]
        
        op_1 = top_down_dp(memo, i+1, j, n, m)
        op_2 = top_down_dp(memo, i, j+1, n, m)
        
        memo[i][j] = op_1 if len(op_1) > len(op_2) else op_2
        
        return memo[i][j]
    
    n, m = len(s1), len(s2)
    i, j = 0, 0
    
    ## memo array of size (n X m)
    memo = [[None]*(m) for _ in range(n)]    
    top_down_dp(memo, i, j, n, m) 
    
    return memo[0][0]


## Bottom-Up approach LCS len
def lcs_len_bottom_up(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)
    
    ## initializing the dp array
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    ## main logic
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                op_1 = dp[i-1][j]
                op_2 = dp[i][j-1]
                dp[i][j] = max(op_1, op_2)
    
    return dp[n][m]


# ## Bottom-Up approach LCS string
# def lcs_bottom_up(s1: str, s2: str) -> str:
#     n = len(s1)
#     m = len(s2)
    
#     ## initializing the dp array
#     dp = [['']*(m+1) for _ in range(m+1)]
    
#     ## main logic
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             if s1[i-1] == s2[j-1]:
#                 dp[i][j] = s1[i-1] + dp[i-1][j-1]  
#             else:
#                 op_1 = dp[i-1][j]
#                 op_2 = dp[i][j-1]
#                 dp[i][j] = op_1 if len(op_1) > len(op_2) else op_2
    
#     return dp[n][m]


# s1 = 'ABCDVSJDFBVSBVFJKBVS'
# s2 = 'ABECFDGJHVFBJDFHVBJ'
# s1 = 'ABCD'
# s2 = 'ABEDG'
# lcs_len = longest_common_subseqs_top_down_len(s1, s2)
# lcs = longest_common_subseqs_top_down(s1, s2)
# lcs_len = lcs_len_bottom_up(s1, s2)
# # lcs = lcs_bottom_up(s1, s2)
# print(lcs_len)
# print(lcs)
# print(list(e) for e in lcs_len)
# for e in lcs:
#     print(e)
# print(lcs)

##-------------------------------------------------------------------------------------------------
## wines sell problem
## Top-Down Dynamic Programming Soln
def wines_top_down(prices: list):
    def top_down_solver(memo, left, right, y):
        ## base case
        if left > right:
            return 0
        
        ## check if the state is already computed
        if memo[left][right] != 0:
            return memo[left][right]
        
        ## recursive case
        ## for a state (L,R) we have two options
        ## either pick left wine or the right one
        left_picked = prices[left]*y + top_down_solver(memo, left+1, right, y+1)
        right_picked = prices[right]*y + top_down_solver(memo, left, right-1, y+1)
        
        ## for state (L,R)
        memo[left][right] = max(left_picked, right_picked)
        
        return memo[left][right]
    
    n = len(prices)
    memo = [[0]*n for _ in range(n)]
    top_down_solver(memo, 0, n-1, 1)
    
    return memo[0][n-1]


## Bottom-Up Dynamic Programming Soln
def wines_bottom_up(prices: list):
    n = len(prices)
    
    ## initializing the dp array
    ## with (n+1) rows and n columns... why (n+1) row and n columns? 
    ## because to calculate the cell (n-1, n-1) we need to have state (n, n-1) and (n-1, n-2)
    dp = [[0]*(n) for _ in range(n+1)]
    
    for row in range(n-1, -1, -1): ## bottom row to top row
        for col in range(n):  ## first to last column
            if row <= col: 
                ## year 
                y = n - (col - row)
                
                ## two options to pick either left bottle or the right one
                left_picked = prices[row]*y + dp[row+1][col]
                right_picked = prices[col]*y + dp[row][col-1]
                
                ## storing the state
                dp[row][col] = max(left_picked, right_picked)
    
    return dp[0][n-1]
            
            
# prices = [2, 3, 5, 1, 4, 8, 1, 3, 6]
# # prices = [2, 5, 3]
# max_profit = wines_bottom_up(prices)
# print(max_profit)
# for e in max_profit:
#     print(e)

##-----------------------------------------------------------------------------------------------------
## subsequence count
## Top-Down DP soln
def count_subseqs_top_down(s1: str, s2: str):
    
    def top_down_dp_solver(memo, i, j):
        ## base cases
        if (i == -1 and j == -1) or (j == -1):
            return 1
        
        if i == -1:
            return 0
        
        ## check if the state is already computed
        if memo[i][j] is not None:
            return memo[i][j]
        
        ## recursive case
        if s1[i] == s2[j]:
            memo[i][j] = top_down_dp_solver(memo, i-1, j-1) + top_down_dp_solver(memo, i-1, j)
            return memo[i][j]
        
        memo[i][j] = top_down_dp_solver(memo, i-1, j)
        
        return memo[i][j]
    
    n, m = len(s1), len(s2)
    memo = [[None]*m for _ in range(n)]
    
    top_down_dp_solver(memo, n-1, m-1)
    
    return memo[n-1][m-1]


## Bottom-Up DP soln
def count_subseqs_bottom_up(s1: str, s2: str):
    n, m = len(s1), len(s2)
    
    ## initializing the dp array
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    ## fill the base case (first column as 1)
    for i in range(n+1):
        dp[i][0] = 1
        
    ## (1, 1) ... (n, m)
    ## main logic
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][m]
                
    
# s1 = "ABCDCECC"
# s2 = "ABC"
# cnt_top_down = count_subseqs_top_down(s1, s2)
# cnt_bottom_up = count_subseqs_bottom_up(s1, s2)
# print(cnt_top_down)
# print(cnt_bottom_up)
# for e in cnt_arr:
#     print(e)

##---------------------------------------------------------------------------------------------------
## Knapsack 0 1
## Top-Down DP soln
def knapsack_top_down(wts: list, prices: list, W: int):
    
    def top_down_dp_solver(memo, W, i, n):
        ## base case
        if i == n or W == 0:
            return 0
        
        ## check if the state is already computed
        if memo[W][i] is not None:
            return memo[W][i]
        
        ## initializing the inc, exc vars
        inc, exc = 0, 0
        
        if (W-wts[i] >= 0):
            inc = prices[i] + top_down_dp_solver(memo, W-wts[i], i+1, n)
        
        exc = 0 + top_down_dp_solver(memo, W, i+1, n)
        
        ## storing the computations
        memo[W][i] = max(inc, exc)
        
        return memo[W][i]
    
    n = len(wts)
    i = 0
    
    ## initializing the memo matrix of size (W+1) X n
    memo = [[None]*n for _ in range(W+1)]
    top_down_dp_solver(memo, W, i, n)
    
    return memo[W][i]


## knapsack bottom-up soln
def knapsack_bottom_up(wts: list, prices: list, W: int):
    n = len(wts)
    
    ## initializing the dp matrix
    dp = [[0]*(W+1) for _ in range(n+1)]
    
    ## filling the dp table in bottom-up manner
    for i in range(1, n+1):
        for w in range(1, W+1):
            inc, exc = 0, 0
            if wts[i-1] <= w:
                inc = prices[i-1] + dp[i-1][w - wts[i-1]]
            
            exc = 0 + dp[i-1][w]
            
            dp[i][w] = max(inc, exc)
    
    return dp[n][W]


# wts = [2, 7, 3, 4]
# prices = [5, 20, 20, 10]
wts = [123, 154, 258, 354, 365, 150, 95, 195]
prices = [89, 90, 95, 100, 90, 79, 50, 10]
W = 1000
max_profit = knapsack_bottom_up(wts, prices, W)
print(max_profit)   
# for e in max_profit:
#     print(e)     