import math

## Longest Increasing Subsequence (LIS)
def lis(arr: list):
    
    def solve_memo(memo, curr, prev, n):
        ## base case
        if curr == n:
            memo[curr][prev] = 0
            return memo[curr][prev]
        
        ## check if the state is already computed
        if memo[curr][prev] is not None:
            return memo[curr][prev]
        
        ## curr -> include or exclude
        incl = 0
        if prev == -1 or arr[curr] > arr[prev]:
            incl = 1 + solve_memo(memo, curr+1, curr, n)
        
        excl = 0 + solve_memo(memo, curr+1, prev, n)
        
        memo[curr][prev] = max(incl, excl)
        
        return memo[curr][prev]
    
    def solve_tabulation(n):
        ## initializing the dp array
        dp = [[None]*(n) for _ in range(n+1)]
        
        ## base case
        for j in range(n):
            dp[n][j] = 0
        
        for curr in range(n-1, -1, -1):
            prev = curr - 1
            while prev >= -1:
                incl = 0
                if prev == -1 or arr[curr] > arr[prev]:
                    incl = 1 + dp[curr+1][curr]
                
                excl = 0 + dp[curr+1][prev]
                
                dp[curr][prev] = max(incl, excl)
                
                prev -= 1
                
        return dp[0][-1]
    
    def solve_space_optimal(n):
        ## initializing the arrays
        up = [None]*n
        bottom = [0]*n
        
        for curr in range(n-1, -1, -1):
            prev = curr - 1
            while prev >= -1:
                incl = 0
                if prev == -1 or arr[curr] > arr[prev]:
                    incl = 1 + bottom[curr]
                
                excl = 0 + bottom[prev]
                
                up[prev] = max(incl, excl)
                
                prev -= 1
            
            bottom = up[:]
        
        return bottom[-1]
    
    n = len(arr)
    
    # ## initializing the memo array
    # memo = [[None]*n for _ in range(n+1)]
    # return solve_memo(memo, 0, -1, n)
    
    # tab = solve_tabulation(n)
    opt = solve_space_optimal(n)
    
    return opt
        
# arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# nums = [5, 8, 3, 7, 9, 1]
# res = lis(arr)
# print(res)        
# for e in res:
#     print(e)
##---------------------------------------------------------------------------------------------------
## DP With Binary Search: Longest Increasing Subsequence (LIS)
def lis_bs(nums: list):
    
    def get_lower_bound(ans, x):
        s = 0
        e = len(ans)
        indx = -1
        while s <= e:
            mid = (s + e) // 2
            
            if ans[mid] == x:
                return mid
            
            if ans[mid] > x:
                indx = mid
                e = mid - 1
            else:
                s = mid + 1
                
        return indx     
    
    def solveOptimal(nums, n):
        if n == 0:
            return 0
        
        ans = []
        ans.append(nums[0])
        
        for i in range(1, n):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                ## get the index of the lower bound
                indx = get_lower_bound(ans, nums[i])
                ans[indx] = nums[i]
        
        return len(ans)
    
    n = len(nums)
    return solveOptimal(nums, n)
    
# arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# nums = [5, 8, 3, 7, 9, 1]
# res = lis_bs(nums)
# print(res)
##-----------------------------------------------------------------------------------------------------
## Russian Doll Envelopes: Variate of LIS
def maxEnvelopes(envelopes: list[list[int]]):
    n = len(envelopes)
    
    ## sort the envelops based on width in ascending order, if widths are equal
    ## then sort based on height in decending order.
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    def getLowerBound(ans, x):
        s = 0
        e = len(ans)
        indx = -1
        while s <= e:
            mid = (s+e) // 2
            
            if ans[mid] == x:
                return mid
            
            if ans[mid] > x:
                indx = mid
                e = mid - 1
            else:
                s = mid + 1
        
        return indx
    
    def solveOptimal(envelopes, n):
        ans = []
        ans.append(envelopes[0][-1])
        
        for i in range(1, n):
            if envelopes[i][-1] > ans[-1]:
                ans.append(envelopes[i][-1])
            else:
                ## get the lower bound of envelopes[i][-1]
                indx = getLowerBound(ans, envelopes[i][-1])
                ans[indx] = envelopes[i][-1]
                
        return len(ans)
    
    return solveOptimal(envelopes, n)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
ans = maxEnvelopes(envelopes)
print(ans)
##-----------------------------------------------------------------------------------------------------
## Maximum Height by Stacking Cuboids: Variate of LIS
def maxHeight(cuboids: list[list[int]]):
    
    n = len(cuboids)
    
    ## sort all dimension of all cuboids
    for cuboid in cuboids:
        cuboid.sort()
    
    ## sort all cuboids based on base (width*length)
    cuboids.sort(key=lambda x: x[0]*x[1])
    
    def canPlaced(cuboid_i, cuboid_j):
        return (cuboid_i[0] >= cuboid_j[0] and cuboid_i[1] >= cuboid_j[1] and cuboid_i[2] >= cuboid_j[2])
        # return all(dim_i >= dim_j for dim_i, dim_j in zip(cuboid_i, cuboid_j))
    
    def solveOptimal(cuboids, n):
        ## initializing up and bottom arrays
        up = [None]*n
        bottom = [0]*n
        
        for curr in range(n-1, -1, -1):
            prev = curr - 1
            while prev >= -1:
                incl = 0
                if prev == -1 or canPlaced(cuboids[curr], cuboids[prev]):
                    incl = cuboids[curr][-1] + bottom[curr]
                excl = 0 + bottom[prev]
                
                up[prev] = max(incl, excl)
                
                prev -= 1
            
            bottom = up[:]
        
        return bottom[-1]
    
    return solveOptimal(cuboids, n)

cuboids = [[92,47,83],[75,20,87],[68,12,83],[12,85,15],[16,24,47],[69,65,35],
        [96,56,93],[89,93,11],[86,20,41],[69,77,12],[83,80,97],[90,22,36]]

cuboids = [[34,29,33],[7,25,75],[31,15,68],[80,80,38],[72,21,30],[2,66,25],[59,36,6],[39,48,95],[35,85,71],[17,14,78]]

cuboids = [[57,59,81],[30,52,47],[21,44,55],[39,78,75],[26,70,100],[99,70,60],[79,72,82],[12,54,50],[34,20,22],[64,26,25],
        [5,12,50],[82,13,37],[64,44,43],[30,50,68],[98,69,84],[40,67,79],[79,83,53],[28,12,92],[99,100,16],[60,17,55],
        [75,86,17],[71,98,7],[61,48,94],[70,3,76],[62,22,30],[24,98,74],[12,5,73],[62,47,85],[95,29,93],[47,59,83],[74,98,13],
        [82,53,69],[85,93,51],[100,80,17],[8,8,3],[52,11,39],[83,89,46],[83,59,47],[66,82,42],[88,64,33],[71,68,87],[77,84,28],
        [75,71,80],[38,22,42],[67,44,31],[12,57,39],[24,5,88],[20,49,25],[45,60,37],[35,19,28],[75,93,57],[82,14,77],
        [78,87,17],[50,22,30],[91,78,71],[30,87,21],[89,66,17],[63,23,75],[12,20,2],[39,93,56],[90,78,24],[61,88,85],
        [65,66,59],[31,21,4],[81,88,14],[15,32,97],[15,44,64],[69,18,92],[8,52,56],[61,45,19],[83,93,24],[45,9,47],[8,20,9],
        [18,71,77],[21,88,19],[38,40,64],[79,67,71],[36,24,60],[11,49,58],[89,49,70],[73,38,67],[40,75,88],[72,92,55],
        [90,2,96],[40,62,33],[47,4,87],[99,8,59],[75,11,15],[50,28,87]]

# res = maxHeight(cuboids)
# print(res)
##--------------------------------------------------------------------------------------------------------------