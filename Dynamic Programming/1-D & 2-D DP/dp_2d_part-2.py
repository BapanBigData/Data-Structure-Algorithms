import math

## recap coin change 1 problem
## given an array of integers (Assume there is infinite supply of elements in the array) and a money m
## find minimum coins required to make the change

def coin_change_1_top_down(coins: list, m: int):
    
    def dp_solver(memo, m):
        ## base case
        if m == 0:
            return 0
        
        ## check if the state is already calculated
        if memo[m] is not None:
            return memo[m]
        
        mn = math.inf
        for coin in coins:
            if (m-coin) >= 0:
                f = dp_solver(memo, m-coin)
                mn = min(mn, f)
                
        memo[m] = mn + 1
        
        return memo[m]
    
    memo = [None] * (m+1)
    dp_solver(memo, m)
    
    return memo[m]

# coins = [1, 3, 7, 10]
# ans = coin_change_1_top_down(coins, 15)
# print(ans)

## coin change 2
def coin_change_2_top_down(coins: list, m: int):
    
    def dp_solver(memo, i, m, n):
        ## base cases
        if m == 0:
            return 1
        
        ## either one scan of the array is completed 
        ## or m becomes negative here
        if (i == n) or (m < 0):
            return 0
        
        ## check if the state is already computed
        if memo[i][m] is not None:
            return memo[i][m]
        
        ## For each coin denomination, we have two choices: 
        ## either we include it in the combination or we exclude it.
        inc = dp_solver(memo, i, m-coins[i], n)
        exc = dp_solver(memo, i+1, m, n)
        
        memo[i][m] = inc + exc
        
        return memo[i][m]
    
    n = len(coins)
    i = 0
    ## initializing the memo array
    memo = [[None]*(m+1) for _ in range(n)]
    dp_solver(memo, i, m, n)
    
    return memo[i][m]

coins = [1, 2, 3]
target = 4
cnt = coin_change_2_top_down(coins, target)
print(cnt)
# for c in cnt:
#     print(c)


# coins = [1, 2, 3]
# cnt = coin_change_2(coins, 4)
# print(cnt)
##-----------------------------------------------------------------------------------------
# ## Game Of Wits
# def game_of_wits(s: str):
    
#     def solver(s, is_oswald_turn):
#         ## base case
#         if not s:
#             if is_oswald_turn:
#                 return 'O', 0
#             else:
#                 return 'H', 0
        
#         if is_oswald_turn:
#             if s[0] == 'O' and s[-1] == 'O':
#                 left_picked = solver(s[1:], not is_oswald_turn)
#                 right_picked = solver(s[:len(s)-1], not is_oswald_turn)
                
#                 if left_picked[1] > right_picked[1]:
#                     return left_picked[0], left_picked[1]
#                 else:
#                     return right_picked[0], right_picked[1]
            
#             elif s[0] == 'O':
#                 return solver(s[1:], not is_oswald_turn)
            
#             elif s[-1] == 'O':
#                 return solver(s[:len(s)-1], not is_oswald_turn)
            
#             else:
#                 return 'H', len(s) + 1
            
#         else:
#             if s[0] == 'H' and s[-1] == 'H':
#                 left_picked = solver(s[1:], is_oswald_turn)
#                 right_picked = solver(s[:len(s)-1], is_oswald_turn)
                
#                 if left_picked[1] > right_picked[1]:
#                     return left_picked[0], left_picked[1]
#                 else:
#                     return right_picked[0], right_picked[1]
            
#             elif s[0] == 'H':
#                 return solver(s[1:], is_oswald_turn)
            
#             elif s[-1] == 'H':
#                 return solver(s[:len(s)-1], is_oswald_turn)
            
#             else:
#                 return 'O', len(s) + 1
    
#     return solver(s, True)
###----------------------------------------------------------------------------------------------------------
## Edit Distance: 
## Top-Down Dynamic Programming
def edit_distance_solver_top_down(memo, word1, word2, i, j):
    ## base cases
    if i == len(word1):
        return len(word2) - j
    
    if j == len(word2):
        return len(word1) - i
    
    ## check if the state is already computed
    if memo[i][j] is not None:
        return memo[i][j]
    
    ## recursion case
    ans = 0
    if word1[i] == word2[j]:
        return edit_distance_solver_top_down(memo, word1, word2, i+1, j+1)
    else:
        ## insert
        insert_ans = 1 + edit_distance_solver_top_down(memo, word1, word2, i, j+1)
        ## delete
        delete_ans = 1 + edit_distance_solver_top_down(memo, word1, word2, i+1, j)
        ## replace
        replace_ans = 1 + edit_distance_solver_top_down(memo, word1, word2, i+1, j+1)
        
        ans = min(insert_ans, delete_ans, replace_ans)
    
    ## store the computations
    memo[i][j] = ans
    
    return memo[i][j]

def edit_distance_top_down(word1: str, word2: str):
    n = len(word1)
    m = len(word2)
    
    ## initializing memo matrix
    memo = [[None]*(m) for _ in range(n)]
    edit_distance_solver_top_down(memo, word1, word2, 0, 0)
    
    return memo[0][0]


def edit_distance_bottom_up(word1, word2):
    
    def bottom_up_solver(dp, word1, word2, n, m):
        ## initialial fill of the dp array (base cases)
        for j in range(m+1):
            dp[n][j] = m - j
        
        for i in range(n+1):
            dp[i][m] = n - i
        
        ## main logic
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                ans = 0
                
                if word1[i] == word2[j]:
                    ans = dp[i+1][j+1]
                else:
                    ## insert
                    insert_ans = 1 + dp[i][j+1]
                    ## delete
                    delete_ans = 1 + dp[i+1][j]
                    ## replace
                    replace_ans = 1 + dp[i+1][j+1]
                    
                    ans = min(insert_ans, delete_ans, replace_ans)
                
                dp[i][j] = ans
        
        return dp[0][0]
    
    n = len(word1)
    m = len(word2)
    
    ## initializing the dp array
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    return bottom_up_solver(dp, word1, word2, n, m)


# word1 = 'horse'
# word2 = 'ros'
# cost = edit_distance_bottom_up(word1, word2)
# print(cost)
# for e in cost:
#     print(e)