
## ** 268. Missing Number **
def missingNumber(nums: list[int]) -> int:
    
    def solver():
        n = len(nums)

        ## take a hash array
        hashArr = [0]*(n+1)

        for num in nums:
            hashArr[num] = 1
        
        for i in range(n+1):
            if hashArr[i] == 0:
                return i
    
    def solver1():
        ## optimal soln
        n = len(nums)

        summ = n*(n+1) // 2

        return summ - sum(nums)
    
    return solver(), solver1()

# nums = [3, 0, 1]
# print(missingNumber(nums))
########################################################################################################################
## ** 485. Max Consecutive Ones **

def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxi = 0
    cnt = 0
    for num in nums:
        if num == 1:
            cnt += 1
            maxi = max(maxi, cnt)
        else:
            cnt = 0
    return maxi

# nums = [1, 1, 0, 1, 1, 1, 0, 1, 1]
# print(findMaxConsecutiveOnes(nums))
##################################################################################################################
## ** 540. Single Element in a Sorted Array **
## Try to solve it in O(log(n)) time

def singleNonDuplicate(nums: list[int]) -> int:
    
    def solver1(nums):
        ## initializing a dict
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
        for k, v in mp.items():
            if v == 1:
                return k
    
    def optimal(nums):
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor
    
    return solver1(nums), optimal(nums)

nums = [1,1,2,3,3,4,4,8,8]
res = singleNonDuplicate(nums)
print(res)