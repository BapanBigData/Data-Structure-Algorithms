import math

## Knapsack problem:
def knapsackProblem(W: int, weights: list[int], values: list[int]) -> int:
    
    def solveMem(memo, i, w):
        ## base case
        if i == len(weights):
            return 0
        
        ## ckeck if the state is alredy computed
        if memo[i][w] is not None:
            return memo[i][w]
        
        incl = 0
        excl = 0
        
        if (w - weights[i]) >= 0:
            incl = values[i] + solveMem(memo, i+1, w-weights[i])
        
        excl = 0 + solveMem(memo, i+1, w)
        
        ## store computed state
        memo[i][w] = max(incl, excl)
        
        return memo[i][w]
    
    
    def solveTab(n, W):
        ## initializing the 2-D dp array of size (n X W)
        dp = [[None]*(W+1) for _ in range(n+1)]
        
        ## filling the base cases
        for j in range(W+1):
            dp[n][j] = 0
        
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(n-1, -1, -1):
            incl, excl = 0, 0
            for w in range(1, W+1):
                if (w - weights[i]) >= 0:
                    incl = values[i] + dp[i+1][w-weights[i]]
                
                excl = 0 + dp[i+1][w]
                
                dp[i][w] = max(incl, excl)
        
        return dp[0][W]
    
    
    def spaceOpt(n, W):
        ## initializing two arrays
        curr = [0] * (W+1)
        prev = [0] * (W+1)
        
        for i in range(n-1, -1, -1):
            incl, excl = 0, 0
            for w in range(1, W+1):
                if (w - weights[i]) >= 0:
                    incl = values[i] + prev[w-weights[i]]
                
                excl = 0 + prev[w]
                
                curr[w] = max(incl, excl)
                
            prev = curr[:]
        
        return prev[W]

    
    n = len(weights)
    
    ## initializing the memo matrix (n X W) to store the computation
    memo = [[None] * (W+1) for _ in range(n)]
    
    return solveMem(memo, 0, W), solveTab(n, W), spaceOpt(n, W)


# W = 17; weights = [1, 2, 4, 5, 8, 3, 6, 12, 9]; values = [5, 4, 8, 6, 32, 23, 10, 1, 12]
# res = knapsackProblem(W, weights, values)
# print(res)
# # print(knapsackProblem(W, weights, values))
##########################################################################################################################################
## **221. Maximal Square**
## Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
def maximalSquare(matrix: list[list[str]]) -> int:
    
    n, m = len(matrix), len(matrix[0])
    
    mx = [0]
    
    def solveMem(memo, i, j):
        ## base case
        if (i >= n) or (j >= m):
            return 0
        
        ## check if the state is already computed
        if memo[i][j] is not None:
            return memo[i][j]
        
        ## for an (i,j) there are 3 function call 
        ## right call (i, j+1), diagonal call (i+1, j+1) and down call (i+1, j)
        right = solveMem(memo, i, j+1)
        diagonal = solveMem(memo, i+1, j+1)
        down = solveMem(memo, i+1, j)
        
        
        if matrix[i][j] == '1':
            
            ans = 1 + min(right, diagonal, down)
            mx[0] = max(mx[0], ans)
            
            ## store the computed state
            memo[i][j] = ans
            return memo[i][j]
        else:
            memo[i][j] = 0
            return memo[i][j]
    
    
    def solveTab(n, m):
        mx = 0
        
        ## initialize the dp matrix
        dp = [[None]*(m+1) for _ in range(n+1)]
        
        ## fill the base case
        for j in range(m+1):
            dp[n][j] = 0
        
        for i in range(n+1):
            dp[i][m] = 0
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                ## now for a (i, j) we have right, diagonal and down
                right = dp[i][j+1]
                diagonal = dp[i+1][j+1]
                down = dp[i+1][j]
                
                if matrix[i][j] == '1':
                    ans = 1 + min(right, diagonal, down)
                    mx = max(mx, ans)
                    dp[i][j] = ans
                else:
                    dp[i][j] = 0
        
        return mx * mx
    
    
    def spaceOpt(n, m):
        mx = 0
        
        ## initialize two arrays prev and curr of size m
        prev = [0] * (m+1)
        curr = [None] * (m+1)
        
        curr[m] = 0
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                right = curr[j+1]
                diagonal = prev[j+1]
                down = prev[j]
                
                if matrix[i][j] == '1':
                    ans = 1 + min(right, diagonal, down)
                    mx = max(mx, ans)
                    curr[j] = ans
                else:
                    curr[j] = 0
            
            prev = curr[:]
        
        return mx * mx
    
    # ## initializing the memo matrix
    # memo = [[None]*m for _ in range(n)]
        
    # solveMem(memo, 0, 0)
    
    return solveTab(n, m), spaceOpt(n, m)

# mat = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]
# area = maximalSquare(mat)
# print(area)
##################################################################################################################################
## 85. Maximal Rectangle
## Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
## Note: Little tricky to solve using DP (Will look into this problem later)
# def maximalRectangle(matrix: list[list[str]]) -> int:
#     ## initializing the n, m
#     n, m = len(matrix), len(matrix[0])
    
#     area = [0]
    
#     def solveMem(i, j):
#         ## base case
#         if (i >= n) or (j >= m):
#             return 0
        
#         ## now, for an (i,j) we have two ways to go: right -> (i, j+1), down -> (i+1, j)
#         right = solveMem(i, j+1)
#         down = solveMem(i+1, j)
        
#         if matrix[i][j] == '1':
#             base = 1 + right
#             height = 1 + down
#             a = (base * height)
#             area[0] = max(area[0], a)
            
#             return a
#         else:
#             return 0
    
#     solveMem(0, 0)
    
#     return area[0]

# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# rect_area = maximalRectangle(matrix=matrix)
# print(rect_area)
#########################################################################################################################
## **1039. Minimum Score Triangulation of Polygon**

def minScoreTriangulation(values: list[int]) -> int:
    
    n = len(values)
    
    def solveMem(memo, i, j):
        ## base case
        ## only 2 vertices (can't form triangle)
        if (i+1) == j:
            return 0
        
        ## check if the state is already computed
        if memo[i][j] is not None:
            return memo[i][j]
        
        mn = math.inf
        
        for k in range(i+1, j):
            ans = (values[i]*values[j]*values[k]) + solveMem(memo, i, k) + solveMem(memo, k, j)
            mn = min(mn, ans)
        
        ## store the computed state
        memo[i][j] = mn
            
        return memo[i][j]
    
    ## let's try to solve it using bottpm-up approach
    def solveTab(n):
        ## let's initializing the 2-D dp array will all 0's 
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i+2, n):
                
                mn = math.inf
                for k in range(i+1, j):
                    ans = (values[i]*values[j]*values[k]) + dp[i][k] + dp[k][j]
                    mn = min(mn, ans)
                
                dp[i][j] = mn
        
        return dp[0][n-1]
    
    ## intitialize a 2-D memo matrix
    memo = [[None]*n for _ in range(n)]
    
    return solveMem(memo, 0, n-1), solveTab(n)

# values = [1,3,1,4,1,5,2]
# print(minScoreTriangulation(values))
############################################################################################################################
## **1824. Minimum Sideway Jumps**
def minSideJumps(obstacles: list[int]) -> int:
    
    n = len(obstacles)
    
    def solveMem(memo, pos, currlane):
        ## base case
        if pos == n-1:
            return 0
        
        ## check if the state is already computed
        if memo[pos][currlane] is not None:
            return memo[pos][currlane]
        
        if obstacles[pos+1] != currlane:
            memo[pos][currlane] = 0 + solveMem(memo, pos+1, currlane)
            return memo[pos][currlane]
        else:
            ans = math.inf
            ## sideway jump, there are 3 options 
            for lane in range(1, 4):
                if (lane != currlane) and (obstacles[pos] != lane):
                    ans = min(ans, 1 + solveMem(memo, pos, lane))
            
            ## store the computed state
            memo[pos][currlane] = ans
            
            return memo[pos][currlane]
        
        
    def solveTab(n):
        ## initializing the dp array
        dp = [[math.inf]*4 for _ in range(n)]
        
        ## base case filling
        for lane in range(4):
            dp[n-1][lane] = 0
        
        for pos in range(n-2, -1, -1):
            for currlane in range(1, 4):
                if obstacles[pos+1] != currlane:
                    ## going straight
                    dp[pos][currlane] = 0 + dp[pos+1][currlane]
                else:
                    ## side ways jump
                    ans = math.inf
                    for lane in range(1, 4):
                        if (lane != currlane) and (obstacles[pos] != lane):
                            ans = min(ans, 1+dp[pos+1][lane]) 
                            
                    dp[pos][currlane] = ans
        
        return min(dp[0][2], 1+dp[0][1], 1+dp[0][3])
    
    ## initializing a 2-D memo array
    memo = [[None]*4 for _ in range(n)]
    
    return solveMem(memo, 0, 2), solveTab(n)

# obstacles = [0,1,1,3,3,0]
# print(minSideJumps(obstacles))
#####################################################################################################################################
## 1402. Reducing Dishes
## Variation of knapsack
def maxSatisfaction(satisfaction: list[int]) -> int:
    ## sort the satisfaction array
    satisfaction.sort()
    
    n = len(satisfaction)
    
    def solveMem(memo, i, t):
        ## base case
        if i == n:
            return 0
        
        ## check if the state is already computed
        if memo[i][t] is not None:
            return memo[i][t]
        
        ## for each i, we have 2 options either include it or exclude it
        incl = (satisfaction[i]*t) + solveMem(memo, i+1, t+1)
        excl = 0 + solveMem(memo, i+1, t)
        
        ## store the computed state
        memo[i][t] = max(incl, excl)
        
        return memo[i][t]
    
    
    def solveTab(n):
        ## initializing the a 2-D dp array
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for t in range(i, -1, -1):
                ## for each i, we have 2 options either include it or exclude it
                incl = (satisfaction[i]*(t+1)) + dp[i+1][t+1]
                excl = 0 + dp[i+1][t]
            
                dp[i][t] = max(incl, excl)
        
        return dp[0][0]
    
    
    def spaceOpt(n):
        ## initializing 2 arrays prev and curr
        prev = [0]*(n+1)
        curr = [0]*(n+1)
        
        for i in range(n-1, -1, -1):
            for t in range(i, -1, -1):
                incl = (satisfaction[i]*(t+1)) + prev[t+1]
                excl = 0 + prev[t]
                
                curr[t] = max(incl, excl)
            
            prev = curr[:]
        
        return prev[0]
    
    ## initializing the a 2-D memo array
    memo = [[None]*(n+1) for _ in range(n)]
    
    return solveMem(memo, 0, 1), solveTab(n), spaceOpt(n)

# satisfaction = [4,3,2]
# res = maxSatisfaction(satisfaction)
# print(res)
##########################################################################################################################################
## **Longest Increasing Subsequence:**

def longestIncreasingSubsequence(nums: list[int]) -> int:
    
    n = len(nums)
    
    ## brute force soln
    def solver(i, seq, l):
        ## base case
        if i == n:
            l[0] = max(l[0], len(seq))
            return l[0]
        
        ## include
        if (len(seq) == 0) or (nums[i] > seq[-1]):
            solver(i+1, seq+[nums[i]], l)
        
        ## exclude
        solver(i+1, seq, l)
        
        return l[0]
    
    
    def solveMem(memo, curr, prev):
        ## base case
        if curr == n:
            return 0
        
        ## check if the state is already computed
        if memo[curr][prev] is not None:
            return memo[curr][prev]
        
        ## include
        incl = 0
        if (prev == -1) or (nums[curr] > nums[prev]):
            incl = 1 + solveMem(memo, curr+1, curr)
        
        ## exclude
        excl = 0 + solveMem(memo, curr+1, prev)
        
        ## store the computed state
        memo[curr][prev] = max(incl, excl)
        
        return memo[curr][prev]
    
    
    def solveTab(n):
        ## initializing the 2-D dp array
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for curr in range(n-1, -1, -1):
            for prev in range(curr-1, -2, -1):
                ##include
                incl = 0
                if (prev == -1) or (nums[curr] > nums[prev]):
                    incl = 1 + dp[curr+1][curr]
                
                excl = 0 + dp[curr+1][prev]
                
                dp[curr][prev] = max(incl, excl)
        
        return dp[0][-1]
    
    
    def spaceOpt(n):
        ## take 2 array
        row0 = [0]*(n+1)
        row1 = [0]*(n+1)
        
        for curr in range(n-1, -1, -1):
            for prev in range(curr-1, -2, -1):
                incl = 0
                if (prev == -1) or (nums[curr] > nums[prev]):
                    incl = 1 + row0[curr]
                
                excl = 0 + row0[prev]
                
                row1[prev] = max(incl, excl)
            
            row0 = row1[:]
        
        return row0[-1]
    
    
    ## DP with Binary Search
    ## T.C: O(n.log(n))
    ## Space: O(n)
    def getJustGreater(lst, x):
        s = 0
        e = len(lst)-1
        indx = -1
        
        while e >= s:
            mid = (s + e) // 2
            
            if lst[mid] >= x:
                indx = mid
                e = mid - 1
            else:
                s = mid + 1
        
        return indx
    
    
    def optimalSoln(n):
        if n == 0:
            return 0
        
        ans = []
        ans.append(nums[0])
        
        for i in range(1, n):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                indx = getJustGreater(ans, nums[i])
                ans[indx] = nums[i]
        
        return len(ans)
    
    ## initializing the memo array
    memo = [[None]*(n) for _ in range(n)]
    
    return solveMem(memo, 0, -1), solveTab(n), spaceOpt(n), optimalSoln(n)

# nums = [5, 8, 3, 7, 9, 1]
# lis = longestIncreasingSubsequence(nums)
# print(lis)
####################################################################################################################################
## **354. Russian Doll Envelopes: Variation of Longest Increasing Subsequence**

def maxEnvelopes(envelopes: list[list[int]]) -> int:
    n = len(envelopes)
    
    ## let's sort the given envelopes array with ascending order of width and decending order of height
    envelopes.sort(key = lambda x: (x[0], -x[-1]))
    
    def solveMem(memo, curr, prev):
        ## base case
        if curr == n:
            return 0
        
        ## check if the state is already computed
        if memo[curr][prev] is not None:
            return memo[curr][prev]
        
        ## include
        incl = 0
        if (prev == -1) or (envelopes[curr][-1] > envelopes[prev][-1]):
            incl = 1 + solveMem(memo, curr+1, curr)
        
        ## exclude
        excl = 0 + solveMem(memo, curr+1, prev)
        
        ## store the computed state
        memo[curr][prev] = max(incl, excl)
        
        return memo[curr][prev]
    
    
    ## DP with Binary Search
    ## T.C: O(n.log(n))
    ## Space: O(n)
    def getJustGreater(lst, x):
        s = 0
        e = len(lst)-1
        indx = -1
        
        while e >= s:
            mid = (s + e) // 2
            
            if lst[mid] >= x:
                indx = mid
                e = mid - 1
            else:
                s = mid + 1
        
        return indx
    
    
    def optimalSoln(n):
        if n == 0:
            return 0
        
        ans = []
        ans.append(envelopes[0][-1])
        
        for i in range(1, n):
            if envelopes[i][-1] > ans[-1]:
                ans.append(envelopes[i][-1])
            else:
                indx = getJustGreater(ans, envelopes[i][-1])
                ans[indx] = envelopes[i][-1]
        
        return len(ans)
    
    return optimalSoln(n)

# envelopes = [[5,4],[6,4],[6,7],[2,3]]
# dolls = maxEnvelopes(envelopes)
# print(dolls)
#########################################################################################################################################
## **1691. Maximum Height by Stacking Cuboids (Variation of LIS)**

def maxHeight(cuboids: list[list[int]]) -> int:
    ## sort all dimensions for each cuboids
    for cuboid in cuboids:
        cuboid.sort()
    
    ## sort all cuboids basis on w or l
    cuboids.sort(key=lambda x: (x[0], x[1], x[2]))
    
    n = len(cuboids)
    
    def solveMem(memo, curr, prev):
        if curr < 0:
            return 0
        
        ## check if the state is already computed
        if memo[curr][prev] is not None:
            return memo[curr][prev]
        
        ## include
        incl = 0
        if (prev == n) or (
            
            (cuboids[curr][0] <= cuboids[prev][0]) and 
            (cuboids[curr][1] <= cuboids[prev][1]) and 
            (cuboids[curr][2] <= cuboids[prev][2])
            
            ):
            
            incl = cuboids[curr][-1] + solveMem(memo, curr-1, curr)
        
        excl = 0 + solveMem(memo, curr-1, prev)
        
        ## store the computed state
        memo[curr][prev] = max(incl, excl)
        
        return memo[curr][prev]
    
    
    def spaceOpt(n):
        ## take 2 array
        row0 = [0]*(n+1)
        row1 = [0]*(n+1)
        
        for curr in range(n-1, -1, -1):
            for prev in range(curr-1, -2, -1):
                incl = 0
                if (prev == -1) or (
                    
                    (cuboids[prev][0] <= cuboids[curr][0]) and 
                    (cuboids[prev][1] <= cuboids[curr][1]) and 
                    (cuboids[prev][2] <= cuboids[curr][2])
                    
                    ):
                    
                    incl = cuboids[curr][-1] + row0[curr]
                
                excl = 0 + row0[prev]
                
                row1[prev] = max(incl, excl)
            
            row0 = row1[:]
        
        return row0[-1]
    
    
    ## initializing the memo 2-D memo array
    memo = [[None]*(n+1) for _ in range(n)]
    
    return solveMem(memo, n-1, n), spaceOpt(n)


cuboids = [[92,47,83],[75,20,87],[68,12,83],[12,85,15],[16,24,47],[69,65,35],[96,56,93],[89,93,11],[86,20,41],[69,77,12],[83,80,97],[90,22,36]]
h = maxHeight(cuboids)
print(h)























