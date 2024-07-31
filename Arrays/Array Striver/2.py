# ** 268. Missing Number **
def missing_number(nums: list[int]) -> int:

    def solver():
        n = len(nums)

        # take a hash array
        hashArr = [0]*(n+1)

        for num in nums:
            hashArr[num] = 1

        for i in range(n+1):
            if hashArr[i] == 0:
                return i

    def solver1():
        # optimal soln
        n = len(nums)

        summ = n*(n+1) // 2

        return summ - sum(nums)

    return solver(), solver1()

# nums = [3, 0, 1]
# print(missing_number(nums))
############################################################################

# ** 485. Max Consecutive Ones **


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
############################################################################

# ** 540. Single Element in a Sorted Array **
# Try to solve it in O(log(n)) time


def singleNonDuplicate(nums: list[int]) -> int:

    def solver1(nums):
        # initializing a dict
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


# nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
# res = singleNonDuplicate(nums)
# print(res)

###########################################################################

# **Longest subarray with given sum k**
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
# Note: when nums contains both positive and negative the prefix sum
# method is the optimal soln

def longest_subarray(nums: list[int], k):
    n = len(nums)

    def prefix_sum_solver(n):
        prefix_summ = {}
        lenn = 0
        curr_summ = 0
        for i in range(n):
            curr_summ += nums[i]

            if (curr_summ == k):
                lenn = max(lenn, i+1)

            if (curr_summ - k) in prefix_summ:
                lenn = max(lenn, (i - prefix_summ[curr_summ-k]))

            if curr_summ not in prefix_summ:
                prefix_summ[curr_summ] = i

        return lenn

    return prefix_sum_solver(n)


# when the nums array contains only positive and
# zeros we can still optimize the prefix sum soln
# two pointers approach

def longest_subarray_positives(nums: list[int], k: int):
    n = len(nums)
    i, j = 0, 0
    curr_summ = nums[0]
    maxLen = 0

    while (i < n):
        while (j <= i) and (curr_summ > k):
            curr_summ -= nums[j]
            j += 1

        if (curr_summ == k):
            maxLen = max(maxLen, i - j + 1)

        i += 1
        if (i < n):
            curr_summ += nums[i]

    return maxLen


nums = [1, 2, 1, 3]
k = 2
res = longest_subarray_positives(nums, k)
print(res)
#######################################################################

# Number of subarray with sum k
# **560. Subarray Sum Equals K**
# Given an array of integers nums and an integer k
# return the total number of subarrays whose sum equals to k.


def numberSubArrays(nums: list[int], k: int):
    n = len(nums)

    # initializing the prefix sum map
    prefix_summ_mp = {}
    prefix_summ_mp[0] = 1

    curr_summ = 0
    cnt = 0
    for i in range(n):
        curr_summ += nums[i]

        rem = curr_summ - k
        if rem in prefix_summ_mp:
            cnt += prefix_summ_mp[rem]

        if curr_summ in prefix_summ_mp:
            prefix_summ_mp[curr_summ] += 1
        else:
            prefix_summ_mp[curr_summ] = 1

    return cnt


nums = [2, 0, 0, 0, 3]
k = 3
res = numberSubArrays(nums, k)
print(res)
