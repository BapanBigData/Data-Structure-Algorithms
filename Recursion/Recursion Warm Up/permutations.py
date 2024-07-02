## Permutations
def permutationsStr(s: str) -> list[str]:
    
    def solver(i: int, proc: str, res: list):
        ## base case
        if i == len(s):
            res.append(proc)
            return res
        
        curr = s[i]
        
        for j in range(len(proc)+1):
            solver(i+1, proc[0:j] + curr + proc[j:len(proc)], res)
        
        return res
    
    return solver(0, proc='', res=[])


def printPermutationsStr(s: str) -> None:
    
    def solver(i: int, proc: str):
        ## base case
        if i == len(s):
            print(proc)
            return 
        
        curr = s[i]
        
        for j in range(len(proc)+1):
            solver(i+1, proc[0:j] + curr + proc[j:len(proc)])
        
        return
    
    solver(0, proc='')
    return

# s = 'cva'
# print(permutationsStr(s))
# printPermutationsStr(s)
############################################################################################################################################
## List permutations
def permutationsList(nums: list) -> list[list[int]]:
    
    def solver(i, permu, res):
        ## base case
        if i == len(nums):
            res.append(permu)
            return res
        
        curr = nums[i]
        
        for j in range(len(permu)+1):
            solver(i+1, permu[0:j] + [curr] + permu[j:len(permu)], res)
        
        return res
    
    return solver(0, permu=[], res=[])


def printPermutationsList(nums: list[int]) -> None:
    
    def solver(i, permu):
        ## base case
        if i == len(nums):
            print(permu)
            return 
        
        curr = nums[i]
        
        for j in range(len(permu)+1):
            solver(i+1, permu[0:j] + [curr] + permu[j:len(permu)])
        
        return 
    
    solver(0, permu=[])
    return

# nums = [1, 2, 5]
# print(permutationsList(nums))
# printPermutationsList(nums)

#########################################################################################################################
## Let's solve permutations Iteratively
def permutationsIter(nums: list[int]) -> list[list[int]]:
    # Start with an empty permutation
    permutations = [[]]
    
    for num in nums:
        new_permutations = []
        for perm in permutations:
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + [num] + perm[i:]
                new_permutations.append(new_perm)
                
        permutations = new_permutations
    
    return permutations

# nums = [1, 1, 2]
# print(permutationsIter(nums))

##-----------------------------------------------------------------------------------------------------------------------
## Leetcode:
## Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.
def permutationsWithDuplicates(nums: list[int]) -> list[int]:
    ## start with an empty permutation
    permutations = [[]]
    
    for num in nums:
        new_permutations = set()
        for perm in permutations:
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + [num] + perm[i:]
                new_permutations.add(tuple(new_perm))
                
        permutations = [list(p) for p in new_permutations]
    
    return permutations

# nums = [1, 1, 2, 1, 5]
# print(permutationsWithDuplicates(nums))

#########################################################################################################################
## Let's calculate number of function calls in permutations
def permutationsFunctionCalls(nums: list[int]) -> int:
    
    def solver(i, permu):
        cnt = 0
        ## base case
        if i == len(nums):
            return 1
        
        curr = nums[i]
        
        for j in range(len(permu)+1):
            cnt += solver(i+1, permu[0:j] + [curr] + permu[j:len(permu)])
        
        return cnt
    
    return solver(0, permu=[])

nums = [1, 2, 3, 4]
print(permutationsFunctionCalls(nums))