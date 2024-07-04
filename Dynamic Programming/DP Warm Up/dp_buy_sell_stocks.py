import math

## **121. Best Time to Buy and Sell Stock**
def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    mn = prices[0]
    profit = 0
    for i in range(1, n):
        sell = prices[i]
        buy = mn
        profit = max(profit, (sell-buy))
        mn = min(mn, prices[i])
    
    return profit

# nums = [7, 1, 5, 3, 6, 4]
# print(maxProfit(nums))
###########################################################################################################
## **122. Best Time to Buy and Sell Stock II**
def buySellStockII(prices: list[int]) -> int:
    n = len(prices)
    
    def solveMem(memo, i, buy):
        ## base case
        if i == n:
            return 0 
        
        ## check if the state is already computed
        if memo[i][buy] is not None:
            return memo[i][buy]
        
        profit = 0
        
        if buy:
            incl = -prices[i] + solveMem(memo, i+1, 0)  ## buying the stock
            excl = 0 + solveMem(memo, i+1, 1)           ## ignoring the buy
            profit = max(profit, max(incl, excl))
        else:
            incl = prices[i] + solveMem(memo, i+1, 1)  ## selling the stock
            excl = 0 + solveMem(memo, i+1, 0)          ## ignoring the sell
            profit = max(profit, max(incl, excl))
        
        ## store the computed state
        memo[i][buy] = profit
        
        return memo[i][buy]
    
    
    def solveTab(n):
        ## initializing the dp array
        dp = [[0]*2 for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                profit = 0
                
                if buy:
                    incl = -prices[i] + dp[i+1][0]  
                    excl = 0 + dp[i+1][1]           
                    profit = max(profit, max(incl, excl))
                else:
                    incl = prices[i] + dp[i+1][1]
                    excl = 0 + dp[i+1][0]
                    profit = max(profit, max(incl, excl))
                
                dp[i][buy] = profit
        
        return dp[0][1]
    
    
    def spaceOpt(n):
        ## initializinng two vars prev and curr
        prev = [0]*2
        curr = [0]*2 
        
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                profit = 0
                
                if buy:
                    incl = -prices[i] + prev[0]
                    excl = 0 + prev[1]
                    profit = max(profit, max(incl, excl))
                else:
                    incl = prices[i] + prev[1]
                    excl = 0 + prev[0]
                    profit = max(profit, max(incl, excl))
                
                curr[buy] = profit
            
            prev = curr[:]
        
        return prev[1]   
    
    ## initializing the memo array
    memo = [[None]*2 for _ in range(n)]
    
    return solveMem(memo, 0, 1), solveTab(n), spaceOpt(n)

# nums = [7, 1, 5, 3, 6, 4]
# res = buySellStockII(nums)
# print(res)
##########################################################################################################################
## **123. Best Time to Buy and Sell Stock III**
def buySellStockIII(prices: list[int]) -> int:
    n = len(prices)
    
    def solveMem(memo, i, buy, limit):
        ## base cases
        if i == n:
            return 0
        
        if limit == 0:
            return 0
        
        ## check if the state is already computed
        if memo[i][buy][limit] is not None:
            return memo[i][buy][limit]
        
        profit = 0
        
        if buy:
            incl = -prices[i] + solveMem(memo, i+1, 0, limit)
            excl = 0 + solveMem(memo, i+1, 1, limit)
            profit = max(profit, max(incl, excl))
        else:
            incl = prices[i] + solveMem(memo, i+1, 1, limit-1)  ## 1 transaction is complete when sell done!
            excl = 0 + solveMem(memo, i+1, 0, limit)
            profit = max(profit, max(incl, excl))
        
        ## store the computed state
        memo[i][buy][limit] = profit
        
        return memo[i][buy][limit]
    
    
    def solveTab(n):
        ## initializing the dp array of shape n X buy X limit
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                for limit in range(2, 0, -1):
                    profit = 0
                    
                    if buy:
                        incl = -prices[i] + dp[i+1][0][limit]
                        excl = 0 + dp[i+1][1][limit]
                        profit = max(profit, max(incl, excl))
                    else:
                        incl = prices[i] + dp[i+1][1][limit-1]
                        excl = 0 + dp[i+1][0][limit]
                        profit = max(profit, max(incl, excl))
                    
                    dp[i][buy][limit] = profit
        
        return dp[0][1][2]
    
    ## space optimized bottom-up soln
    def spaceOpt(n):
        ## initializing prev and curr
        prev = [[0]*3 for _ in range(2)]
        curr = [[0]*3 for _ in range(2)]
        
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                for limit in range(2, 0, -1):
                    profit = 0
                    
                    if buy:
                        incl = -prices[i] + prev[0][limit]
                        excl = 0 + prev[1][limit]
                        profit = max(profit, max(incl, excl))
                    else:
                        incl = prices[i] + prev[1][limit-1]
                        excl = 0 + prev[0][limit]
                        profit = max(profit, max(incl, excl))
                    
                    curr[buy][limit] = profit
                
                prev = curr[:]
        
        return prev[1][2]
    
    ## initializing a 3D memo array of shape n X buy X limit
    memo = [[[None]*3 for _ in range(2)] for _ in range(n)]
    
    return solveMem(memo, 0, 1, 2), solveTab(n), spaceOpt(n)

# prices = [1, 2, 3, 4, 5]
# res = buySellStockIII(prices)
# print(res)
#####################################################################################################################
## **Best Time to Buy and Sell Stock IV**

def buySellStockIV(prices: list[int], k: int) -> int:
    n = len(prices)
    
    def solveMem(memo, i, buy, limit):
        ## base cases
        if i == n:
            return 0
        
        if limit == 0:
            return 0
        
        ## check if the state is already computed
        if memo[i][buy][limit] is not None:
            return memo[i][buy][limit]
        
        profit = 0
        
        if buy:
            incl = -prices[i] + solveMem(memo, i+1, 0, limit)
            excl = 0 + solveMem(memo, i+1, 1, limit)
            profit = max(profit, max(incl, excl))
        else:
            incl = prices[i] + solveMem(memo, i+1, 1, limit-1)  ## 1 transaction is complete when sell done!
            excl = 0 + solveMem(memo, i+1, 0, limit)
            profit = max(profit, max(incl, excl))
        
        ## store the computed state
        memo[i][buy][limit] = profit
        
        return memo[i][buy][limit]
    
    
    def solveTab(n, k):
        ## initializing the dp array of shape n X buy X k
        dp = [[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                for limit in range(k, 0, -1):
                    profit = 0
                    
                    if buy:
                        incl = -prices[i] + dp[i+1][0][limit]
                        excl = 0 + dp[i+1][1][limit]
                        profit = max(profit, max(incl, excl))
                    else:
                        incl = prices[i] + dp[i+1][1][limit-1]
                        excl = 0 + dp[i+1][0][limit]
                        profit = max(profit, max(incl, excl))
                    
                    dp[i][buy][limit] = profit
        
        return dp[0][1][k]
    
    ## space optimized bottom-up soln
    def spaceOpt(n, k):
        ## initializing prev and curr
        prev = [[0]*(k+1) for _ in range(2)]
        curr = [[0]*(k+1) for _ in range(2)]
        
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                for limit in range(k, 0, -1):
                    profit = 0
                    
                    if buy:
                        incl = -prices[i] + prev[0][limit]
                        excl = 0 + prev[1][limit]
                        profit = max(profit, max(incl, excl))
                    else:
                        incl = prices[i] + prev[1][limit-1]
                        excl = 0 + prev[0][limit]
                        profit = max(profit, max(incl, excl))
                    
                    curr[buy][limit] = profit
                
                prev = curr[:]
        
        return prev[1][k]
    
    ## initializing a 3D memo array of shape n X buy X k
    memo = [[[None]*(k+1) for _ in range(2)] for _ in range(n)]
    
    return solveMem(memo, 0, 1, k), solveTab(n, k), spaceOpt(n, k)

# prices = [2,4,1]; k = 2
# res = buySellStockIV(prices, k)
# print(res)
##################################################################################################################################
## **714. Best Time to Buy and Sell Stock with Transaction Fee**
## **Buy & Sell Stocks Part V
def buySellStockV(prices: list[int], fee: int) -> int:
    
    n = len(prices)
    
    def solveMem(memo, i, buy):
        ## base case
        if i == n:
            return 0 
        
        ## check if the state is already computed
        if memo[i][buy] is not None:
            return memo[i][buy]
        
        profit = 0
        
        if buy:
            incl = -prices[i] + solveMem(memo, i+1, 0)  
            excl = 0 + solveMem(memo, i+1, 1)           
            profit = max(profit, max(incl, excl))
        else:
            incl = prices[i] - fee + solveMem(memo, i+1, 1)  ## one transaction completed have to give the fee
            excl = 0 + solveMem(memo, i+1, 0)          
            profit = max(profit, max(incl, excl))
        
        ## store the computed state
        memo[i][buy] = profit
        
        return memo[i][buy]
    
    def solveTab(n):
        ## initializing the dp array
        dp = [[0]*2 for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                profit = 0
                
                if buy:
                    incl = -prices[i] + dp[i+1][0]  
                    excl = 0 + dp[i+1][1]           
                    profit = max(profit, max(incl, excl))
                else:
                    incl = prices[i] - fee + dp[i+1][1]
                    excl = 0 + dp[i+1][0]
                    profit = max(profit, max(incl, excl))
                
                dp[i][buy] = profit
        
        return dp[0][1]
    
    ## space optimized bottom-up soln
    def spaceOpt(n):
        ## initializinng two vars prev and curr
        prev = [0]*2
        curr = [0]*2 
        
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                profit = 0
                
                if buy:
                    incl = -prices[i] + prev[0]
                    excl = 0 + prev[1]
                    profit = max(profit, max(incl, excl))
                else:
                    incl = prices[i] - fee + prev[1]
                    excl = 0 + prev[0]
                    profit = max(profit, max(incl, excl))
                
                curr[buy] = profit
            
            prev = curr[:]
        
        return prev[1] 
    
    ## initializing the memo array
    memo = [[None]*2 for _ in range(n)]
    
    return solveMem(memo, 0, 1), solveTab(n), spaceOpt(n)

prices = [1,3,2,8,4,9]; fee = 2
res = buySellStockV(prices, fee)
print(res)