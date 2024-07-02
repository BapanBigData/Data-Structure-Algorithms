## 46. Permutations
## Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def permutations(nums: list):

    def solver(start, n, res):
        if start == n:
            res.append(nums[:])
            return
        
        for i in range(start, n):
            nums[i], nums[start] = nums[start], nums[i]
            solver(start+1, n, res)

            ## back-tracking
            nums[i], nums[start] = nums[start], nums[i]
        
        return
    
    n = len(nums)
    res = []

    solver(start=0, n=n, res=res)
    return res

# nums = [1, 2, 3]
# res = permutations(nums)
# print(res)
############################################################################################
## 47. Permutations II
## Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

def permutations_II(nums: list):
    
    def solver(start, n, res):
        ## base case
        if start == n:
            res.append(nums[:])
            return

        used = set()
        for i in range(start, n):
            ## skip the duplicates number
            if nums[i] in used:
                continue

            used.add(nums[i])

            nums[i], nums[start] = nums[start], nums[i]
            solver(start+1, n, res)

            ## back-tracking
            nums[i], nums[start] = nums[start], nums[i]
        
        return
    
    n = len(nums)
    result = []

    solver(start=0, n=n, res=result)
    return result

# nums = [1, 1, 2, 2]
# res = permutations_II(nums)
# print(res)
#############################################################################################################################


