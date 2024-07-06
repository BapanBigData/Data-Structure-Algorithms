import math

## **53. Maximum Subarray**
## Given an integer array nums, find the subarray with the largest sum, and return its sum.
def maxSubArray(nums: list[int]) -> int:
    n = len(nums)
    
    def bruteForce():
        mx = -math.inf
        
        for i in range(n):
            for j in range(i, n):
                s = 0
                for k in range(i, j):
                    s += nums[k]
                
                mx = max(mx, s)
        
        return mx
    
    ## better
    def solver():
        mx = -math.inf
        
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                mx = max(mx, s)
        
        return mx
    
    def kadanes_algo():
        mx = -math.inf
        s = 0
        
        for i in range(n):
            if s < 0:
                s = 0
            
            s += nums[i]
            mx = max(mx, s)
        
        return mx
    
    return kadanes_algo()

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# res = maxSubArray(nums)
# print(res)

###############################################################################
## ** Length of the maximum subarray
def maxSubArrayLength(nums: list[int]):
    n = len(nums)
    indx_start, indx_end = -1, -1
    
    mx = -math.inf
    s = 0
    
    for i in range(n):
        if s == 0:
            start = i
        
        s += nums[i]
        
        if s > mx:
            mx = s
            indx_start = start
            indx_end = i
        
        if s < 0:
            s = 0
            
    return indx_start, indx_end


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
indx = maxSubArrayLength(nums)
print(indx)
###########################################################################
## **Valid Parentheses**

def validParentheses(s: str) -> bool:
    
    def balanced(close, open):
        return (close == ')' and open == '(') or (close == '}' and open == '{') or (close == ']' and open == '[')
    
    def solver():
        ## initializing a stack
        stack = []
        
        for e in s:
            if e in ('(', '{', '['):
                stack.append(e)
            else:
                if not stack:
                    return False
                else:
                    if not balanced(e, stack[-1]):
                        return False
                    else:
                        stack.pop()
        
        if stack:
            return False
        
        return True
    
    return solver()

# s = '(]'
# res = validParentheses(s)
# print(res)

## fibonacci
def fib(n: int):
    if n == 1:
        return [0]
    
    a = 0
    b = 1
    dp = [0, 1]
    
    for _ in range(2, n):
        c = a  + b
        dp.append(c)
        
        a = b
        b = c
    
    return dp

n = 1
series = fib(n)
print(series)