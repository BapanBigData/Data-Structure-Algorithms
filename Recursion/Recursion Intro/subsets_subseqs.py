import collections

## subset sum to k
def subset_sum_k(nums, k):

    def solver(i, subset, k, n, res):
        ## base case
        if i == n:
            if k == 0:
                res.append(subset)
                return
            else:
                return
        
        ## there are two options include and exclude
        solver(i+1, subset + [nums[i]], k-nums[i], n, res)
        solver(i+1, subset, k, n, res)

        return
    
    res = []
    solver(0, [], k, len(nums), res)

    return res

# arr = [2, 3, 6, 7]
# k = 7
# ans = subset_sum_k(arr, k)
# print(ans)

## Leetcode 39. Combination Sum
## i/p: nums = [2, 3, 6, 7], target = 7
## o/p: [[2, 2, 3], [7]]

def combination_sum(nums, target):
    
    def solver(start, target, subset, res):
        ## base case
        if target == 0:
            res.append(subset)
            return
        
        for i in range(start, len(nums)):
            if (target-nums[i]) >= 0:
                solver(i, target-nums[i], subset+[nums[i]], res)
        
        return
    
    res = []
    solver(0, target, [], res)
    return res

# # arr = [2, 3, 6, 7]
# target = 8
# ans = combination_sum(arr, target)
# print(ans)
##################################################################################################
## 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates 
# where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

def combination_sum_2(candidates: list, target: int):
    
    def solver(counter, start, target, subset, res):
        ## base case
        if target == 0:
            res.append(subset)
            return
        
        for i in range(start, len(counter)):
            candi, freq = counter[i]

            if freq <= 0:
                continue

            if (target - candi) >= 0:
                counter[i] = (candi, freq-1)
                solver(counter, i, target-candi, subset+[candi], res)

                ## backtrack
                counter[i] = (candi, freq)
        
        return
    
    result = []

    counter = collections.Counter(candidates)
    counter = [(c, counter[c]) for c in counter]

    solver(counter=counter, start=0, target=target, subset=[], res=result)

    return result

arr = [10, 1, 2, 7, 6, 1, 5]
nums = [2, 5, 2, 2, 2]
k = 4
res = combination_sum_2(nums, k)
print(res)