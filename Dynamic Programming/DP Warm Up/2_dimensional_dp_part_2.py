import math

## **1388. Pizza With 3n Slices**
## Variation of House Robber II

def maxSizeSlices(slices: list[int]) -> int:
    
    k = len(slices)
    
    def solveMem(memo, arr, i, n):
        ## base case
        if (n == 0) or (i >= len(arr)):
            return 0
        
        ## check if the state is already computed
        if memo[i][n] is not None:
            return memo[i][n]
        
        ## include
        incl = arr[i] + solveMem(memo, arr, i+2, n-1)
        
        ## exclude
        excl = 0 + solveMem(memo, arr, i+1, n)
        
        ## store the computed state
        memo[i][n] = max(incl, excl)
        
        return memo[i][n]
    
    
    def solveTab(k, arr):
        m = len(arr)
        
        ## initializinng two dp arrays with zeros
        dp = [[0]*(k//3 + 1) for _ in range(m+2)]
            
        for i in range(m-1, -1, -1):
            for n in range(1, (k//3+1)):
                ## include
                incl = arr[i] + dp[i+2][n-1]
                
                ## exclude
                excl = 0 + dp[i+1][n]
                
                dp[i][n] = max(incl, excl)
        
        return dp[0][k//3]
    
    ## space optimal soln
    def spaceOpt(k, arr):
        m = len(arr)
        
        ## let's initialize 3 arrays, 2 previous and 1 current
        prev1 = [0]*(k//3 + 1)
        prev2 = [0]*(k//3 + 1)
        curr = [0]*(k//3 + 1)
        
        for i in range(m-1, -1, -1):
            for n in range(1, (k//3 + 1)):
                ## include
                incl = arr[i] + prev2[n-1]
                
                ## exclude
                excl = 0 + prev1[n]
                
                curr[n] = max(incl, excl)
            
            prev2 = prev1[:]
            prev1 = curr[:]
        
        return prev1[k//3]
    
    ## initializing 2 memo array for 2 cases
    memo1 = [[None]*(k//3 + 1) for _ in range(k-1)]
    memo2 = [[None]*(k//3 + 1) for _ in range(k-1)]
    
    case1 = solveMem(memo1, slices[:(k-1)], 0, k//3)
    case2 = solveMem(memo2, slices[1:], 0, k//3)
    
    bottom1 = spaceOpt(k, slices[:(k-1)])
    bottom2 = spaceOpt(k, slices[1:])
    
    return max(case1, case2), max(bottom1, bottom2)

# slices = [8,9,8,6,1,1]
# res = maxSizeSlices(slices)
# print(res)
################################################################################################################
## **Distinct Ways Pattern Dynamic Programming**
## **1155. Number of Dice Rolls With Target Sum**

def numRollsToTarget(n: int, k: int, target: int) -> int:
    MOD = (10 ** 9) + 7
    
    def solveMem(memo, i, tar):
        ## base cases
        if tar < 0:
            return 0
        
        if (i == 0) and (tar != 0):
            return 0
        
        if (tar == 0) and (i != 0):
            return 0
        
        if (tar == 0) and (i == 0):
            return 1
        
        ## check if the state is already computed
        if memo[i][tar] is not None:
            return memo[i][tar]
        
        ans = 0
        for face in range(1, k+1):
            ans += solveMem(memo, i-1, tar-face) 
        
        ## store the computed state
        memo[i][tar] = (ans % MOD)
        
        return memo[i][tar]
    
    
    def solveTab(n, k, target):
        ## initializing the dp array
        dp = [[0]*(target+1) for _ in range(n+1)]
        
        ## base case
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for tar in range(1, target+1):
                ans = 0
                for face in range(1, k+1):
                    if (tar - face) >= 0:
                        ans += dp[i-1][tar-face]
                
                dp[i][tar] = (ans % MOD)
        
        return dp[n][target]
    
    
    ## space optimization
    def spaceOpt(n, k, target):
        ## let's create 2 arrays
        prev = [0]*(target+1)
        curr = [0]*(target+1)
        
        ## base case
        prev[0] = 1
        
        for i in range(1, n+1):
            for tar in range(1, target+1):
                ans = 0
                for face in range(1, k+1):
                    if (tar - face) >= 0:
                        ans += prev[tar-face]
                
                curr[tar] = (ans % MOD)
            
            prev = curr[:]
        
        return prev[target]
    
    ## initializing the memo array
    memo = [[None]*(target+1) for _ in range(n+1)]    
    
    return solveMem(memo, n, target), solveTab(n, k, target), spaceOpt(n, k, target)


# n = 30; k = 30; target = 500  
# ways = numRollsToTarget(n, k, target)
# print(ways)         
###################################################################################################################################
## **Distinct Ways Pattern Dynamic Programming**
## **416. Partition Equal Subset Sum**

def canPartition(nums: list[int]) -> bool:
    ## let's get the total sum of the nums
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    ## if any of the sum of the subset of nums is equal to the target 
    ## then we can say partition is possible. 
    target = total_sum // 2
    n = len(nums)
    
    def solveMem(memo, i, tar):
        ## base cases
        if tar < 0:
            return False
        
        if i >= n:
            return False
        
        if tar == 0:
            return True
        
        ## check if the state is already computed
        if memo[i][tar] != -1:
            return memo[i][tar]
        
        ## include
        incl = solveMem(memo, i+1, tar-nums[i])
        
        ## exclude
        excl = solveMem(memo, i+1, tar)
        
        ## store the computed state
        memo[i][tar] = incl or excl
        
        return memo[i][tar]
    
    
    def solveTab(n):
        ## initializing the dp array
        dp = [[False]*(target+1) for _ in range(n+1)]
        
        ## base case
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(n-1, -1, -1):
            for tar in range(1, target+1):
                incl, excl = False, False
                if (tar - nums[i]) >= 0:
                    ## include
                    incl = dp[i+1][tar-nums[i]]
                    
                ## exclude
                excl = dp[i+1][tar]
                    
                dp[i][tar] = incl or excl
                    
        return dp[0][target]
    
    
    def spaceOpt(n):
        ## let's create 2 arrays prev and curr
        prev = [False]*(target+1)
        curr = [False]*(target+1)
        
        ## base case
        prev[0] = True
        curr[0] = True
        
        for i in range(n-1, -1, -1):
            for tar in range(1, target+1):
                incl, excl = False, False
                if (tar - nums[i]) >= 0:
                    ## include
                    incl = prev[tar-nums[i]]
                
                ## exclude
                excl = prev[tar]
                
                curr[tar] = incl or excl
            
            prev = curr[:]
        
        return prev[target]
    
    ## initialize the memo array
    memo = [[-1]*(target+1) for _ in range(n)]
    
    return solveMem(memo, 0, target), solveTab(n), spaceOpt(n)

# nums = [1, 2, 5, 1, 3, 2, 4, 1, 6, 2, 1, 4, 2, 6, 8, 2, 4]
# print(canPartition(nums))
#########################################################################################################################################
## **Distinct Ways Pattern Dynamic Programming**
## **801. Minimum Swaps To Make Sequences Increasing**
## **Awesome Problem**

def minSwap(nums1: list[int], nums2: list[int]) -> int:
    ## insert -1 at begin of each of the array
    nums1.insert(0, -1)
    nums2.insert(0, -1)
    
    n = len(nums1)
    
    def solveMem(memo, i, swapped):
        ## base case
        if i == n:
            return 0
        
        ## check if the state is already computed
        if memo[i][swapped] is not None:
            return memo[i][swapped]
        
        ans = math.inf
        
        prev1 = nums1[i-1]
        prev2 = nums2[i-1]
        
        if swapped:
            ## swap the prev1 and prev2
            prev1, prev2 = prev2, prev1
        
        ## no swap
        if (nums1[i] > prev1) and (nums2[i] > prev2):
            ans = solveMem(memo, i+1, 0)
        
        ## swap
        if (nums1[i] > prev2) and (nums2[i] > prev1):
            ans = min(ans, 1+solveMem(memo, i+1, 1))
        
        ## store the computed state
        memo[i][swapped] = ans
        
        return memo[i][swapped]
    
    
    def solveTab(n):
        ## initialize a dp array
        dp = [[0]*2 for _ in range(n+1)]
        
        for i in range(n-1, 0, -1):
            for swapped in range(1, -1, -1):
                ans = math.inf
        
                prev1 = nums1[i-1]
                prev2 = nums2[i-1]
                
                if swapped:
                    ## swap the prev1 and prev2
                    prev1, prev2 = prev2, prev1
                
                ## no swap
                if (nums1[i] > prev1) and (nums2[i] > prev2):
                    ans = dp[i+1][0]
                
                ## swap
                if (nums1[i] > prev2) and (nums2[i] > prev1):
                    ans = min(ans, 1+dp[i+1][1])
                
                dp[i][swapped] = ans
                
        return dp[1][0]
    
    
    ## space optimized bottom-up soln
    def spaceOpt(n):
        ## let's initialize the prev and curr
        prev = [0]*2
        curr = [0]*2
        
        for i in range(n-1, 0, -1):
            for swapped in range(1, -1, -1):
                ans = math.inf
        
                prev1 = nums1[i-1]
                prev2 = nums2[i-1]
                
                if swapped:
                    ## swap the prev1 and prev2
                    prev1, prev2 = prev2, prev1
                
                ## no swap
                if (nums1[i] > prev1) and (nums2[i] > prev2):
                    ans = prev[0]
                
                ## swap
                if (nums1[i] > prev2) and (nums2[i] > prev1):
                    ans = min(ans, 1+prev[1])
                
                curr[swapped] = ans
            
            prev = curr[:]
        
        return prev[0]
    
    ## initialize a memo array
    memo = [[None]*2 for _ in range(n)]
    
    return solveMem(memo, 1, 0), solveTab(n), spaceOpt(n)


# nums1 = [1,3,5,4]; nums2 = [1,2,3,7]
# res = minSwap(nums1, nums2)
# print(res)
##################################################################################################################################
## **1027. Longest Arithmetic Subsequence**
## Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
## **DP with Hashing**
## **Awesome Question**
## Please note, Bottom-up Dp is important here as Top-Down DP didn't pass all the test cases
def longestArithSeqLength(nums: list[int]) -> int:
    
    def solveMem(memo, index, diff):
        ## base case
        if index < 0:
            return 0
        
        ## check if the state is already computed
        if diff in memo[index]:
            return memo[index][diff]
        
        ans = 0
        for k in range(index):
            if (nums[index] - nums[k]) == diff:
                ans = max(ans, 1+solveMem(memo, k, diff))
        
        ## store the computed state
        memo[index][diff] = ans
        
        return memo[index][diff]
    
    
    def solveMemDriver(n):
        ## let's initializing memo [{}, {}, {}...]
        memo = [{} for _ in range(n)]
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, 2 + solveMem(memo, i, nums[j]-nums[i]))
        
        return ans
    
    
    ## **Bottom-up soln with hashing**
    def solveTab(nums, n):
        ans = 0
        
        ## let's initializing dp [{}, {}, {}...]
        dp = [{} for _ in range(n)]
        
        for i in range(1, n):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                
                ## initializing the cnt with 1, since j is included in AP
                cnt = 1
                
                ## check if the state (for j) is computed then update the cnt
                if diff in dp[j]:
                    cnt = dp[j][diff]
                
                ## now, including i to the AP. So, adding 1 to the cnt
                dp[i][diff] = 1 + cnt
                ans = max(ans, dp[i][diff])
        
        return ans
        
    n = len(nums)
    
    if n <= 2:
        return n

    return solveMemDriver(n), solveTab(nums, n)

# nums = [1, 7, 10, 13, 14, 19]
# l = longestArithSeqLength(nums)
# print(l)
#######################################################################################################################################
## 1218. Longest Arithmetic Subsequence of Given Difference
def longestSubsequence(nums: list[int], difference: int) -> int:
    n = len(nums)
    
    ans = 0
    
    ## initializing dp
    dp = {}
    
    for i in range(n):
        temp = nums[i] - difference
        cnt = 0
        
        if temp in dp:
            cnt = dp[temp]
        
        dp[nums[i]] = 1 + cnt
        
        ans = max(ans, dp[nums[i]])
    
    return ans

arr = [1,5,7,8,5,3,4,2,1]; difference = -2
l = longestSubsequence(arr, difference)
print(l)














