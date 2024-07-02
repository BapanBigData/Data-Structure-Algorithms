import math
from collections import deque

## 377. Combination Sum IV
## Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
def combinationSum4(nums: list[int], target: int) -> int:
    
    def solveMem(memo, target):
        ## base case
        if target == 0:
            return 1
        
        ## check if the state is already computed
        if memo[target] is not None:
            return memo[target]
        
        ans = 0
        for num in nums:
            if (target - num) >= 0:
                ans += solveMem(memo, target-num)
        
        ## store the computed state
        memo[target] = ans
        
        return memo[target]
    
    def solveTab(target):
        ## initializing the dp array
        dp = [None] * (target+1)
        
        ## base case
        dp[0] = 1
        
        for tar in range(1, target+1):
            ans = 0
            for num in nums:
                if (tar - num) >= 0:
                    ans += dp[tar-num]
            
            dp[tar] = ans
        
        return dp[target]
    
    ## initializing the memo array
    memo = [None] * (target+1)
    
    return solveMem(memo, target), solveTab(target)

# nums = [1, 2, 3]; target = 4
# res = combinationSum4(nums, target)
# print(res)
###################################################################################################################################
## 279. Perfect Squares
## Given an integer n, return the least number of perfect square numbers that sum to n.
## A perfect square is an integer that is the square of an integer; 
## in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
def numSquares(n: int):
    
    def solveMem(memo, n):
        ## base case
        if n == 0:
            return 0
        
        ## check if the state is computed
        if memo[n] is not None:
            return memo[n]
        
        ans = math.inf

        i = 1
        while (i*i) <= n:
            f = 1 + solveMem(memo, n-(i*i))
            ans = min(ans, f)
            
            i += 1
        
        ## store the computed state
        memo[n] = ans
        
        return memo[n]
    
    
    def solveTab(n):
        ## initializing the dp array
        dp = [None] * (n+1)
        
        ## base case
        dp[0] = 0
        
        for i in range(1, n+1):
            ans = math.inf
            j = 1
            while (j*j) <= i:
                f = 1 + dp[i-(j*j)]
                ans = min(ans, f)
                
                j += 1
            
            dp[i] = ans
        
        return dp[n]
    
    ## initializing the memo array
    memo = [None] * (n+1)
    
    return solveMem(memo, n), solveTab(n)

# n = 931
# print(numSquares(n))
###########################################################################################################################
## **983. Minimum Cost For Tickets**

def minCostTickets(days: list[int], costs: list[int]) -> int:
    n = len(days)
    
    def solveMem(memo, i):
        ## base case
        if i >= n:
            return 0
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        ## 1-day pass
        option_1 = costs[0] + solveMem(memo, i+1)
        
        ## 7-day pass
        j = i
        while (j < n) and (days[j] < days[i] + 7):
            j += 1
        
        option_2 = costs[1] + solveMem(memo, j)
        
        ## 30-day pass
        j = i
        while (j < n) and (days[j] < days[i] + 30):
            j += 1
        
        option_3 = costs[2] + solveMem(memo, j)
        
        ## store the computed state
        memo[i] = min(option_1, option_2, option_3) 
        
        return memo[i]
    
    
    def solveTab(n):
        ## initializing the dp array
        dp = [None] * (n+1)
        
        ## base case
        dp[n] = 0
        
        for i in range(n-1, -1, -1):
            ## 1-day pass
            option_1 = costs[0] + dp[i+1]
            
            ## 7-day pass
            j = i
            while (j < n) and (days[j] < days[i] + 7):
                j += 1
            
            option_2 = costs[1] + dp[j]
            
            ## 30-day pass
            j = i
            while (j < n) and (days[j] < days[i] + 30):
                j += 1
                
            option_3 = costs[2] + dp[j]
            
            dp[i] = min(option_1, option_2, option_3)
        
        return dp[0]
    
    ## initializing a memo array
    memo = [None] * (n+1)
    
    return solveMem(memo, 0), solveTab(n)

## Queue soln
def minCostTickets1(days: list[int], costs: list[int]) -> int:
    ## initializing 2 queues (weekly, monthly)
    ## the queues are in the pair of (day, cost)
    weekly_queue = deque()
    monthly_queue = deque()
    
    ans = 0
    
    for day in days:
        
        ## to be in the queue for `weekly_queue` (weekly_front + 7) > curr day 
        ## simillarly for `monthly_queue` (monthly_front + 30) > curr day
        
        while weekly_queue and (weekly_queue[0][0] + 7 <= day):
            weekly_queue.popleft()
        
        while monthly_queue and (monthly_queue[0][0] + 30 <= day):
            monthly_queue.popleft()
        
        ## push the current day cost to the queues
        weekly_queue.append((day, ans + costs[1]))
        monthly_queue.append((day, ans + costs[2]))
        
        ans = min((ans + costs[0]), weekly_queue[0][1], monthly_queue[0][1])
    
    return ans

# days = [1,2,3,4,5,6,7,8,9,10,30,31]; costs = [2, 7, 15]
# min_cost = minCostTickets1(days=days, costs=costs)
# print(min_cost)
#######################################################################################################################



















