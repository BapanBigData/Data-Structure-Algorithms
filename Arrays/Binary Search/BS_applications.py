import random

def binary_search(arr, target):
    si = 0
    ei = len(arr)-1
    
    while ei >= si:
        mid = (si+ei) // 2
        
        if arr[mid] == target:
            return mid
        
        elif target > arr[mid]:
            si = mid + 1
        
        else:
            ei = mid - 1
    
    return -1


# arr = [2, 3, 5, 9, 14, 16, 18]
# print(binary_search(arr, 16))

## find smallest number greater than or equal to target.
def ceiling(arr, target):
    si = 0
    ei = len(arr)-1
    
    res = None
    
    while ei >= si:
        mid = (si+ei) // 2
        
        if arr[mid] == target:
            return target
        
        elif arr[mid] > target:
            res = arr[mid]
            ei = mid-1
        
        else:
            si = mid+1
    
    return res


# arr = [2, 3, 5, 9, 14, 16, 18]
# target = 20
# print(ceiling(arr, target))        

## find the greatest number smaller than or equal to target.
def floor(arr, target):
    si = 0
    ei = len(arr)-1
    
    res = None
    
    while ei >= si:
        mid = (si+ei) // 2
        
        if arr[mid] == target:
            return arr[mid]
        
        elif arr[mid] < target:
            res = arr[mid]
            si = mid + 1
        
        else:
            ei = mid - 1
    
    return res   

# arr = [2, 3, 5, 9, 14, 16, 18]
# target = 1
# print(floor(arr, target))     

def first_occurrence(arr, target):
    si = 0
    ei = len(arr)-1
    
    while ei >= si:
        mid = (si+ei) // 2
        
        if target > arr[mid]:
            si = mid+1
        
        elif target < arr[mid]:
            ei = mid-1
        
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            
            else:
                ei = mid-1
    
    return -1

def last_occurrence(arr, target):
    si = 0
    ei = len(arr)-1
    
    while ei >= si:
        mid = (si+ei) // 2
        
        if target > arr[mid]:
            si = mid+1
        
        elif target < arr[mid]:
            ei = mid-1
        
        else:
            if mid == len(arr)-1 or arr[mid+1] != arr[mid]:
                return mid
            
            else:
                si = mid+1
    
    return -1


def first_last_occurrence(nums, target):
    
        def binary_search(nums, target, first_index):
            si = 0
            ei = len(nums)-1

            while ei >= si:
                mid = (si+ei) // 2

                if target > nums[mid]:
                    si = mid + 1
                
                elif target < nums[mid]:
                    ei = mid - 1
                
                else:
                    if first_index:
                        if mid == 0 or nums[mid-1] != nums[mid]:
                            return mid
                        else:
                            ei = mid - 1
                    else:
                        if mid == len(nums) - 1 or nums[mid+1] != nums[mid]:
                            return mid
                        else:
                            si = mid + 1
            
            return -1
        
        res = [-1, -1]

        res[0] = binary_search(nums, target, True)
        res[1] = binary_search(nums, target, False)

        return res

# nums = [5, 7, 7, 7, 7, 8, 8, 10]
# target = 7
# # print("First Occurrence:", first_occurrence(nums, target))
# # print("Last Occurrence:", last_occurrence(nums, target))
# print(first_last_occurrence(nums, target))


def find_position_infinite_array(arr, target):
    
    def binary_search(si, ei, target):
        
        while ei >= si:
            mid = (si+ei) // 2
        
            if arr[mid] == target:
                return mid
            
            elif target > arr[mid]:
                si = mid + 1
            
            else:
                ei = mid - 1
    
        return -1
    
    si = 0
    ei = 1
    
    while target > arr[ei]:
        ## start_index = end_index + 1
        new_si = ei + 1
        ## end_index = previous end_index + size of the window*2
        ei = ei + (ei - si + 1) * 2
        si = new_si
    
    return binary_search(si, ei, target)


# random_numbers = random.sample(range(1, 10001), 5000)
# random_numbers.sort()        
# print(random_numbers[:10])
# target = 16
# arr = [2, 3, 5, 9, 14, 16, 18]
# print(find_position_infinite_array(arr, target))


def mountain_peak(arr):
    si = 0
    ei = len(arr)-1
    
    while ei > si:
        mid = (si+ei) // 2
        
        ## we are in acceding part of arr,
        ## then mid can be potential answer, and that's why 
        ## ei ! = mid -1
        if arr[mid] > arr[mid+1]: 
            ei = mid
        
        ## we are in descending part of arr,
        else:
            si = mid + 1
    
    return si

## given a rotated sorted array,
## find the count of rotation 
def get_rotation_count(nums):
    
    def pivot_indx(si, ei):
        
        while ei >= si:
            mid = (si+ei) // 2
            
            if mid < ei and nums[mid] > nums[mid+1]:
                return mid
            
            if mid > si and nums[mid-1] > nums[mid]:
                return mid - 1
            
            if nums[si] >= nums[mid]:
                ei = mid - 1
            else:
                si = mid + 1
        
        return -1
    
    return pivot_indx(0, len(nums)-1) + 1

arr = [0, 1, 2, 3, 4, 5, 6, 7]
print(get_rotation_count(arr))
##############################################################################################################################
## 153. Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


def findMin(nums: list):
    si = 0
    ei = len(nums) - 1
    
    ## if the given array is not rotated or rotated by n times
    if nums[si] <= nums[ei]:
        return nums[si]
    
    peak = -1
    
    while si <= ei:
        
        mid = (si + ei) // 2
        
        if mid < ei and nums[mid] > nums[mid+1]:
            peak = mid
            break
        
        if mid > si and nums[mid-1] > nums[mid]:
            peak = mid-1
            break
        
        if nums[si] <= nums[mid]:
            si = mid + 1
        else:
            ei = mid - 1
    
    return nums[peak+1]

nums = [1, 2, 3]
mn = findMin(nums)
print(mn)