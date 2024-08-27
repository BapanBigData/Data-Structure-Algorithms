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


nums = [1,2,3,4,5,6,1]
k = 3
res = max_score(nums, k)
print(res)