## is the given array sorted
def isSorted(arr: list) -> bool:
    
    def solver(i):
        ## base case
        if i == len(arr) - 1:
            return True
        
        if arr[i] <= arr[i+1]:
            return solver(i+1)
        else:
            return False
    
    return solver(0)


def isSorted1(arr: list) -> bool:
    
    def solver(i):
        ## base case
        if i == len(arr) - 1:
            return True
        
        return arr[i] <= arr[i+1] and solver(i+1)
    
    return solver(0)

# arr = [1, 3, 4, 5, 8, 8, 10, 11, 12]
# print(isSorted1(arr))

## linear search
def linearSearch(nums: list, target: int) -> int:
    
    def findIndex(i):
        ## base case
        if i == len(nums):
            return -1
        
        if nums[i] == target:
            return i
        else:
            return findIndex(i+1)
        
    return findIndex(0)

## given an array and a target, find all index 
def findAllIndex(nums: list, target: int) -> list:
    
    def solver(i):
        ## base case
        if i == len(nums):
            return 
        
        if nums[i] == target:
            res.append(i)
            
        return solver(i+1)
    
    res = []
    solver(0)
    
    return res

## now, I do not want to take the `res` variable outside of the function
def findAllIndex1(nums: list, target: int) -> list:
    
    def solver(i, res):
        ## base case
        if i == len(nums):
            return res
        
        if nums[i] == target:
            res.append(i)
        
        return solver(i+1, res)
    
    return solver(0, [])


def findAllIndex2(nums: list, target: int) -> list:
    
    ## return the list without passing in the argument
    def solver(i):
        res = []
        ## base case
        if i == len(nums):
            return res
        
        ## this will contain the answer from that function call only
        if nums[i] == target:
            res.append(i)
        
        ansFromBelowCalls = solver(i+1)
        
        res = res + ansFromBelowCalls
        
        return res
    
    return solver(0)

# nums = [3, 2, 1, 18, 9, 11, 1, 10, 12, 7]; target = 1
# print(findAllIndex2(nums, target))

## Rotated Binary Search
def rotatedBinarySearch(nums: list, target: int):
    
    def search(s, e):
        ## base case
        if s > e:
            return -1
        
        mid = (s + e) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[s] <= nums[mid]:
            if target >= nums[s] and target < nums[mid]:
                return search(s, mid-1)
            else:
                return search(mid+1, e)
        else:
            if target <= nums[e] and target > nums[mid]:
                return search(mid+1, e)
            else:
                return search(s, mid-1)
            
    
    return search(0, len(nums)-1)


nums = [5, 6, 1, 2, 3, 4]; target = 1
print(rotatedBinarySearch(nums, target))