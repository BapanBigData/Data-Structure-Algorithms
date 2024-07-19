import math

## **Coin change problem**
def coinChange(coins: list[int], amount: int) -> int:
    
    def solveMem(memo, amt):
        ## b.c
        if amt == 0:
            return 0
        
        ## check if the state is already computed
        if memo[amt] is not None:
            return memo[amt]
        
        mn = math.inf
        for coin in coins:
            if (amt - coin) >= 0:
                mn = min(mn, 1 + solveMem(memo, amt-coin))
        
        ## store the computed state
        memo[amt] = mn
        
        return mn
    
    ## let' initialize the memo array
    memo = [None]*(amount+1)
    res = solveMem(memo, amount)
    
    return -1 if res == math.inf else res  

# coins = [1, 2, 5]; amount = 11
# minCoins = coinChange(coins, amount)
# print(minCoins)


## ** 518. Coin Change II **
def coinChangeII(coins: list[int], amount: int) -> int:
    n = len(coins)
    
    def solveMem(memo, i, amt):
        ## base cases
        if amt == 0:
            return 1
        
        if i == n:
            return 0
        
        ## check if the state is already computed
        if memo[i][amt] is not None:
            return memo[i][amt]
        
        option1, option2 = 0, 0
        
        if (amt - coins[i]) >= 0:
            option1 = solveMem(memo, i, amt - coins[i])
        
        if (i + 1) < n:
            option2 = solveMem(memo, i+1, amt)
        
        ## store the computed state
        memo[i][amt] = option1 + option2
        
        return memo[i][amt]
    
    
    def solveTab(n):
        ## initializing the dp array
        dp = [[0]*(amount+1) for _ in range(n+1)]
        
        ## base case
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(n-1, -1, -1):
            for amt in range(1, amount+1):
                option1, option2 = 0, 0
                
                if (amt - coins[i]) >= 0:
                    option1 = dp[i][amt-coins[i]]
                
                if (i+1) < n:
                    option2 = dp[i+1][amt]
                
                dp[i][amt] = option1 + option2
        
        return dp[0][amount]
    
    
    def spaceOpt(n):
        ## lets initialize two rows prev and curr
        prev = [0]*(amount+1)
        curr = [0]*(amount+1)
        
        ## base case
        prev[0] = curr[0] = 1
        
        for i in range(n-1, -1, -1):
            for amt in range(1, amount+1):
                option1, option2 = 0, 0
                
                if (amt - coins[i]) >= 0:
                    option1 = curr[amt-coins[i]]
                
                if (i+1) < n:
                    option2 = prev[amt]
                
                curr[amt] = option1 + option2
            
            prev = curr[:]
        
        return prev[amount]
    
    ## let's initializing the memo array
    memo = [[None]*(amount+1) for _ in range(n)]
    
    return solveMem(memo, 0, amount), solveTab(n), spaceOpt(n)


coins = [1, 2, 3, 7, 5]; amount = 727
print(coinChangeII(coins, amount))