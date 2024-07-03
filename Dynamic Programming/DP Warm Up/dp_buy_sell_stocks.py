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
    pass