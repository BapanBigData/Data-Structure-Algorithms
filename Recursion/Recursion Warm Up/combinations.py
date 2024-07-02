## Leetcode: 77. Combinations
## Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.
## You may return the answer in any order.

def combinations(n: int, k: int) -> list[list[int]]:
    
    def solver(start, k, ans, res):
        ## base case
        if k == 0:
            res.append(ans)
            return res
        
        for i in range(start, n+1):
            solver(i+1, k-1, ans + [i], res)
        
        return res
    
    return solver(1, k, [], [])


## let's calculate number of function calls of the above function
def numFunctionCalls(n: int, k: int) -> int:
    
    def solver(start, k):
        cnt = 0
        ## base case
        if k == 0:
            return 1
        
        for i in range(start, n+1):
            cnt += solver(i+1, k-1)
        
        return cnt
    
    return solver(1, k)

# n = 10;  k = 6
# # print(combinations(n, k))
# nCk = numFunctionCalls(n, k)
# print(nCk)
##--------------------------------------------------------------------------------------------------------------------------
## 216. Combination Sum III
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
def combinationSum3(k: int, n: int) -> list[list[int]]:
    
    def solver(start, k, n, ans, res):
        ## base case
        if k == 0 and n == 0:
            res.append(ans)
            return res
        
        for i in range(start, 10):
            if i <= n:
                solver(i+1, k-1, n-i, ans + [i], res)
        
        return res
    
    return solver(1, k, n, ans=[], res=[])


k = 3; n = 13
print(combinationSum3(k, n))