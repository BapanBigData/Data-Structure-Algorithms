import math

## LIS (Longest Increasing Subsequence)

def lengthOfLIS(nums: list[int]) -> int:
    n = len(nums)
    
    def solveMem(memo, curr, prev):
        ## base cases
        if curr == n:
            return 0
        
        ## check if the state is already computed
        if memo[curr][prev] is not None:
            return memo[curr][prev]
        
        incl, excl = 0, 0
        
        if (prev == -1) or (nums[curr] > nums[prev]):
            incl = 1 + solveMem(memo, curr+1, curr)
        
        excl = 0 + solveMem(memo, curr+1, prev)
        
        ## store the computed state
        memo[curr][prev] = max(incl, excl)
        
        return memo[curr][prev] 
    
    ## initializing the memo array
    memo = [[None]*n for _ in range(n)]
    
    return solveMem(memo, 0, -1)


# nums = [10,9,2,5,3,7,101,18]
# lis = lengthOfLIS(nums)
# print(lis)

#############################################################################################################################
## ** 673. Number of Longest Increasing Subsequence **

def findNumberOfLIS(nums: list[int]) -> int:
    n = len(nums)
    
    def solveMem(memo, curr, prev):
        # Base cases: If curr is out of bounds, return length 0 and count 1
        if curr == n:
            return (0, 1)
        
        # Check if the state is already computed
        if memo[curr][prev] is not None:
            return memo[curr][prev]
        
        incl, incl_cnt = 0, 0
        
        # Include the current element if it's valid
        if prev == -1 or nums[curr] > nums[prev]:
            incl, incl_cnt = solveMem(memo, curr + 1, curr)
            incl += 1
        
        # Exclude the current element
        excl, excl_cnt = solveMem(memo, curr + 1, prev)
        
        # Determine the result for the current state
        if (incl > excl):
            result = (incl, incl_cnt)
        elif (incl < excl):
            result = (excl, excl_cnt)
        else:  # incl == excl
            result = (incl, incl_cnt + excl_cnt)
        
        # Store the computed state
        memo[curr][prev] = result
        
        return memo[curr][prev]
    
    
    def solveTab(n):
        ## let's initializing the dp array
        dp = [[None]*(n) for _ in range(n+1)]
        
        ## base case
        for j in range(n):
            dp[n][j] = (0, 1)
        
        for curr in range(n-1, -1, -1):
            for prev in range(curr-1, -2, -1):
                
                incl, incl_cnt = 0, 0
        
                # Include the current element if it's valid
                if prev == -1 or nums[curr] > nums[prev]:
                    incl, incl_cnt = dp[curr+1][curr]
                    incl += 1
                
                # Exclude the current element
                excl, excl_cnt = dp[curr+1][prev]
                
                # Determine the result for the current state
                if (incl > excl):
                    result = (incl, incl_cnt)
                elif (incl < excl):
                    result = (excl, excl_cnt)
                else:  # incl == excl
                    result = (incl, incl_cnt + excl_cnt)
                
                dp[curr][prev] = result
                
        return dp[0][-1][-1]
    
    
    def spaceOpt(n):
        ## let's initialize two rows row0 and row1
        row0 = [(0, 1)]*n
        row1 = [None]*n
        
        for curr in range(n-1, -1, -1):
            for prev in range(curr-1, -2, -1):
                
                incl, incl_cnt = 0, 0
        
                # Include the current element if it's valid
                if prev == -1 or nums[curr] > nums[prev]:
                    incl, incl_cnt = row0[curr]
                    incl += 1
                
                # Exclude the current element
                excl, excl_cnt = row0[prev]
                
                # Determine the result for the current state
                if (incl > excl):
                    result = (incl, incl_cnt)
                elif (incl < excl):
                    result = (excl, excl_cnt)
                else:  # incl == excl
                    result = (incl, incl_cnt + excl_cnt)
                
                row1[prev] = result
            
            row0 = row1[:]
                
        return row0[-1][-1]
    
    
    # Initializing the memo array
    memo = [[None]*n for _ in range(n)]
    
    return solveMem(memo, 0, -1)[-1], solveTab(n), spaceOpt(n)


# nums = [1, 3, 5, 4, 7]
# print(findNumberOfLIS(nums))

###########################################################################################################################
## ** 646. Maximum Length of Pair Chain **
def findLongestChain(pairs: list[list[int]]) -> int:
    ## Sort the pairs by their first element
    pairs.sort(key=lambda x: x[0])
    n = len(pairs)
    
    def solveMem(memo, curr, prev):
        ## base case
        if curr == n:
            return 0
        
        ## check if the state is already computed
        if memo[curr][prev] is not None:
            return memo[curr][prev]
        
        incl, excl = 0, 0
        
        if (prev == -1) or (pairs[curr][0] > pairs[prev][1]):
            incl = 1 + solveMem(memo, curr+1, curr)
        
        excl = 0 + solveMem(memo, curr+1, prev)
        
        ## store the computed state
        memo[curr][prev] = max(incl, excl)
        
        return memo[curr][prev]
    
    ## let's initializing the memo array
    memo = [[None]*n for _ in range(n)]
    
    return solveMem(memo, 0, -1)


def findLongestChainDpWithBS(pairs: list[list[int]]) -> int:
    ## Sort the pairs by their first element
    pairs.sort(key=lambda x: x[0])
    n = len(pairs)
    
    def justGreater(arr, x):
        si, ei = 0, len(arr)-1
        indx = -1
        while (ei >= si):
            mid = (si + ei) // 2
            
            if arr[mid] == x:
                return mid
            
            if arr[mid] >= x:
                indx = mid
                ei = mid-1
            else:
                si = mid+1
        return indx
    
    ## Dp with Binary Search
    def solver(n):
        res = [pairs[0][1]]
        
        for i in range(1, n):
            if (pairs[i][0] > res[-1]):
                res.append(pairs[i][1])
            else:
                ## get the just greater element
                indx = justGreater(res, pairs[i][1])
                
                if indx != -1:
                    res[indx] = pairs[i][1]
        
        return len(res)
    
    return solver(n)


pairs = [[5,24],[15,25],[27,40],[50,60],[5,6],[1,2],[6,7],[2,3],[3,4]]
chainLen = findLongestChainDpWithBS(pairs)
print(chainLen)