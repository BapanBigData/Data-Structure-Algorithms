import math
from collections import deque

## Fibonacci series (Tabulation) space optimization
def fib_series(n: int):
    if n == 0:
        return 0
    
    ## base cases
    a = 0
    b = 1
    for _ in range(2, n+1):
        curr = a + b
        a = b
        b = curr
    
    return b

# n = 6
# res = fib_series(n)
# print(res)
##--------------------------------------------------------------------------------------------------------
def stairs_climbing(n: int):
    
    def solver(i, n):
        ## base case
        if i == n:
            return 1
        
        if i > n:
            return 0
        
        return solver(i+1, n) + solver(i+2, n)
    
    return solver(0, n)


def min_cost_stairs_climbing(cost: list):
    
    def solve(memo, cost, n):
        ## base cases
        if n == 0:
            memo[0] = cost[0]
            return memo[0]
        
        if n == 1:
            memo[1] = cost[1]
            return memo[1]
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        ans = cost[n] + min(solve(memo, cost, n-1), solve(memo, cost, n-2))
        memo[n] = ans
        
        return memo[n]
    
    n = len(cost)
    
    ## initializing the memo array
    memo = [None] * (n+1)
    
    ## f(n) = min(f(n-1), f(n-2)), for sate n
    ans = min(solve(memo, cost, n-1), solve(memo, cost, n-2))
    memo[n] = ans
    
    return memo[n]


def min_cost_stairs_climbing_tabulation(cost: list):
    nStairs = len(cost)
    
    ## initializing the dp array
    dp = [0] * (nStairs+1)
    
    ## base cases
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2, nStairs):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    ## for nth stair
    dp[nStairs] = min(dp[nStairs-1], dp[nStairs-2])
    
    return dp[nStairs]

## space optimization
def min_cost_stairs_climbing_space_optimization(cost: list):
    n = len(cost)
    
    ## base cases
    a = cost[0]
    b = cost[1]
    
    for i in range(2, n):
        curr = cost[i] + min(a, b)
        a = b
        b = curr
    
    return min(a, b)

# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# min_cost = min_cost_stairs_climbing_space_optimization(cost)
# print(min_cost)
##-----------------------------------------------------------------------------------------------------
## minimum number of coins
def min_coins(coins: list, amount: int):
    
    def solve_memo(memo, coins, amount):
        ## base case
        if amount == 0:
            memo[0] = 0
            return memo[0]
        
        ## check if the state is already computed
        if memo[amount] is not None:
            return memo[amount]
        
        mn = math.inf
        for coin in coins:
            if (amount - coin) >= 0:
                f = solve_memo(memo, coins, amount-coin)
                mn = min(mn, f)
        
        ## store the compute
        memo[amount] = 1 + mn
        
        return memo[amount]
    
    def solve_tabulation(coins, amount):
        ## initializing the dp array
        dp = [math.inf] * (amount+1)
        
        ## base case
        dp[0] = 0
        
        ## for each amount i, there are len(coins) possibilities
        for i in range(1, amount+1):
            mn = dp[i]
            for coin in coins:
                if (i - coin) >= 0:
                    mn = min(mn, dp[i-coin])
                    
            dp[i] = 1 + mn
        
        return dp[amount]
    
    ## initializing the memo array
    # memo = [None] * (amount+1)
    # solve_memo(memo, coins, amount)
    
    # return memo[amount] if memo[amount] != math.inf else -1
    
    tabulation = solve_tabulation(coins, amount)
    
    return tabulation if tabulation != math.inf else -1

# coins = [6, 3, 7]
# amount = 79
# res = min_coins(coins, amount)
# print(res)
##---------------------------------------------------------------------------------------------------------
## Maximum Sum Of Non-Adjacent Elements:
def max_sum_non_adjacent_elements(nums: list):
    
    def solve_memo(memo, i, nums):
        ## base cases
        if i < 0:
            return 0
        
        if i == 0:
            memo[i] = nums[i]
            return memo[i]
        
        if i == 1:
            memo[i] = max(nums[i], nums[i-1])
            return memo[i]
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        ## there are two options, either include the current element or exclude it
        inc = nums[i] + solve_memo(memo, i-2, nums)
        exc = 0 + solve_memo(memo, i-1, nums)
        
        memo[i] = max(inc, exc)
        
        return memo[i]
    
    def solve_tabulation(nums, n):
        ## initializing the dp array
        dp = [0] * n
        
        ## base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            ## there are two options, either include the current element or exclude it
            inc = nums[i] + dp[i-2]
            exc = 0 + dp[i-1]
            
            dp[i] = max(inc, exc)
        
        return dp[n-1]
    
    def solve_space_optimization(nums, n):
        ## base cases
        a = nums[0]
        b = max(nums[0], nums[1])
        
        for i in range(2, n):
            ## there are two options, either include the current element or exclude it
            inc = nums[i] + a
            exc = 0 + b
            
            a = b
            b = max(inc, exc)
        
        return b
            
    
    n = len(nums)
    
    # ## initializing the memo array
    memo = [None] * n
    solve_memo(memo, n-1, nums)
    
    # return memo
    
    res_tab = solve_tabulation(nums, n)
    space_opt = solve_space_optimization(nums, n)
    return memo[n-1], res_tab, space_opt

# nums = [9, 9, 8, 2, 0, 2, 1, 5, 9, 12, 10, 7, 8, 2, 16]
# res = max_sum_non_adjacent_elements(nums)
# print(res)
##----------------------------------------------------------------------------------------------------
## House Robbery: Maximum money -> non-adjacent house, can't consider first and last house together
## because houses are arranged in a circular way
def max_money(nums: list):
    
    def solve(nums, n):
        ## base cases
        a = nums[0]
        b = max(nums[0], nums[1])
        
        for i in range(2, n):
            ## there are two options, either include the current element or exclude it
            inc = nums[i] + a
            exc = 0 + b
            
            a = b
            b = max(inc, exc)
        
        return b
    
    n = len(nums)
    
    if n == 1:
        return nums[0]
    
    first = [0]*n
    last = [0]*n
    
    for i in range(n):
        if i != n-1:
            first[i] = nums[i]
        
        if i != 0:
            last[i] = nums[i]
    
    incl_first = solve(first, n)
    excl_first = solve(last, n)
    
    return max(incl_first, excl_first)

# nums = [8, 7]    
# ans = max_money(nums)
# print(ans)
##-----------------------------------------------------------------------------------------------------
## Rod Cutting into the segments
def max_segments(n: int, x: int, y: int, z: int):
    
    def solve_memo(memo, n, x, y, z):
        ## base cases
        if n < 0:
            return -math.inf
        
        if n == 0:
            memo[n] = 0
            return memo[n]
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        a = solve_memo(memo, n-x, x, y, z)
        b = solve_memo(memo, n-y, x, y, z)
        c = solve_memo(memo, n-z, x, y, z)
        
        ans = 1 + max(a, b, c)
        memo[n] = ans
        
        return memo[n]
    
    
    def solve_tabulation(n, x, y, z):
        ## initializing the dp array
        dp = [None]*(n+1)
        
        ## base case
        dp[0] = 0
        
        ## rod of length 1 to n
        for i in range(1, n+1):
            ## for rod length i, we have three options to cut it x, y, z
            a, b, c = -math.inf, -math.inf, -math.inf
            
            if (i - x) >= 0:
                a = dp[i-x]
            
            if (i - y) >= 0:
                b = dp[i-y]
            
            if (i - z) >= 0:
                c = dp[i-z]
            
            dp[i] = 1 + max(a, b, c)
        
        return dp
            
    ## initializing the memo array
    memo = [None] * (n+1)
    solve_memo(memo, n, x, y, z)
    
    # return memo
    
    res_tab = solve_tabulation(n, x, y, z)
    return memo, res_tab
    
# ans = max_segments(22, 3, 2, 3)
# print(ans)    
##----------------------------------------------------------------------------------------------------
## Count Dearrangement
def cnt_dearrangement(n: int):
    
    MOD = (10 ** 9) + 7
    
    def solve_memo(memo, n):
        ## base case
        if n == 1:
            memo[n] = 0
            return memo[n]
        
        if n == 2:
            memo[n] = 1
            return memo[n]
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        ans = ((n-1) * solve_memo(memo, n-2)) % MOD + ((n-1) * solve_memo(memo, n-1)) % MOD
        memo[n] = ans % MOD
        
        return memo[n]
    
    def solve_tabulation(n):
        if n == 1:
            return 0
        
        ## initializing the dp array
        dp = [None] * (n+1)
        
        ## base cases
        dp[1] = 0
        dp[2] = 1
        
        for i in range(3, n+1):
            ans = ((i-1) * dp[i-2]) % MOD + ((i-1) * dp[i-1]) % MOD
            dp[i] = ans % MOD
        
        return dp[n]
    
    
    def solve_opt_space(n):
        if n == 1:
            return 0
        
        ## base cases
        a = 0
        b = 1
        
        for i in range(3, n+1):
            ans = ((i-1) * a) % MOD + ((i-1) * b) % MOD
            a = b
            b = ans % MOD
        
        return b
    
    ## initializing the memo array
    memo = [None] * (n+1)
    solve_memo(memo, n)
    
    tab = solve_tabulation(n)
    opt = solve_opt_space(n)
    
    return memo[n], tab, opt

# cnt = cnt_dearrangement(9)
# print(cnt)
##----------------------------------------------------------------------------------------------------------
## Painting Fence Algorithm:
def cnt_combinations(n: int, k: int):
    
    MOD = (10 ** 9) + 7
    
    def solve_memo(memo, n, k):
        ## base cases
        if n == 1:
            memo[n] = k
            return memo[n]
        
        if n == 2:
            memo[n] = k ** 2
            return memo[n]
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        same = (solve_memo(memo, n-2, k) * (k-1)) % MOD
        diff = (solve_memo(memo, n-1, k) * (k-1)) % MOD
        total = (same + diff) % MOD
        
        memo[n] = total
        
        return memo[n]
    
    
    def solve_tabulation(n, k):
        if n == 1:
            return k
        
        ## initializing the dp array
        dp = [None] * (n+1)
        
        ## base cases
        dp[1] = k
        dp[2] = (k ** 2)
        
        for i in range(3, n+1):
            same = (dp[i-2] * (k - 1)) % MOD
            diff = (dp[i-1] * (k - 1)) % MOD
            total = (same + diff) % MOD
            dp[i] = total
        
        return dp[n]
    
    def solve_space_optimal(n, k):
        if n == 1:
            return k
        
        ## base cases
        a = k
        b = (k ** 2)
        
        for _ in range(3, n+1):
            same = (a * (k - 1)) % MOD
            diff = (b * (k - 1))  % MOD
            total = (same + diff) % MOD
            
            a = b
            b = total
        
        return b
    
    ## initializing the memo array
    memo = [None] * (n+1)
    solve_memo(memo, n, k)
    
    tab = solve_tabulation(n, k)
    opt = solve_space_optimal(n, k)
    
    return memo[n], tab, opt

# n, k = 2, 12
# combies = cnt_combinations(n, k)
# print(combies)
##----------------------------------------------------------------------------------------------------------
## Combination Sum IV: 
## nums = [1, 2, 3], target = 4
## o/p: -> [1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [2, 1, 1], [3, 1], [1, 2, 1]
## Note: here [1, 1, 2] and [2, 1, 1] are two different ways and so...
def combination_sum(nums: list, target: int):
    
    MOD = (10 ** 9) + 7
    
    def solve_memo(memo, tar, n):
        ## base case
        if tar < 0:
            return 0
        
        if tar == 0:
            memo[tar] = 1
            return memo[tar]
        
        ## check if the state is already computed
        if memo[tar] is not None:
            return memo[tar]
        
        ans = 0
        for i in range(n):
            ans += solve_memo(memo, tar-nums[i], n) % MOD
            
        memo[tar] = ans % MOD
        
        return memo[tar]
    
    def solve_tabulation(tar, n):
        ## initializing the dp array
        dp = [0] * (tar+1)
        
        ## base case
        dp[0] = 1
        
        for t in range(1, tar+1):
            ans = 0
            for i in range(n):
                if (t-nums[i]) >= 0:
                    ans += dp[t-nums[i]] % MOD
            
            dp[t] = ans % MOD
        
        return dp[tar]
    
    
    n = len(nums)
    
    ## initializing the memo array
    memo = [None] * (target+1)
    solve_memo(memo, target, n)
    
    tab = solve_tabulation(target, n)
    
    return memo[target], tab

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 24
# memo, tab = combination_sum(arr, target)
# print(memo)
# print(tab)
##---------------------------------------------------------------------------------------------------------
## Perfect Square Problem:
def get_min_squares(n: int):
    
    def solve_memo(memo, n):
        ## base case
        if n == 0:
            memo[n] = 0
            return memo[n]
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        i = 1
        ans = n
        while (i*i) <= n:
            sm_out = 1 + solve_memo(memo, n-(i*i))
            ans = min(ans, sm_out)
            
            i += 1
        
        memo[n] = ans
        
        return memo[n]
    
    def solve_tabulation(n):
        ## initializing the dp array
        dp = [None] * (n+1)
        
        ## base case
        dp[0] = 0
        
        for i in range(1, n+1):
            ans = i
            j = 1
            while (j*j) <= i:
                sm_out = 1 + dp[i-(j*j)]
                ans = min(ans, sm_out)
                
                j += 1
            
            dp[i] = ans
            
        return dp[n]
    
    ## initializing the memo array
    # memo = [None] * (n+1)
    # solve_memo(memo, n)
    
    tab = solve_tabulation(n)
    
    return tab

# n = 3337
# tab = get_min_squares(n)
# print(tab)     
##----------------------------------------------------------------------------------------------------------
## **Minimum Cost For Tickets**:
def min_cost_tickets(days: list, cost: list):
    
    def solve_memo(memo, indx, n):
        ## base case
        if indx >= n:
            return 0
        
        ## check if the state is already computed
        if memo[indx] is not None:
            return memo[indx]
        
        ## 1-day pass
        pass_for_1_day = cost[0] + solve_memo(memo, indx+1, n)
        
        ## 7-day pass
        i = indx
        while (i < n) and (days[i] < days[indx] + 7):
            i += 1
            
        pass_for_7_day = cost[1] + solve_memo(memo, i, n)
        
        ## 30-day pass
        while (i < n) and (days[i] < days[indx] + 30):
            i += 1
        
        pass_for_30_day = cost[2] + solve_memo(memo, i, n)
        
        memo[indx] = min(pass_for_1_day, pass_for_7_day, pass_for_30_day)
        
        return memo[indx]
    
    
    def solve_tabulation(n):
        ## initializing the dp array
        dp = [None] * (n+1)
        
        ## base case
        dp[n] = 0
        
        indx = n-1
        while indx >= 0:
            ## 1-day pass
            pass_for_1_day = cost[0] + dp[indx+1]
            
            ## 7-day pass
            i = indx
            while (i < n) and (days[i] < days[indx] + 7):
                i += 1
            
            pass_for_7_day = cost[1] + dp[i]
            
            ## 30-day pass
            while (i < n) and (days[i] < days[indx] + 30):
                i += 1
            
            pass_for_30_day = cost[2] + dp[i]
            
            dp[indx] = min(pass_for_1_day, pass_for_7_day, pass_for_30_day)
            
            indx -= 1
        
        return dp[0]
    
    n = len(days)
    
    ## initializing the memo array
    memo = [None] * n
    solve_memo(memo, 0, n)
    
    tab = solve_tabulation(n)
    
    return memo[0], tab


def min_cost_tickets_space_optimal(days: list, cost: list):
    ans = 0
    
    ## initializing the deques
    ## monthly:-> pair (day, cost till that day)
    ## weekly:-> pair (day, cost till that day)
    monthly = deque()
    weekly = deque()
    
    for day in days:
        
        while len(monthly) > 0 and (monthly[0][0] + 30) <= day:
            monthly.popleft()
        
        while len(weekly) > 0 and (weekly[0][0] + 7) <= day:
            weekly.popleft()
        
        weekly.append([day, ans+cost[1]])
        monthly.append([day, ans+cost[2]])
        
        ## update the answer with minimum of daily cost, 
        ## cost by 7-day pass and cost by 30-day pass
        ans = min(ans+cost[0], monthly[0][1], weekly[0][1])
    
    return ans

days = [4, 5, 7, 8, 10, 17, 23, 32, 57, 82, 117, 147, 194, 224, 250, 298, 320, 361]
cost = [2, 7, 20]
res = min_cost_tickets_space_optimal(days, cost)      
print(res)
# print(memo)
# print(tab)  