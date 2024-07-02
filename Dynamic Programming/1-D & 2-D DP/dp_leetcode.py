import math

## 198. House Robber:

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
# it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
## return the maximum amount of money you can rob tonight without alerting the police.

def houseRob(nums: list):
    
    def top_down_dp(memo, i, n):
        ## base cases
        if i == n-1:
            memo[i] = nums[i]
            return memo[i]
        
        if i == n-2:
            memo[i] = max(nums[i], nums[i+1])
            return memo[i]
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        robbed = 0
        no_robbed = 0
        
        if i < n:
            no_robbed = 0 + top_down_dp(memo, i+1, n)
        
        if i+1 < n:
            robbed = nums[i] + top_down_dp(memo, i+2, n)
        
        ## store the computation
        memo[i] = max(no_robbed, robbed)
        
        return memo[i]
    
    def bottom_up_dp(n):
        ## initializing the dp array
        dp = [None]*n
        
        ## filling the base cases
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-1], nums[n-2])
        
        for i in range(n-3, -1, -1):
            
            no_robbed = 0 + dp[i+1]
            robbed = nums[i] + dp[i+2]
            
            dp[i] = max(no_robbed, robbed)
        
        return dp[0]
    
    def space_opt(n):
        ## base cases
        a = nums[n-1]
        b = max(nums[n-1], nums[n-2])
        
        for i in range(n-3, -1, -1):
            
            no_robbed = 0 + b
            robbed = nums[i] + a
            
            a = b
            b = max(robbed, no_robbed)
        
        return b
    
    n = len(nums)
    memo = [None]*n
    
    return top_down_dp(memo, 0, n)

# nums = [1, 2, 5, 6, 7, 12, 0, 3]
nums1 = [1, 2, 1]
nums2 = [2, 1, 1]
ans1 = houseRob(nums1)
ans2 = houseRob(nums2)
print(ans1)
print(ans2)
# print(houseRob(nums))
########################################################################################################################################
## 213. House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

def houseRob2(nums: list):
    
    def top_down_dp(memo, i, n):
        ## base cases
        if i == n-1:
            memo[i] = nums[i]
            return memo[i]
        
        if i == n-2:
            memo[i] = max(nums[i], nums[i+1])
            return memo[i]
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        robbed = 0
        no_robbed = 0
        
        if i < n:
            no_robbed = 0 + top_down_dp(memo, i+1, n)
        
        if i+1 < n:
            robbed = nums[i] + top_down_dp(memo, i+2, n)
        
        ## store the computation
        memo[i] = max(no_robbed, robbed)
        
        return memo[i]
    
    n = len(nums)
    
    if n == 1:
        return nums[0]
    
    memo1 = [None]*n
    memo2 = [None]*n
    
    last_exclude = top_down_dp(memo1, 0, n-1)
    last_include = top_down_dp(memo2, 1, n)
    
    return max(last_exclude, last_include)


nums = [1, 2, 1, 1]
ans = houseRob2(nums)
print(ans)