## remove char of the given string
def removeChar(s: str, c: str):
    
    def remove(i, ans):
        ## base case
        if i == len(s):
            return ans
        
        if s[i] == c:
            return remove(i+1, ans=ans+'')
        else:
            return remove(i+1, ans=ans+s[i])
    
    return remove(0, '')


def removeChar1(s: str, c: str):
    
    def solver(i):
        ans = ''
        ## base case
        if i == len(s):
            return ans
        
        ans = '' if s[i] == c else s[i]
        
        fromBelowCalls = solver(i+1)
        ans = ans + fromBelowCalls
        
        return ans
    
    return solver(0)


# s = 'baccad'; c = 'a'
# print(removeChar1(s, c))

## skip word from the given string
def skipWord(s: str, word: str):
    
    def skip(i, ans):
        ## base case
        if i >= len(s):
            return ans
        
        if s.startswith(word, i):
            return skip(i+len(word), ans)
        else:
            return skip(i+1, ans+s[i])
    
    return skip(0, '')


def skipWord1(s: str, word: str):
    
    def solver(i):
        ans = ''
        ## base case
        if i == len(s):
            return ans
        
        if s.startswith(word, i):
            ans = ''
            fromBelowCalls = solver(i+len(word))
        else:
            ans = s[i]
            fromBelowCalls = solver(i+1)
        
        ans = ans + fromBelowCalls
        
        return ans
    
    return solver(0)


def skipAppNotApple(s: str):
    
    def skip(i, ans):
        ## base case
        if i == len(s):
            return ans
        
        if s.startswith('app', i) and not s.startswith('apple', i):
            return skip(i+3, ans)
        else:
            return skip(i+1, ans+s[i])
    
    return skip(0, '')

# txt = 'the curious cat chased the colorful butterfly through the lush garden.'; word = 'the'
# txt = 'bcgapplehowareyou'; word = 'apple'
# print(skipWord(txt, word))

# txt = 'I love apple app but appleapp'
# print(skipAppNotApple(txt))
##-----------------------------------------------------------------------------------------------------------
## Subsets problems
def subsetsStr(s: str):
    subsets = []
    
    def solver(i, ans):
        ## base case
        if i == len(s):
            subsets.append(ans)
            return subsets
        
        ## for each char I have two options, either take it or ignore it
        
        ## inclding the char
        solver(i+1, ans+s[i])
        
        ## ignoring the char
        solver(i+1, ans)
        return
    
    solver(0, '')
    
    return subsets

## lets pass the `subset` variable in the function argument
def subsetsStr1(s: str):
    
    def solver(i, ans, subset):
        ## base case
        if i == len(s):
            subset.append(ans)
            return subset
        
        ## include the char
        solver(i+1, ans+s[i], subset)
        
        ## exclude the char
        solver(i+1, ans, subset)
        
        return subset
    
    return solver(0, '', []) 

# s = 'abc'
# print(subsetsStr1(s))

###################################################################################################
## Subsets with list
def subsetsList(nums: list):
    subsets = []
    
    def solver(i, ans):
        ## base case
        if i == len(nums):
            subsets.append(ans)
            return subsets
        
        ## let's include the element
        solver(i+1, ans + [nums[i]])
        
        ## let's exclude the element
        solver(i+1, ans)
        
        return
    
    solver(0, [])
    
    return subsets


## let's pass the variable `subsets` in the function argument
def subsetsList1(nums: list):
    
    def solver(i, ans, subsets):
        ## base case
        if i == len(nums):
            subsets.append(ans)
            return subsets
        
        ## let's include the current element
        solver(i+1, ans + [nums[i]], subsets)
        
        ## let's exclude the currect element
        solver(i+1, ans, subsets)
        
        return subsets
    
    return solver(0, [], [])


## method3
def subsetsList2(nums: list):
    
    def solver(i, ans):
        lst = []
        ## base case
        if i == len(nums):
            lst.append(ans)
            return lst
        
        curr = nums[i]
        
        ## let's include the curr element
        incl = solver(i+1, ans+[curr])
        
        ## ignore the curr element
        excl = solver(i+1, ans)
        
        lst = incl + excl
        
        return lst
    
    return solver(0, [])


# nums = [3, 5, 9]
# print(subsetsList2(nums))
####################################################################################################################
## Let's print the subsets
def printSubsetsStr(s: str):
    
    def solver(i, subset):
        ## base case
        if i == len(s):
            print(subset)
            return 
        
        ## let's include the current char
        solver(i+1, subset + s[i])
        
        ## ingore the current char
        solver(i+1, subset)
        
        return
    
    solver(0, '')
    return


def printSubsetsList(nums: list):
    
    def solver(i, subset):
        ## base case
        if i == len(nums):
            print(subset)
            return
        
        ## include 
        solver(i+1, subset + [nums[i]])
        
        ## ignore
        solver(i+1, subset)
        
        return
    
    solver(0, [])
    
    return


# s = 'xyz'
# printSubsetsStr(s)
# nums = [3, 5, 9, 4, 2, 0, 6, 1, 7]
# printSubsetsList(nums)
#################################################################################################################
## Subsets Iteratively
def subsetsIter(nums: list) -> list[list]:
    subsets = []
    subsets.append([])
    
    for num in nums:
        n = len(subsets)
        for i in range(n):
            internal = subsets[i][:]
            internal.append(num)
            subsets.append(internal)
    
    return subsets

# nums = [3, 5, 9, 4]
# print(subsetsIter(nums))
#---------------------------------------------------------------------------------------------------------------------------------
## Subsets with Duplicates
def subsetsWithDuplicates(nums: list) -> list[list[int]]:
    ## sort the given array
    nums.sort()
    
    subsets = []
    subsets.append([])
    
    start = 0
    end = 0
    
    for i in range(len(nums)):
        n = len(subsets)
        start = 0
        ## if the curr and prev elements are equal
        if (i > 0) and (nums[i] == nums[i-1]):
            start = end + 1
        
        end = n - 1
        for j in range(start, n):
            internal = subsets[j][:]
            internal.append(nums[i])
            subsets.append(internal)
    
    return subsets

# nums = [1, 1, 1, 3, 1, 0, 1]
# print(subsetsWithDuplicates(nums))
##################################################################################################################################
## Let's calculate the number of function call while returing all the subsets
def numFunctionCalls(nums: list[int]) -> int:
    
    def solver(i):
        cnt = 0
        
        ## base case
        if i == len(nums):
            return 1
        
        ## include the current element
        incl = solver(i+1)
        
        ## ignore 
        excl = solver(i+1)
        
        cnt = incl + excl
        
        return cnt
    
    return solver(0)

nums = [1, 3, 4, 2, 5]
print(numFunctionCalls(nums))