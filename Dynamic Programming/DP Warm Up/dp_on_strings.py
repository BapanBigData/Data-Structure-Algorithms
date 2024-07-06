import math

## **1143. Longest Common Subsequence**
## Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
## Note: A subsequence of a string is a new string generated from the original string with some characters (can be none) 
##      deleted without changing the relative order of the remaining characters.

def longestCommonSubsequence(text1: str, text2: str) -> int:
    n1, n2 = len(text1), len(text2)
    
    def solveMem(memo, i, j):
        ## base case
        if (i == n1) or (j == n2):
            return 0
        
        ## check if the state is already computed
        if memo[i][j] is not None:
            return memo[i][j]
        
        if text1[i] == text2[j]:
            memo[i][j] = 1 + solveMem(memo, i+1, j+1)
            return memo[i][j]
        
        memo[i][j] = 0 + max(solveMem(memo, i, j+1), solveMem(memo, i+1, j))
        
        return memo[i][j]
    
    
    def solveTab(n1, n2):
        ## initializing the dp array
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        
        # ## base case filling
        # for i in range(n1+1):
        #     dp[i][n2] = 0
            
        # for j in range(n2+1):
        #     dp[n1][j] = 0
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = 0 + max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]
    
    
    def spaceOpt(n1, n2):
        ## initializing the prev and curr row
        prev = [0]*(n2+1)
        curr = [0]*(n2+1)
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = 0 + max(curr[j+1], prev[j])
            
            prev = curr[:]
        
        return prev[0]
    
    ## initializing the memo array
    memo = [[None]*n2 for _ in range(n1)]
    
    return solveMem(memo, 0, 0), solveTab(n1, n2), spaceOpt(n1, n2)


# text1 = 'indiaaaa indiaaaa'; text2 = 'india india india'
# lcs = longestCommonSubsequence(text1, text2)
# print(lcs)
#########################################################################################################################
## **516. Longest Palindromic Subsequence**
## Given a string s, find the longest palindromic subsequence's length in s.
def longestPalindromeSubseq(s: str) -> int:
    rev = s[::-1]
    n1, n2 = len(s), len(rev)
    
    def solveMem(memo, i, j):
        ## base case
        if (i == n1) or (j == n2):
            return 0
        
        ## check if the state is already computed
        if memo[i][j] is not None:
            return memo[i][j]
        
        if s[i] == rev[j]:
            memo[i][j] = 1 + solveMem(memo, i+1, j+1)
            return memo[i][j]
        
        memo[i][j] = 0 + max(solveMem(memo, i, j+1), solveMem(memo, i+1, j))
        
        return memo[i][j]
    
    def spaceOpt(n1, n2):
        ## initializing the prev and curr row
        prev = [0]*(n2+1)
        curr = [0]*(n2+1)
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                
                if s[i] == rev[j]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = 0 + max(curr[j+1], prev[j])
            
            prev = curr[:]
        
        return prev[0]
    
    ## initializing the memo array
    memo = [[None]*n2 for _ in range(n1)]    
    
    return solveMem(memo, 0, 0), spaceOpt(n1, n2)

# text = 'bbbaba'
# res = longestPalindromeSubseq(text)
# print(res)
############################################################################################################################
## **72. Edit Distance**
## Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

def minDistance(word1: str, word2: str) -> int:
    n1, n2 = len(word1), len(word2)
    
    def solveMem(memo, i, j):
        ## base cases
        if i == n1:
            return n2 - j
        
        if j == n2:
            return n1 - i
        
        ## check if the state is already compputed
        if memo[i][j] is not None:
            return memo[i][j]
        
        ans = math.inf
        
        if word1[i] == word2[j]:
            ans = min(ans, 0 + solveMem(memo, i+1, j+1))
        else:
            ## insert
            insert_ops = 1 + solveMem(memo, i, j+1)
            
            ## delete
            delete_ops = 1 + solveMem(memo, i+1, j)
            
            ## replace
            replace_ops = 1 + solveMem(memo, i+1, j+1)
            
            ans = min(ans, min(insert_ops, delete_ops, replace_ops))
        
        ## store the computed state
        memo[i][j] = ans
            
        return memo[i][j]
    
    
    def solveTab(n1, n2):
        ## initializing the dp array
        dp = [[math.inf]*(n2+1) for _ in range(n1+1)]
        
        for i in range(n1, -1, -1):
            for j in range(n2, -1, -1):
                
                ## base case filling
                if i == n1:
                    dp[i][j] = n2 - j
                    continue
                
                if j == n2:
                    dp[i][j] = n1 - i
                    continue
                
                ans = math.inf
                
                if word1[i] == word2[j]:
                    ans = min(ans, 0 + dp[i+1][j+1])
                else:
                    ## insert
                    insert_ops = 1 + dp[i][j+1]
                    
                    ## delete
                    delete_ops = 1 + dp[i+1][j]
                    
                    ## replace
                    replace_ops = 1 + dp[i+1][j+1]
                    
                    ans = min(ans, min(insert_ops, delete_ops, replace_ops))
                
                dp[i][j] = ans
        
        return dp[0][0]
    
    
    def spaceOpt(n1, n2):
        ## initializing 2 rows prev and curr
        prev = [math.inf]*(n2+1)
        curr = [math.inf]*(n2+1)
        
        for i in range(n1, -1, -1):
            for j in range(n2, -1, -1):
                
                ## base cases
                if i == n1:
                    curr[j] = n2 - j
                    continue
                
                if j == n2:
                    curr[j] = n1 - i
                    continue
                
                ans = math.inf
                
                if word1[i] == word2[j]:
                    ans = min(ans, 0 + prev[j+1])
                else:
                    ## insert
                    insert_ops = 1 + curr[j+1]
                    
                    ## delete
                    delete_ops = 1 + prev[j]
                    
                    ## replace
                    replace_ops = 1 + prev[j+1]
                    
                    ans = min(ans, min(insert_ops, delete_ops, replace_ops))
                
                curr[j] = ans
            
            prev = curr[:]
        
        return prev[0]
    
    ## initializing the memo array
    memo = [[None]*n2 for _ in range(n1)]
    
    return solveMem(memo, 0, 0), solveTab(n1, n2), spaceOpt(n1, n2)


word1 = "intention"; word2 = "execution"
dist = minDistance(word1, word2)
print(dist)


















