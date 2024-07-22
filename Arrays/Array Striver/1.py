import math
from ordered_set import OrderedSet

def secondLargest(nums: list[int]) -> int:
    ## can do better 
    def solver():
        n = len(nums)
        largest = max(nums)
        second = -1
        for i in range(n):
            if (nums[i] > second) and (nums[i] != largest):
                second = nums[i]
                
        return second
    
    return solver()


## get second largest and second smallest elements

def getSecondOrderElements(a: list[int]) -> list[int]:
    n = len(a)
    
    def getSecondLargest(n, a):
        largest, slargest = a[0], -1
        for i in range(1, n):
            if (a[i] > largest):
                slargest = largest
                largest = a[i]

            elif (a[i] < largest) and (a[i] > slargest):
                slargest = a[i]
        
        return slargest


    def getSecondSmallest(n, a):
        smallest, ssmallest = a[0], math.inf
        for i in range(1, n):
            if a[i] < smallest:
                ssmallest = smallest
                smallest = a[i]
            
            elif (a[i] > smallest) and (a[i] < ssmallest):
                ssmallest = a[i]

        return ssmallest

    slargest = getSecondLargest(n, a)
    ssmallest = getSecondSmallest(n, a)
    
    return [slargest, ssmallest]


# nums = [2, 3, -1, 5, 3, 7, 9, 5, 9, 8, 2, 11]
# # print(secondLargest(nums))
# res = getSecondOrderElements(nums)
# print(res)
##########################################################################################
## check if the given array is sorted
def isSorted(nums: list[int]) -> bool:
    n = len(nums)
    
    def solver(i):
        ## b.c 
        if (i == n-1) or (i == n):
            return True
        
        if nums[i+1] >= nums[i]:
            return solver(i+1)
        
        return False
    
    return solver(0)

# nums = [1, 2, 2, 3, 3, 3, 4, 5, 6]
# print(isSorted(nums))
###############################################################################################
## Remove duplicates from sorted array
def removeDuplicates(nums: list[int]):
    n = len(nums)
    
    def bruteForce():
        s = OrderedSet()
        
        for i in range(n-1, -1, -1):
            s.add(nums[i])
        
        i = 0
        while s:
            nums[i] = s.pop()
            i += 1
        
        return i
    
    def optimalSoln():
        i = 0
        for j in range(1, n):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
                
        return i+1
    
    return optimalSoln()

# nums = [-1,0,0,0,0,3,3]
# res = removeDuplicates(nums)
# print(nums)
# print(res)
#########################################################################################################################################
## Left rotate the given array by one place (in-place rotate)
def leftRotate(arr: list[int]):
    n = len(arr)
    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    
    return

# arr = [1, 2, 3, 4, 5, 6]
# leftRotate(arr)
# print(arr)


## left rotate by k

def rotate(nums: list[int], k: int):
    n = len(nums)
    k = k % n
    temp = nums[:k]
    
    for i in range(k, n):
        nums[i-k] = nums[i]
    
    for i in range(n-k, n):
        nums[i] = temp[i-(n-k)]
    
    return


## left rotate most optimal soln

def rotate(nums: list[int], k: int):
    n = len(nums)
    k = k % n
    
    def reverse(s, e):
        while (e >= s):
            nums[s], nums[e] = nums[e], nums[s]    
            s += 1
            e -= 1
        return
    
    reverse(0, k-1)
    reverse(k, n-1)
    reverse(0, n-1)
    
    return


nums = [1,2,3,4,5,6,7]; k = 3
rotate(nums, k)
print(nums)
