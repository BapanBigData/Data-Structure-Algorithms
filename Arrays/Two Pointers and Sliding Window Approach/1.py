# 1423. Maximum Points You Can Obtain from Cards

def max_score(nums: list[int], k: int) -> int:
    n = len(nums)
    
    left_sum, right_sum = 0, 0
    max_sum = 0
    
    for i in range(k):
        left_sum = left_sum + nums[i]
        max_sum = left_sum
    
    i = k-1
    j = n-1
    
    while (i >= 0):
        left_sum = left_sum - nums[i]
        right_sum = right_sum + nums[j]
        
        max_sum = max(max_sum, (left_sum + right_sum))
        
        i -= 1
        j -= 1
    
    return max_sum

# nums = [1,2,3,4,5,6,1]
# k = 3
# res = max_score(nums, k)
# print(res)

############################################################################################################

# 3. Longest Substring Without Repeating Characters

def length_of_longest_substring(s: str) -> int:
    
    def solver():
        n = len(s)
        max_len = 0

        for i in range(n):
            mapp = {}
            for j in range(i, n):
                if s[j] in mapp:
                    break
                
                l = j - i + 1
                max_len = max(max_len, l)

                mapp[s[j]] = 1
        
        return max_len 
    
    
    def optimal_solver():
        n = len(s)
        
        max_len = 0
        
        l, r = 0, 0
        mapp = {}
        
        while (r < n):
            
            if s[r] in mapp:
                if (mapp[s[r]] >= l):
                    l = mapp[s[r]] + 1
            
            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            
            mapp[s[r]] = r
            r += 1
        
        return max_len
    
    return solver(), optimal_solver()

# s = "abba"
# res = length_of_longest_substring(s)
# print(res)
########################################################################################################################

# 1004. Max Consecutive Ones III

def longest_ones(nums: list[int], k: int):
    n = len(nums)
    
    def solver():
        max_len = 0
        
        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if (nums[j] == 0):
                    zeros += 1
                
                if (zeros <= k):
                    curr_len = j - i + 1
                    max_len = max(max_len, curr_len)
                else:
                    break
        
        return max_len
    
    def better_solver():
        max_len = 0
        zeros = 0
        l, r = 0, 0
        
        while (r < n):
            if (nums[r] == 0):
                zeros += 1
            
            while (zeros > k):
                if (nums[l] == 0):
                    zeros -= 1
                    
                l += 1
            
            if (zeros <= k):
                curr_len = r - l + 1
                max_len = max(max_len, curr_len)
            
            r += 1
        
        return max_len
    
    
    def optimal_solver():
        max_len = 0
        zeros = 0
        l, r = 0, 0
        
        while (r < n):
            if (nums[r] == 0):
                zeros += 1
            
            if (zeros > k):
                if (nums[l] == 0):
                    zeros -= 1
                    
                l += 1
            
            if (zeros <= k):
                curr_len = r - l + 1
                max_len = max(max_len, curr_len)
            
            r += 1
        
        return max_len
    
    return better_solver(), optimal_solver()


nums = [1,1,1,0,0,0,1,1,1,1,0]; k = 2
res = longest_ones(nums, k)
print(res)

