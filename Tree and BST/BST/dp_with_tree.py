import math

class TreeNode:
    
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

##############################################################################################################################
## **DP With BST**
## **96. Unique Binary Search Trees**
## Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
## Catalan Number
def numTrees(n: int) -> int:
    
    def solveMem(memo, n):
        ## base cases
        if (n == 0) or (n == 1):
            return 1
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        ans = 0
        ## assume i as the root node
        for i in range(1, n+1):
            ans += solveMem(memo, i-1) * solveMem(memo, n-i)
        
        ## store the computed state
        memo[n] = ans
        
        return memo[n]
    
    
    def solveTab(num_nodes):
        ## initializing the dp array
        dp = [0] * (num_nodes+1)
        
        ## base cases
        dp[0] = dp[1] = 1
        
        ## considering nodes from 2 to total number of nodes
        for n in range(2, num_nodes+1):
            ## assume i as the root node
            ans = 0
            for i in range(1, n+1):
                ans += dp[i-1] * dp[n-i]
            
            dp[n] = ans
        
        return dp[num_nodes]            
    
    ## initializing the memo array
    memo = [None] * (n+1)
    
    return solveMem(memo, n), solveTab(n)

# n = 4
# trees = numTrees(n)
# print(trees)
#######################################################################################################################
## **375. Guess Number Higher or Lower II**
def getMoneyAmount(n: int) -> int:
    
    def solveMem(memo, start, end):
        ## base case
        if start >= end:
            return 0
        
        ## check if the state is already computed
        if memo[start][end] is not None:
            return memo[start][end]
        
        mn = math.inf
        ## Guessing wrong integer (i)
        for i in range(start, end+1, 1):
            mn = min(mn, i + max(solveMem(memo, start, i-1), solveMem(memo, i+1, end)))
        
        ## store the computed state
        memo[start][end] = mn
        
        return memo[start][end]
    
    
    def solveTab(n):
        ## initializing the dp array
        dp = [[0]*(n+2) for _ in range(n+2)]
        
        for start in range(n, 0, -1):
            for end in range(start, n+1, 1):
                if start == end:
                    continue
                else:
                    mn = math.inf
                    for i in range(start, end+1, 1):
                        mn = min(mn, i + max(dp[start][i-1], dp[i+1][end]))
                
                    dp[start][end] = mn
                
        return dp[1][n]
    
    ## initializing the memo array
    memo = [[None]*(n+1) for _ in range(n+1)]
    
    return solveMem(memo, 1, n), solveTab(n)

n = 69
money = getMoneyAmount(n)
print(money)

















