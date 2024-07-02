import math

## Introduction to Dynamic Programming
## fibonacci series:
def fibonacci(n: int):
    
    def top_down_solver(memo, n):
        ## base case
        if n == 0 or n == 1:
            return n
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        ## store the computed state
        memo[n] = top_down_solver(memo, n-1) + top_down_solver(memo, n-2)
        
        return memo[n]
    
    
    def bottom_up_solver(n):
        ## initializing the dp array
        dp = [None] * (n+1)
        
        ## base case
        dp[0], dp[1] = 0, 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    
    def space_opt(n):
        ## initializing the zeroth and first fib
        a, b = 0, 1
        
        if n == 0:
            return a
        
        for _ in range(2, n+1):
            c = a + b
            a = b
            b = c
        
        return b
    
    
    # memo = [None] * (n+1)
    # return top_down_solver(memo, n)
    
    return space_opt(n)

# print(fibonacci(n=10))
##------------------------------------------------------------------------------------------------------------------------
## total number of ways to reach nth stair:
def climbingStairs(n: int):
    
    def solver(nStairs):
        ## base case
        if nStairs == n:
            return 1
        
        if nStairs > n:
            return 0
        
        return solver(nStairs=nStairs+1) + solver(nStairs=nStairs+2)
    
    
    def top_down_solver(memo, nStairs):
        ## base cases
        if nStairs == n:
            return 1
        
        if nStairs > n:
            return 0
        
        ## check if the state is already computed
        if memo[nStairs] is not None:
            return memo[nStairs]
        
        ## store the computation
        memo[nStairs] = top_down_solver(memo, nStairs+1) + top_down_solver(memo, nStairs+2)
        
        return memo[nStairs]
    
    
    def bottom_up_solver(nStairs):
        ## initializing the dp array
        dp = [None] * (nStairs+1)
        
        ## base cases
        dp[nStairs], dp[nStairs-1] = 1, 1
        
        for i in range(nStairs-2, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]
    
    def space_opt(nStairs):
        ## base cases
        a, b = 1, 1
        
        for _ in range(nStairs-2, -1, -1):
            c = a + b
            a = b
            b = c
        
        return b

    
    memo = [None] * (n+1)
    # return top_down_solver(memo, 0)
    
    return top_down_solver(memo, 0), bottom_up_solver(n), space_opt(n)

# n = 45
# print(climbingStairs(n))

##----------------------------------------------------------------------------------------------------------------
## Minimum cost climbing stair:
## 746. Min Cost Climbing Stairs
def minCostClimbingStairs(cost: list[int]) -> int:
    
    def solver(i):
        ## base case
        if i == len(cost) - 1:
            return cost[i]
        
        if i >= len(cost):
            return 0
        
        one_step = cost[i] + solver(i+1)
        two_step = cost[i] + solver(i+2)
        
        return min(one_step, two_step)
    
    
    def top_down_solver(memo, i):
        ## base cases
        if i == len(cost) - 1:
            return cost[i]
        
        if i >= len(cost):
            return 0
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        one_step = cost[i] + top_down_solver(memo, i+1)
        two_step = cost[i] + top_down_solver(memo, i+2)
        
        ## store the computed state
        memo[i] = min(one_step, two_step)
        return memo[i]
    
    def bottom_up_solver(n):
        ## initializing the dp array
        dp = [None] * n
        
        ## base cases
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]
        
        for i in range(n-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])
    
    
    def top_down_solver1(memo, i):
        ## base cases
        if i == 0 or i == 1:
            return cost[i]
        
        if i < 0:
            return 0
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        one_step = cost[i] + top_down_solver1(memo, i-1)
        two_step = cost[i] + top_down_solver1(memo, i-2)
        
        ## store the state
        memo[i] = min(one_step, two_step)
        
        return memo[i]
    
    
    def bottom_up_solver1(n):
        ## initializing the dp array
        dp = [None] * (n)
        
        ## base case
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])
    
    def space_opt(n):
        a = cost[0]
        b = cost[1]
        
        for i in range(2, n):
            c = cost[i] + min(a, b)
            a = b
            b = c
        
        return min(a, b)
    
    
    n = len(cost)
    # memo = [None] * (n+1)
    
    return bottom_up_solver(n)

# cost = [1,100,1,1,1,100,1,1,100,1]
# print(minCostClimbingStairs(cost))
## -------------------------------------------------------------------------------------------------------------------------------------
## 322. Coin Change
def coinChange(coins: list[int], amount:  int) -> int:
    
    def top_down_solver(memo, amount):
        ## base case
        if amount == 0:
            return 0
        
        if amount < 0:
            return math.inf
        
        ## check if the state is already computed
        if memo[amount] is not None:
            return memo[amount]
        
        mn = math.inf
        for coin in coins:
            ans = 1 + top_down_solver(memo, amount-coin)
            mn = min(mn, ans)
            
        ## store the computed state
        memo[amount] = mn
        
        return memo[amount]
    
    
    def bottom_up_solver(amount):
        ## inializing the dp array
        dp = [math.inf] * (amount+1)
        
        ## base case
        dp[0] = 0
        
        for amnt in range(1, amount+1):
            mn = math.inf
            for coin in coins:
                if (amnt - coin) >= 0:
                    ans = 1 + dp[amnt-coin]
                    mn = min(mn, ans)
                    
            dp[amnt] = mn
        
        return dp[amount]
    
    ## initializing the memo array
    # memo = [None] * (amount+1)
    # res = top_down_solver(memo, amount)
    
    res = bottom_up_solver(amount)
    
    return -1 if res == math.inf else res

# coins = [2]; amount = 3
# print(coinChange(coins, amount))
################################################################################################################
## Maximun sum of non-adjacent elements:
## Leetcode: 198. House Robber
def maxSumNonAdjacentElements(nums: list[int]) -> int:
    
    n = len(nums)
    
    def solveMem(memo, i):
        ## base cases
        if i >= n:
            return 0
        
        if i == n-1:
            return nums[i]
        
        if i == n-2:
            return max(nums[i], nums[i+1])
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        ## include the curr element
        incl = nums[i] + solveMem(memo, i+2)
        
        ## exclude the curr element
        excl = 0 + solveMem(memo, i+1)
        
        ## store the computed state
        memo[i] = max(incl, excl)
        
        return memo[i]
    
    
    def solveTab(n):
        ## initializing the dp array
        dp = [None] * (n)
        
        ## base cases
        dp[n-1] = nums[n-1]
        dp[n-2] = max(dp[n-1], nums[n-2])
        
        for i in range(n-3, -1, -1):
            
            ## include the current element
            incl = nums[i] + dp[i+2]
            
            ## exclude 
            excl = 0 + dp[i+1]
            
            dp[i] = max(incl, excl)
        
        return dp[0]
    
    
    def spaceOpt(n):
        ## initializing two vars
        ## base cases
        a = nums[n-1]
        b = max(a, nums[n-2])
        
        for i in range(n-3, -1, -1):
            ## include
            incl = nums[i] + a
            
            ## exclude
            excl = 0 + b
            
            c = max(incl, excl)
            
            a = b
            b = c
        
        return b
    
    memo = [None] * (n)
    
    return solveMem(memo, 0), solveTab(n), spaceOpt(n)

# nums = [9]
# res = maxSumNonAdjacentElements(nums)
# print(res)
##################################################################################################################################
## 213. House Robber II
def rob(nums: list[int]) -> int:
    
    def solveMem(memo, i, m):
        ## base cases
        if i >= m:
            return 0
        
        if i == m-1:
            return nums[i]
        
        if i == m-2:
            return max(nums[i], nums[i+1])
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        ## include the curr element
        incl = nums[i] + solveMem(memo, i+2, m)
        
        ## exclude the curr element
        excl = 0 + solveMem(memo, i+1, m)
        
        ## store the computed state
        memo[i] = max(incl, excl)
        
        return memo[i]
    
    def solveTab(arr):
        m = len(arr)
        
        ## initializing the dp array
        dp = [None] * m
        
        ## base cases
        dp[m-1] = arr[m-1]
        dp[m-2] = max(dp[m-1], arr[m-2])
        
        for i in range(m-3, -1, -1):
            ## include
            incl = arr[i] + dp[i+2]
            
            ## exclude
            excl = 0 + dp[i+1]
            
            dp[i] = max(incl, excl)
        
        return dp[0]
    
    def spaceOpt(arr):
        m = len(arr)
        
        ## initializing the base cases
        a = arr[m-1]
        b = max(a, arr[m-2])
        
        for i in range(m-3, -1, -1):
            ## include
            incl = arr[i] + a
            
            ## exclude
            excl = 0 + b
            
            c = max(incl, excl)
            
            a = b
            b = c
        
        return b
    
    
    n = len(nums)

    ## explicit base case
    if n == 1:
        return nums[0]

    # memo1 = [None] * n
    # memo2 = [None] * n
    
    # return max(solveMem(memo1, 0, n-1), solveMem(memo2, 1, n)) 
    
    # Solve two scenarios:
    # 1. Exclude the last house
    # 2. Exclude the first house
    return max(spaceOpt(nums[:-1]), spaceOpt(nums[1:]))

##########################################################################################################################
## Cut into segments:
def cutIntoSegments(n: int, x: int, y: int, z: int) -> int:
    
    def solveMem(memo, n):
        ## base case
        if n == 0:
            return 0
        
        if n < 0:
            return -math.inf
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        segment_x = 1 + solveMem(memo, n-x)
        segment_y = 1 + solveMem(memo, n-y)
        segment_z = 1 + solveMem(memo, n-z)
        
        ## store the computed state
        memo[n] = max(segment_x, segment_y, segment_z)
        
        return memo[n]
    
    
    def solveTab(n):
        ## initializing the dp array
        dp = [-math.inf] * (n+1)
        
        ## fill the base case
        dp[0] = 0
        
        for i in range(1, n+1):
            segment_x, segment_y, segment_z = -math.inf, -math.inf, -math.inf
            
            if (i - x) >= 0:
                segment_x = 1 + dp[i-x]
            
            if (i - y) >= 0:
                segment_y = 1 + dp[i-y]
            
            if (i - z) >= 0:
                segment_z = 1 + dp[i-z]
            
            dp[i] = max(segment_x, segment_y, segment_z)
        
        return dp[n]
    
    memo = [None] * (n+1)
    
    return solveMem(memo, n), solveTab(n)

# n = 102; x, y, z = 3, 7, 2
# segments = cutIntoSegments(n, x, y, z)
# print(segments)
################################################################################################################
## Count Derangements: Total number of possible derangements, given a number n -> [0, 1, 2, ... n-2, n-1]
def cntDerangements(n: int):
    
    MOD = (10**9) + 7
    
    def solveMem(memo, n):
        ## base case
        if n == 1:
            return 0
        
        if n == 2:
            return 1
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        ## strore the computed state
        memo[n] = ((n-1) * (solveMem(memo, n-1) + solveMem(memo, n-2))) % MOD
        
        return memo[n]
    
    
    def solveTab(n):
        ## initializig the dp array
        dp = [0] * (n+1)
        
        ## fill the base cases
        dp[1] = 0
        dp[2] = 1
        
        for i in range(3, n+1):
            dp[i] = ((i-1) * (dp[i-1] + dp[i-2])) % MOD
        
        return dp[n]
    
    
    def spaceOpt(n):
        if n == 1:
            return 0
        
        ## base cases
        a = 0
        b = 1
        
        for i in range(3, n+1):
            c = ((i-1) * (a + b)) % MOD
            
            a = b
            b = c
        
        return b
    
    ## initializing the memo array
    # memo = [None] * (n+1)
    
    return spaceOpt(n)

# n = 1
# cnt = cntDerangements(n)
# print(cnt)
####################################################################################################################################
## Painting Fence Algorithm:
def fenceAlgo(n: int, k: int) -> int:
    MOD = (10**9) + 7
    
    def solveMem(memo, n, k):
        ## base case
        if n == 1:
            return k
        
        if n == 2:
            return k*k
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        ## store the computed state
        memo[n] = ( (k-1) * ( solveMem(memo, n-2, k) + solveMem(memo, n-1, k) ) ) % MOD
        
        return memo[n]
    
    
    def solveTab(n, k):
        ## initializing the dp array
        dp = [0] * (n+1)
        
        ## base cases
        dp[1] = k
        dp[2] = k*k
        
        for i in range(3, n+1):
            dp[i] = ( (k-1) * ( dp[i-2] + dp[i-1] ) ) % MOD
        
        return dp[n]
    
    
    def spaceOpt(n, k):
        if n == 1:
            return k
        
        ## initializing the base cases
        a = k
        b = k*k
        
        for _ in range(3, n+1):
            c = ( (k-1) * ( a + b ) ) % MOD
            
            a = b
            b = c
        
        return b
    
    ## initializing the memo array
    # memo = [None] * (n+1)
    
    return spaceOpt(n, k)


n = 16; k = 4
ways = fenceAlgo(n, k)
print(ways)