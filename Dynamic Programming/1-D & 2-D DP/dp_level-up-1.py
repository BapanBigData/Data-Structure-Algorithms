import math

## maximum non-adjacent sum
## bottom-up solution
def max_sum_non_adjacent_bottom_up(nums: list) -> int:
    ## recurrence relation
    ## dp[i] = max(nums[i]+dp[i-1], dp[i-1])
    ## here dp[i] is storing the maximum non-adjacent sum till that index i
    
    n = len(nums)
    dp = [0] * n
    
    ## corner cases
    if n == 1:
        return max(0, nums[0])
    
    if n == 2:
        return max(0, max(nums[0], nums[1]))
    
    ## bottom-up logic
    dp[0] = max(0, nums[0])
    dp[1] = max(dp[0], nums[1])
    
    for i in range(2, n):
        inc = nums[i] + dp[i-2]
        exc = dp[i-1]
        dp[i] = max(inc, exc)
    
    return dp[n-1]

## Top-Down solution
def max_sum_non_adjacent_top_down(nums: list) -> int:
    
    def top_down_dp(memo, i, nums):
        ## base cases
        if i < 0:
            return 0
        
        if i == 0:
            memo[i] = max(0, nums[i])
            return memo[i]
        
        if i == 1:
            memo[i] = max(0, max(nums[0], nums[1]))
            return memo[i]
        
        ## check if the state is already computed
        if memo[i] is not None:
            return memo[i]
        
        ## at index i there are two options -> 
        ## 1. include the element at index i in the sum
        ## 2. exclude the element in the sum
        ## if we include the element at index i, then we should not include 
        ## the adjacent element of it i.e (i-1) in the sum, and if we exclude 
        ## the element at index i, then we have to consider the element at (i-1).
        ## Because two adjacent elements are not consider in the sum
        
        inc = nums[i] + top_down_dp(memo, i-2, nums)
        exc = top_down_dp(memo, i-1, nums)
        
        ## storing the state
        memo[i] = max(inc, exc)
        
        return memo[i]
    
    n = len(nums)
    memo = [None] * n
    top_down_dp(memo, n-1, nums)
    return memo[n-1]
            

# nums = [6, 10, 12, 7, 9, 14]
# # nums = [6, 10]
# res = max_sum_non_adjacent_top_down(nums)
# print(res) 

## -----------------------------------------------------------------------------------------------------
## Longest Increasing Subsequence
## bottom-up solution
def longest_increasing_subsequence_bottom_up(arr: list) -> int:
    n = len(arr)
    
    ## initializing the dp array
    dp = [1] * n
    lic = 1
    
    ## bottom up logic
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                ## dp[i] stores length of LIC ending at array of index i
                dp[i] = max(dp[i], 1+dp[j])
                lic = max(lic, dp[i])
    
    return lic


def longest_increasing_subsequence_top_down(arr: list) -> int:
    pass

# arr = [50, 4, 10, 8, 30, 100, 2]
# print(longest_increasing_subsequence_bottom_up(arr))

##---------------------------------------------------------------------------------------------------------
## Box Stacking Problem
## Bottom-Up DP Solution
## Top-Down Dp HW:
def can_place(box1: list, box2: list):
    if box1[0] > box2[0] and box1[1] > box2[1] and box1[2] > box2[2]:
        return True
    return False

def box_stacking_bottom_up(boxes: list[list[int]]) -> int:
    n = len(boxes)
    
    ## sort the boxes based on the height of each box
    boxes.sort(key=lambda box: box[-1])
    
    ## assigning the dp array
    dp = [0] * n
    
    for i in range(n):
        dp[i] = boxes[i][-1]
        
    ## initializing the max height that can stacked    
    max_height = dp[0]
    
    for i in range(1, n):
        ## check all the boxes before box i
        for j in range(i):
            if can_place(boxes[i], boxes[j]):
                current_height = boxes[i][-1]
                dp[i] = max(dp[j]+current_height, dp[i])
                max_height = max(dp[i], max_height)
                
    return max_height
            
# boxes = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
# height = box_stacking_bottom_up(boxes)
# print(height)

##----------------------------------------------------------------------------------------------------------
## Count Binary Search Trees (BST)
## Top-Down DP Solution
## T.C: O(n^2)
def count_trees_top_down(n: int) -> int:
    
    def top_down_dp(memo, n):
        ## base case
        if n == 0 or n == 1:
            memo[n] = 1
            return memo[n]
        
        ## check if the state is already computed
        if memo[n] is not None:
            return memo[n]
        
        cnt = 0
        for i in range(1, n+1):
            x = top_down_dp(memo, i-1)
            y = top_down_dp(memo, n-i)
            cnt += (x*y)
            
        ## store the computed state
        memo[n] = cnt
        return memo[n]
    
    memo = [None] * (n+1)
    top_down_dp(memo, n)
    return memo[n]


## Bottom-Up DP Solution
## T.C: O(n^2)
def count_trees_bottom_up(N: int) -> int:
    ## assigning the dp array
    dp = [0] * (N+1)
    ## base case 
    dp[0] = dp[1] = 1
    
    for n in range(2, N+1):
        for i in range(1, n+1):
            x = dp[i-1]
            y = dp[n-i]
            dp[n] += (x*y)
            
    return dp[N]

trees_top_down = count_trees_top_down(7)
trees_bottom_up = count_trees_bottom_up(7)
print("Count Top Down:", trees_top_down)
print("Count Bottom Up:", trees_bottom_up)