## fibonacci series
import math

def fib_cnt(num: int):
    if num <= 1:
        return 1
    
    cnt = 0
    
    cnt_n_1 = fib_cnt(num-1) 
    cnt_n_2 = fib_cnt(num-2)
    
    cnt += cnt_n_1 + cnt_n_2
    
    return cnt


c = 0

def fibonacci_series(n: int):
    
    def solver(memo, n):
        global c
        c += 1
        
        if memo[n] is not None:
            return memo[n]
        
        if n <= 1:
            memo[n] = n
            return n
        
        sm = solver(memo, n-1) + solver(memo, n-2)
        memo[n] = sm
        
        return sm
    
    memo = [None] * (n+1)
    solver(memo, n)
    
    return memo



def fibonacci_series_tabulation(n: int):
    dp = [None] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    cnt = 0
    
    for i in range(2, n+1):
        cnt += 1
        dp[i] = dp[i-1] + dp[i-2]
    
    return cnt, dp

# n = 210
# # print(fibonacci_series(25))
# fibonacci_series(n)
# print(c, end=' ')
# print(cnt)

## -------------------------------------------------------------------------------------------------------------------


## ladder problem
## 1. top down approach 
## T.C: O(n*k)
def climb_ladder_top_down(n: int, k: int):
    
    def solver(memo, n, k):
        ## check if the state the already computed
        if memo[n] is not None:
            return memo[n]
        
        ## base case
        if n < 0:
            return 0
        
        if n == 0:
            memo[n] = 1
            return memo[n]
        
        sm = 0
        for jump in range(1, k+1):
            sm += solver(memo, n-jump, k)
        
        memo[n] = sm
        
        return memo[n]
    
    memo = [None] * (n+1)
    
    solver(memo, n, k)
    
    return memo[n]


## 2. bottom up approach
## T.C: O(n*k)
def climb_ladder_bottom_up(n: int, k: int):
    ## iterative solution
    dp = [0] * (n+1)
    
    ## base case assignment
    dp[0] = 1
    
    for i in range(1, n+1):
        for jump in range(1, k+1):
            if (i-jump) >= 0:
                dp[i] += dp[i-jump]
    
    return dp[n]


## approach-3 bottom up optimized
## T.C: O(n+k)
def climb_ladder_bottom_up_optimized(n: int, k: int):
    ## iterative solution 
    dp = [0] * (n+1)
    
    dp[0], dp[1] = 1, 1
    
    for i in range(2, k+1):
        dp[i] = 2 * dp[i-1]
    
    for i in range(k+1, n+1):
        dp[i] = 2 * dp[i-1] - dp[n-k-1]
    
    return dp[n]

# print(climb_ladder_bottom_up_optimized(6, 4))
# print(climb_ladder_bottom_up(6, 4))
# print(climb_ladder_top_down(6, 4))

## -------------------------------------------------------------------------------------------------------------------

## coin change problem
## T.C: O(t^m) m: target money, t: types of coins
def coin_change(coins: list, m: int) -> int:
    
    def solver(m):
        ## base case
        if m == 0:
            return 0
        
        # fn = []
        mn = math.inf
        for coin in coins:
            if (m - coin) >= 0:
                f = solver(m-coin)
                mn = min(f, mn)
                # fn.append(f)
                
        return mn + 1
    
    res = solver(m)
    return -1 if res == math.inf else res


## DP top-down solution
## T.C: O(m.t) m: target money, t: types of coins
def coin_change_top_down(coins: list, m: int) -> int:
    
    def solver(memo, m):
        ## check if the state is already computed
        if memo[m] is not None:
            return memo[m]
        
        ## base case
        if m == 0:
            memo[m] = 0
            return memo[m]
        
        ## storing all the function calling in a list, 
        ## so that we can have the track of all the function call
        ## at a given state m.
        mn = math.inf
        # fn = []
        for coin in coins:
            if (m - coin) >= 0:
                f = solver(memo, m-coin)
                mn = min(mn, f)
                # fn.append(f)
        
        ## storing the computed result at m state in memo array
        memo[m] = mn + 1
        
        return memo[m]
    
    memo = [None] * (m+1)
    
    solver(memo, m)
    
    return -1 if memo[m] == math.inf else memo[m]


## DP bottom-up solution
## T.C: O(m.t) m: target money, t: types of coins
def coin_change_bottom_up(coins: list, m: int) -> int:
    ## assigning the dp array
    dp = [0] * (m+1)
    
    ## base case assignment
    dp[0] = 0
    
    for n in range(1, m+1):
        dp[n] = math.inf
        for coin in coins:
            if (n - coin) >= 0 and dp[n-coin] != math.inf:
                dp[n] = min(dp[n], dp[n-coin] + 1)
    
    return -1 if dp[m] == math.inf else dp[m]
    
    
# coins = [1, 3, 7, 10, 2]
# m = 12
# coins = [5, 6, 7, 3]
# m = 47
# print(coin_change_top_down(coins, m))

## -----------------------------------------------------------------------------------------------------
## Rod Cutting Problem

def rod_cutting(n: int, price: list) -> int:
    ## base case
    if n <= 0:
        return 0
    
    max_profit = - math.inf
    
    for i in range(n):
        cut_length = i + 1
        f = price[i] + rod_cutting(n-cut_length, price)
        max_profit = max(max_profit, f)
    
    return max_profit


def rod_cutting_top_down(n: int, price: list) -> int:
    
    def solver(memo, n, price):
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        ## base cases
        if n < 0:
            return 0
        
        if n == 0:
            memo[n] = 0
            return memo[n]
        
        # Initialize max_profit for current rod length
        max_profit = - math.inf
        
        for i in range(n):
            cut_length = i + 1
            f = price[i] + solver(memo, n-cut_length, price)
            max_profit = max(max_profit, f)
        
        memo[n] = max_profit
        
        return memo[n]
    
    memo = [None] * (n+1)
    solver(memo, n, price)
    
    return memo[n]


def rod_cutting_bottom_up(n: int, price: list) -> int:
    dp = [None] * (n+1)
    
    ## base case assignment
    dp[0] = 0
    
    for length in range(1, n+1):
        # Initialize max_profit for current rod length
        max_profit = - math.inf
        for i in range(length):
            cut_length = i + 1
            # Calculate potential profit
            f = price[i] + dp[length - cut_length]
            # Update max_profit if f is greater
            max_profit = max(max_profit, f)
            
        # Store the maximum profit for current rod length
        dp[length] = max_profit
        
    # Maximum profit for rod of length n
    return dp[n]
            

# n = 8
# # price = [3, 5, 8, 9, 10, 17, 17, 20, 12, 16, 32, 15, 2, 3, 5, 6, 17, 18]
# price = [1, 5, 8, 9, 10, 17, 17, 20]
# max_profit = rod_cutting_top_down(n, price)
# # max_profit = rod_cutting_bottom_up(n, price)
# print(max_profit)

## ----------------------------------------------------------------------------------------------------------
## minimum array jumps
## Top-Down solution
def array_jumps_top_down(nums: list) -> int:
    
    def top_down_dp(memo, i, nums, n):
        
        ## base cases
        if i >= n:
            return math.inf
        
        if i == n-1:
            memo[i] = 0
            return memo[i]
        
        ## check does the state already been calculated
        if memo[i] is not None:
            return memo[i]
        
        ## initializing the min steps needed to reach at end index 
        ## from index i
        min_steps = math.inf
        ## maximum jump can take from index i
        max_jumps = nums[i]
        
        for jump in range(1, max_jumps+1):
            subproblem = top_down_dp(memo, i+jump, nums, n)
            ## check does it possible to reach end index from the current index i
            if subproblem != math.inf:
                min_steps = min(min_steps, subproblem+1)
                
        ## storing the minimum steps needed to reach the end index from the current 
        ## index i in memo array to avoid re-calculations.
        memo[i] = min_steps
                
        return memo[i]
    
    n = len(nums)
    memo = [None] * n
    top_down_dp(memo, 0, nums, n)
    
    return memo[0]


## bottom-up solution
def array_jumps_bottom_up(nums: list) -> int:
    n = len(nums)
    
    dp = [None] * n
    dp[n-1] = 0
    
    for i in range(n-2, -1, -1):
        min_steps = math.inf
        max_jumps = nums[i]
        for jump in range(1, max_jumps+1):
            if i + jump < n:
                min_steps = min(min_steps, dp[i+jump]+1)
                
        dp[i] = min_steps
    
    return dp[0]

# nums1 = [2, 1, 2, 1, 1, 3, 2, 1, 1, 1, 2, 3, 1, 2, 4, 1, 2, 1, 2, 3, 7, 3, 1, 2, 1, 2, 1, 2]
# nums2 = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 2, 5]
# # jumps = array_jumps_top_down(nums1)
# jumps = array_jumps_bottom_up((nums2))
# print(jumps)

## ----------------------------------------------------------------------------------------------------
## Frog's min cost
## Top-Down solution
def min_cost_top_down(height: list) -> int:
    
    def top_down_dp(memo, i, n):
        ## base cases
        if i >= n:
            return math.inf
        
        if i == n-1:
            ## since the cost to reach from index i = n-1 to end index i.e (n-1) is 0
            memo[i] = 0
            return memo[i]
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        ## for an index i, there are two options to go, either i+1 or i+2
        ## initializing the cost for jump-1 and jump-2
        cost_to_jump_1 = math.inf
        cost_to_jump_2 = math.inf
        
        if (i + 1) < n:
            cost_to_jump_1 = min(cost_to_jump_1, abs(height[i] - height[i+1]) + top_down_dp(memo, i+1, n))
        
        if (i + 2) < n:
            cost_to_jump_2 = min(cost_to_jump_2, abs(height[i] - height[i+2]) + top_down_dp(memo, i+2, n))
        
        ## storing the minimum cost to reach end index from index i in memo array, 
        ## to avoid re-calculations.
        ## cost for index i to reach the end index will be minimum of cost_to_jump_1 and cost_to_jump_2
        memo[i] = min(cost_to_jump_1, cost_to_jump_2)
        
        return memo[i]
    
    n = len(height)
    memo = [None] * n
    top_down_dp(memo, 0, n)
    
    return memo[0]


nums = [30, 10, 60, 10, 60, 50]
# stones = [10, 10]
print(min_cost_top_down(nums))    