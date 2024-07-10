import math

## **70. Climbing Stairs**
## You are climbing a staircase. It takes n steps to reach the top.
## Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n: int) -> int:
    
    def solvMem(memo, n):
        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        if n == 1:
            return 1
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        ## store the computed state
        memo[n] = solvMem(memo, n-1) + solvMem(memo, n-2)
        
        return memo[n]
    
    ## initializing the memo
    memo = [None]*(n+1)
    
    return solvMem(memo, n)

# n = 3
# num_ways = climbStairs(n)
# print(num_ways)
## ##################################################################################################
## **746. Min Cost Climbing Stairs**
def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    
    def solveMem(memo, i):
        ## base case
        if i >= n:
            return 0
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        ## store the computed state
        memo[i] = cost[i] + min(solveMem(memo, i+1), solveMem(memo, i+2))
        
        return memo[i]
    
    ## initializing the memo array
    memo = [None]*n
    
    return min(solveMem(memo, 0), solveMem(memo, 1))

# nums = [1,100,1,1,1,100,1,1,100,1]
# minCost = minCostClimbingStairs(nums)
# print(minCost)
############################################################################################################################
## **2244. Minimum Rounds to Complete All Tasks**
def minimumRounds(tasks: list[int]) -> int:
    
    def solveMem(memo, n):
        ## base cases
        if n < 2:
            return math.inf
        
        if (n == 2) or (n == 3):
            return 1
        
        ## check if the state is already computed
        if n in memo:
            memo[n]
        
        res = math.inf
        
        if (n-2) > 0:
            res = min(res, (1+solveMem(memo, n-2)))
            
        if (n-3) > 0:
            res = min(res, (1+solveMem(memo, n-3)))
        
        ## store the computed state
        memo[n] = res
        
        return memo[n]
    
    
    def solveTab(n):
        ## initializing the dp
        dp = {}
        
        ## base case
        dp[2] = dp[3] = 1
        
        dp[1] = math.inf
        
        for i in range(4, n+1):
            res = math.inf
            
            if (i-2) > 0:
                res = min(res, 1 + dp[i-2])
            
            if (i-3) > 0:
                res = min(res, 1 + dp[i-3])
            
            dp[i] = res
        
        return dp[n]
    
    ## initializing a frequency dict for each task 
    freq_dict = {}
    for e in tasks:
        if e in freq_dict:
            freq_dict[e] += 1
        else:
            freq_dict[e] = 1
    
    ## initializing the memo dict
    memo = {}
    
    min_rounds = 0
    for task, cnt in freq_dict.items():
        ## for each task calculate min rounds required to complete
        rounds = solveTab(cnt)
        
        if rounds == math.inf:
            return -1
        
        min_rounds += rounds
    
    return min_rounds


tasks = [2,2,3,3,2,4,4,4,4,4]
min_rounds = minimumRounds(tasks)
print(min_rounds)