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

nums = [-1,0,0,0,0,3,3]
res = removeDuplicates(nums)
print(nums)
print(res)