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


# nums = [1,2,3,4,5,6,7]; k = 3
# rotate(nums, k)
# print(nums)
##########################################################################################################################

## Right Rotate the given array by one place
def rightRotate(nums: list[int]): 
    n = len(nums)
    temp = nums[n-1]
    
    for i in range(n-2, -1, -1):
        nums[i+1] = nums[i]
    
    nums[0] = temp
    
    return

# nums = [1, 2, 3, 4, 5, 6, 7]
# rightRotate(nums)
# print(nums)

######################################################################################################################

## Right roatation by k places (in-place)
def rightRotateByK(nums: list[int], k: int):
    n = len(nums)
    k = k % n
    temp = nums[(n-k):]
    for i in range(n-k-1, -1, -1):
        nums[i+k] = nums[i]
    
    for i in range(k):
        nums[i] = temp[i]
    
    return


## Right rotate optimal soln

def rightRotateByK(nums: list[int], k: int):
    n = len(nums)
    k = k % n
    
    def reverse(s, e):
        while (e >= s):
            nums[s], nums[e] = nums[e], nums[s]
            
            s += 1
            e -= 1
        return
    
    reverse(0, n-k-1)
    reverse(n-k, n-1)
    reverse(0, n-1)
    
    return

# nums = [1, 2, 3, 4, 5, 6, 7]; k=3
# rightRotateByK(nums, 3)
# print(nums)
#######################################################################################################################
## Moves zeros to the end
## ** 283. Move Zeroes **
def moveZeroes(nums: list[int]):
    
    def bruteForce(nums):
        n = len(nums)
        
        temp = []
        for i in range(n):
            if (nums[i] != 0):
                temp.append(nums[i])
        
        nz = len(temp)
        for i in range(nz):
            nums[i] = temp[i]
        
        for i in range(nz, n):
            nums[i] = 0
        
        return
    
    def optimal(nums):
        n = len(nums)
        
        j = -1
        for i in range(n):
            if (nums[i] == 0):
                j = i
                break
            
        ## if there are no zeros
        if j == -1:
            return
        
        for i in range(j+1, n):
            if nums[i] != 0:
                ## swap
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        
        return
    
    optimal(nums)
    
    return

# nums = [1,2,3,1]
# moveZeroes(nums)
# print(nums)
############################################################################################################################
## Union of two sorted arrays
## ** Variation of merge two sorted array **

def findUnion(arr1: list[int], arr2: list[int]):
    
    def bruteForce(arr1, arr2):
        s = set()
        for e in arr1:
            s.add(e)
        
        for f in arr2:
            s.add(f)
        
        res = list(s)
        res.sort()
        
        return res
    
    
    def optimal(arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        
        i, j = 0, 0
        unionArr = []
        
        while (i < n1) and (j < n2):
            if (arr1[i] <= arr2[j]):
                if (not unionArr) or (unionArr[-1] != arr1[i]):
                    unionArr.append(arr1[i])
                
                i += 1
                
            else:
                if (not unionArr) or (unionArr[-1] != arr2[j]):
                    unionArr.append(arr2[j])
                
                j += 1
        
        
        while (j < n2):
            if (not unionArr) or (unionArr[-1] != arr2[j]):
                    unionArr.append(arr2[j])
                
            j += 1
        
        while (i < n1):
            if (not unionArr) or (unionArr[-1] != arr1[i]):
                    unionArr.append(arr1[i])
                
            i += 1
        
        return unionArr
    
    return optimal(arr1, arr2)


# arr1 = [2, 2, 3, 4, 5]; arr2 = [1, 1, 2, 3, 4]
# u = findUnion(arr1, arr2)
# print(u)

##################################################################################################################
## Intersection of two sorted arrays

def findIntersection(nums1: list[int], nums2: list[int]):
    
    def bruteForce(nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        visited = [0]*n2
        ans = set()
        
        for i in range(n1):
            for j in range(n2):
                if (nums1[i] == nums2[j]) and (not visited[j]):
                    ans.append(nums1[i])
                    visited[j] = 1
                    break
                
                if (nums2[j] > nums1[i]):
                    break
        
        return ans
    
    
    def optimal(nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        ans = set()
        
        while (i < n1) and (j < n2):
            if (nums1[i] < nums2[j]):
                i += 1
                
            elif (nums2[j] < nums1[i]):
                j += 1
                
            else: ## nums1[i] == nums2[j]
                ans.add(nums1[i])
                
                i += 1
                j += 1
        
        return ans
    
    return optimal(nums1, nums2)


arr1 = [1, 2, 2, 3, 3, 4, 5, 6]; arr2 = [2, 3, 3, 5, 6, 6, 7]
intersect = findIntersection(arr1, arr2)
print(intersect)


