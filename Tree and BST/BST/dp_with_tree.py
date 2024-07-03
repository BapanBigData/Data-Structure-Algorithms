import math

##############################################################################################################################
## **DP with Merge interval Pattern**
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

# n = 69
# money = getMoneyAmount(n)
# print(money)
#####################################################################################################################################
## **1130. Minimum Cost Tree From Leaf Values**

def mctFromLeafValues(arr: list[int]) -> int:
    n = len(arr)
    
    ## initializing a dict to have the access of the maximum
    mx_mp = {}
    
    for i in range(n):
        mx_mp[(i, i)] = arr[i]
        for j in range(i+1, n):
            mx_mp[(i, j)] = max(arr[j], mx_mp[(i, j-1)])
    
    def solveMem(memo, left, right):
        ## base cases
        if left >= right:
            return 0
        
        ## check if the state is already computed
        if memo[left][right] is not None:
            return memo[left][right]
        
        ans = math.inf
        for i in range(left, right):
            ans = min(ans, ( (mx_mp[(left, i)] * mx_mp[((i+1), right)]) + solveMem(memo, left, i) + solveMem(memo, i+1, right)) )
        
        ## store the computed state
        memo[left][right] = ans
        
        return memo[left][right]
    
    
    def solveTab(n):
        ## initializing the dp array
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for left in range(n-1, -1, -1):
            for right in range(left, n):
                if left == right:
                    continue
                else:
                    ans = math.inf
                    for i in range(left, right):
                        ans = min(ans, (mx_mp.get((left, i), 0)) * mx_mp.get((i+1, right), 0) + dp[left][i] + dp[i+1][right])
                    
                    dp[left][right] = ans
        
        return dp[0][n-1]
    
    ## initializing the memo array of nXn
    memo = [[None]*n for _ in range(n)]
    
    return solveMem(memo, 0, n-1), solveTab(n)

arr = [6, 2, 4]
res = mctFromLeafValues(arr)
print(res)

















