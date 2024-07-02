import math
import heapq
import collections

def reverse_array(arr):
    i = 0
    j = len(arr)-1
    
    for _ in range(len(arr)//2):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
        
    return True

# arr = [7, 1, 0, 4]
# reverse_array(arr)
# # arr.reverse()
# print(arr)

# arr = [7, 10, 4, 3, 20, 15]
# heapq.heapify(arr)
# heapq.heappop(arr)
# heapq.heappop(arr)
# print(arr)

# def k_smallest_n_largest_element(arr, k):
#     def solver(smallest: bool):
#         ## T.C: O(n + k*log(n))
#         if smallest:
#             ## T.C: O(n)
#             heapq.heapify(arr)
#             ## T.C: O(k*log(n))
#             for _ in range(k-1):
#                 heapq.heappop(arr)  
#             return arr[0]  
#         else:
#             arr_ = list(map(lambda x: -x, arr))
#             ## T.C: O(n)
#             heapq.heapify(arr_)
#             ## T.C: O(k*log(n))
#             for _ in range(k-1):
#                 heapq.heappop(arr_)
#             return -arr_[0]
        
#     k_smallest = solver(True)
#     k_largest = solver(False)
    
#     return k_smallest, k_largest


# def k_smallest_n_largest_element(arr, k):
#     def solver(smallest: bool, heap_ds):
#         ## T.C: O(n*log(k))
#         if smallest:
#             ## use max Heap
#             ## T.C: O(n*log(k))
#             for e in arr:
#                 heapq.heappush(heap_ds, -e)
#                 if len(heap_ds) > k:
#                     heapq.heappop(heap_ds)
#             return -heap_ds[0]
#         ## largest element
#         else:
#             ## use min heap
#             ## T.C: O(n*log(k))
#             for e in arr:
#                 heapq.heappush(heap_ds, e)
#                 if len(heap_ds) > k:
#                     heapq.heappop(heap_ds)
#             return heap_ds[0]
        
#     k_smallest = solver(True, heap_ds=[])
#     k_largest = solver(False, heap_ds=[])
    
#     return k_smallest, k_largest

def k_smallest_n_largest_element(nums, k):
    def solver(smallest: bool):
        ## k smallest element
        ## T.C: O(k + (n-k)*log(k))
        if smallest:
            arr = [-e for e in nums[:k]]
            ## build heap (max heap)
            ## T.C O(k)
            heapq.heapify(arr)
            
            ## T.C O((n-k)*log(k))
            for i in range(k, len(nums)):
                if -nums[i] > arr[0]:
                    
                    # poping from heap 
                    heapq.heappop(arr)
                    
                    # insert into the heap
                    heapq.heappush(arr, -nums[i])
                    
            return [-e for e in arr][0]
        ## k largest element
        ## T.C: O(k + (n-k)*log(k))
        else:
            arr = nums[:k]
            ## build heap (min heap)
            ## T.C O(k)
            heapq.heapify(arr)
            
            ## T.C O((n-k)*log(k))
            for i in range(k, len(nums)):
                ## in the top of the heap the smallest element will be there
                ## if the current element is greater than top of the heap, then
                ## remove the minimum element from the heap and push current 
                ## element to the heap.
                if nums[i] > arr[0]:

                    # poping from heap (min extraction)
                    heapq.heappop(arr)
                    
                    # insert into the heap
                    heapq.heappush(arr, nums[i])
            
            return arr[0]
        
    k_smallest = solver(True)
    k_largest = solver(False)
    
    return k_smallest, k_largest

# arr = [5, 30, 20, 3, 4, 6, 5, 25]
# print(k_smallest_n_largest_element(arr, 3))

def sort_0_1(arr):
    pass

def sort_0_1_2(arr):
    temp = [1] * len(arr)
    nZ = 0
    nT = len(arr) - 1
    
    for i in range(len(arr)):
        if arr[i] == 0:
            temp[nZ] = 0
            nZ += 1
        elif arr[i] == 2:
            temp[nT] = 2
            nT -= 1
    return temp


def sort_0_1_2_efficient(arr):
    i = 0 ## represnting zeros
    j = 0 ## representing ones
    k = len(arr) - 1 ## representing twos
    
    while j <= k:
        if arr[j] == 1:
            j += 1
        elif arr[j] == 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        elif arr[j] == 2:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
    return

# # arr = [1, 1, 0, 0, 2, 0, 1, 2, 1, 0]
# arr = [2, 1, 1, 2, 1, 0, 1, 0, 0, 2, 1, 0, 1]
# # arr = [0, 1, 0, 2, 2]
# sort_0_1_2_efficient(arr)
# print(arr)

## 347. Top K Frequent Elements (Leetcode)

# nums = [1, 2, 3, 4, 5, 6, 3]
# counters = collections.Counter(nums)
# print(counters)
# print(counters.keys())
# print(counters.values())
# arr = [(-c, e) for e, c in zip(counters.keys(), counters.values())]
# print(arr)

def Top_K_Frequent_Elements(nums, k):
        if len(nums) == k:
            return nums
        
        counters = collections.Counter(nums)
        arr = [(cnt, ele) for ele, cnt in zip(counters.keys(), counters.values())]
        heap_ds = arr[:k]

        ## build the min heap
        heapq.heapify(heap_ds)

        for i in range(k, len(arr)):
            if arr[i][0] > heap_ds[0][0]:
                ## pop from the heap (min extraction)
                heapq.heappop(heap_ds)

                ## push in the heap
                heapq.heappush(heap_ds, arr[i])

        return [ele for cnt, ele in heap_ds]
    
# nums = [1, 1, 1, 2, 2, 3]
# print(Top_K_Frequent_Elements(nums, 2))


def negatives_to_a_side(arr):
    i = 0 ## representing the negatives
    j = len(arr) - 1 ## representing the positives
    
    while j > i :
        ## 
        if arr[i] > 0 and arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] > 0 and arr[j] > 0:
            j -= 1
        elif arr[i] < 0 and arr[j] < 0:
            i += 1
        else:
            i += 1
            j -= 1
    return

# nums = [2, 3, -4, -1, 6, -9]
# negatives_to_a_side(nums)
# print("::", nums)

def rearrange_array(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return 

# nums = [2, 3, -4, -1, 6, -9]
# rearrange_array(nums)
# print(":::", nums)

# Example usage:
# arr = [2, -4, 6, -8, 5, -1, 9, -3]
# n = len(arr)

# rearrange_array(arr, n)
# print(arr)

# arr = [-12, 11, -13, -5, 6, -7, 5]
# negatives_to_a_side(arr)
# print(arr)

def get_subarrays(arr):
    subarrays = []
    for start in range(len(arr)):
        for end in range(start, len(arr)):
            subarray = arr[start:end+1]
            subarrays.append(subarray)
    return subarrays

arr = [2, 3, -2, 4]
print(get_subarrays(arr))

def max_subarray_sum_naive(arr):
    maxSum = 0
    for start in range(len(arr)):
        for end in range(start, len(arr)):
            subarray = arr[start:end+1]
            maxSum = max(maxSum, sum(subarray))
    return maxSum

## Kadane's Algo 
# def max_subarray_sum(arr):
#     currSum = 0
#     maxSum = -math.inf
#     for e in arr:
#         currSum += e
#         maxSum = max(currSum, maxSum)
#         if currSum < 0:
#             currSum = 0
#     return maxSum

def max_subarray_sum(nums):
    ## it will store max sum till that point
    curr_max = nums[0]
    
    ## max sum so far
    max_sum_so_far = nums[0]
    
    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        max_sum_so_far = max(curr_max, max_sum_so_far)
    
    return max_sum_so_far

## the code to find max suarray product 
## will fail where are is negative number at the
## middle of the array
def max_subarray_product_(nums):
    currProduct = 1
    maxProduct = -math.inf
    for i in range(len(nums)):
        currProduct *= nums[i]
        maxProduct = max(currProduct, maxProduct)
        if currProduct == 0:
            currProduct = 1
    
    return maxProduct

## this is more generic and will pass all the test cases
def max_subarray_product(nums):
    n = len(nums)
    left_product = 1
    right_product = 1
    max_product = nums[0]
    
    for i in range(n):
        left_product = 1 if left_product == 0 else left_product
        right_product = 1 if right_product == 0 else right_product
        
        left_product *= nums[i]
        right_product *= nums[n-1-i]
        
        max_product = max(max_product, max(left_product, right_product))
    
    return max_product
    

# nums = [2, 3, -2, 4]
nums = [3, -1, 4]
print(max_subarray_product(nums))
        

# print(get_subarrays([5, 4, -1, 7, 8]))
# arr = [5, 4, -1, 7, 8]
# maxSum = max_subarray_sum(arr)
# print(maxSum)

## Kadane's Algo 
def longest_even_odd(nums):
    res = 1
    curr = 1
    for i in range(1, len(nums)):
        if (nums[i] % 2 == 0 and nums[i-1] % 2 == 0) or \
            (nums[i] % 2 != 0 and nums[i-1] % 2 != 0):
                curr += 1
                res = max(curr, res)
        else:
            curr = 1
    return res

# nums = [2, 5, 7, 2, 4, 6, 8, 3]
# print(longest_even_odd(nums))


def find_duplicates(nums):
    ## set the slow ans fast pointers 
    ## to same index, and runs a loop until 
    ## they meet.
    slow, fast = 0, 0
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    ## now run the slow and fast pointers to the 
    ## same pace, and run the loop untill they met.
    ## when they meet return the slow pointer.
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


def merge_interval(intervals):
    if not intervals:
        return []
    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])
    ## initializing a new interval, which will store 
    ## all the modified intervals, if there are any 
    ## overlapping intervals, initializing with the
    ## first interval
    new_intervals = [intervals[0]]
    for curr in intervals[1:]:
        ## start time of current interval is less than 
        ## end time of the last interval of the new intervals
        ## (modified intervals)
        if curr[0] <= new_intervals[-1][-1]:
            ## modify the end time in the new interval
            new_intervals[-1][-1] = max(curr[-1], new_intervals[-1][-1])
        else:
            new_intervals.append(curr)
        
    return new_intervals

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 4], [0, 0]]
# print(merge_interval(intervals))

def next_permutation(nums):
    if len(nums) == 1:
        return
    
    ## step1:
    indx1 = -1
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            indx1 = i
            break
    ## all the elements are in decending orders
    if indx1 < 0:
        nums[:] = nums[::-1]
        # nums.reverse()
        
    ## step2:
    else:
        indx2 = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[indx1]:
                indx2 = i
                break
        ## step3:
        ## swap
        nums[indx1], nums[indx2] = nums[indx2], nums[indx1]
        
        ## step4:
        ## sort the the portion from 
        ## indx1+1 to end
        nums[indx1+1:] = sorted(nums[indx1+1:])
    
    return
        
# nums = [4, 1, 5, 3, 2]
# print("Before:", id(nums))
# next_permutation(nums)
# print(nums)
# print("After:", id(nums))

def merge(left, right, nums):
    i, j, k = 0, 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
            k += 1
        else:
            nums[k] = right[j]
            j += 1
            k += 1
    
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
    
    return
        

def merge_sort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    
    # s = 0
    # e = len(nums) - 1
    mid = len(nums) // 2
    
    left = nums[:mid]
    right = nums[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge(left, right, nums)


# nums = [1, 20, 6, 4, 5]
# merge_sort(nums)
# print(nums)

## Application of Merge sort Amazon Interview question 
def cnt_inversion_merge(left, right, nums):
    i, j, k = 0, 0, 0
    cnt_inv = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            cnt_inv += len(left) - i
            j += 1
        k += 1
    
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
    
    return cnt_inv

def cnt_inversion(nums):
    if len(nums) <= 1:
        return 0
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    
    cnt_inv = 0
    
    cnt_inv += cnt_inversion(left)
    cnt_inv += cnt_inversion(right)
    cnt_inv += cnt_inversion_merge(left, right, nums)
    
    return cnt_inv

# # nums = [1, 20, 6, 4, 5]
# # nums = [20, 6, 5, 4, 1]
# nums = [1, 4, 5, 6, 20]
# inv_cnt = cnt_inversion(nums)
# print(inv_cnt)
# print(nums)

## best time to buy and sell stock
def max_profit(prices):
    n = len(prices)
    maxSelling = prices[n-1]
    maxProfit = 0
    for i in range(n-2, -1, -1):
        maxSelling = max(maxSelling, prices[i])
        maxProfit = max(maxProfit, maxSelling-prices[i])
    return maxProfit

# nums = [7, 1, 5, 3, 6, 4]
# print(max_profit(nums))

# def common_elements(A: list, B: list, C: list):
#     i, j, k = 0, 0, 0
#     res = []
#     prev1, prev2, prev3 = -math.inf, -math.inf, -math.inf
    
#     while i < len(A) and j < len(B) and k < len(C):
#         while i < len(A) and A[i] == prev1:
#             i += 1
#         while j < len(B) and B[j] == prev2:
#             j += 1
#         while k < len(C) and C[k] == prev3: 
#             k += 1
#         if i < len(A) and j < len(B) and k < len(C) and A[i] == B[j] == C[k]:
#             res.append(A[i])
#             prev1 = A[i]
#             prev2 = B[j]
#             prev3 = C[k]
#             i += 1
#             j += 1
#             k += 1
#         else:
#             ## A[i] is the smallest
#             if i < len(A) and j < len(B) and k < len(C) and A[i] < B[j] <= C[k]:
#                 prev1 = A[i]
#                 i += 1
#             ## B[j] is the smallest
#             elif i < len(A) and j < len(B) and k < len(C) and  B[j] < A[i] <= C[k]:
#                 prev2 = B[j]
#                 j += 1
#             ## C[k] is the smallest
#             else:
#                 if k < len(C):
#                     prev3 = C[k]
#                     k += 1
    
#     return res 

def common_elements(ar1, ar2, ar3, n1, n2, n3):
    i, j, k = 0, 0, 0
    ans = []
    prev1 = prev2 = prev3 = float('-inf')
        
    while i < n1 and j < n2 and k < n3:
        while ar1[i] == prev1 and i < n1:
            i += 1
            
        while ar2[j] == prev2 and j < n2:
            j += 1
            
        while ar3[k] == prev3 and k < n3:
            k += 1
            
        if ar1[i] == ar2[j] == ar3[k]:
            ans.append(ar1[i])
            prev1 = ar1[i]
            prev2 = ar2[j]
            prev3 = ar3[k]
            i += 1
            j += 1
            k += 1
        elif ar1[i] < ar2[j]:
            prev1 = ar1[i]
            i += 1
        elif ar2[j] < ar3[k]:
            prev2 = ar2[j]
            j += 1
        else:
            prev3 = ar3[k]
            k += 1
        
    return ans
                
# a = [1, 5, 10, 20, 40, 80]
# b = [6, 7, 20, 80, 100]
# c = [3, 4, 15, 20, 30, 70, 80, 120]    
# a = [3, 3, 3, 3]
# b = [3, 3, 3]
# c = [3, 3, 3, 3, 3, 3]
# print(common_elements(a, b, c, 4, 3, 6))


## You are given a 0-indexed integer array nums of even length consisting of an equal number 
## of positive and negative integers.
## The rearranged array begins with a positive integer.

## case1: order does not matter
def rearrange_negatives_positivesI(arr):
    i = 0
    j = len(arr) - 1
    ## this will rearrange the array
    ## [-ve, -ve, ... -ve, +ve, +ve, ... +ve]
    while j >= i:
        if arr[i] > 0 and arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] < 0:
            i += 1
        elif arr[j] > 0:
            j -= 1
    # return arr[i]
    ## i pointer now will indicates 
    ## the first +ve element
    k = 0
    while k < len(arr) and i < len(arr):
        arr[i], arr[k] = arr[k], arr[i]
        i += 1
        k += 2
    return


## Rotation of an array to the right by k steps
def get_reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return

def rotate_right(nums, k):
    n = len(nums)
    k = k % n
    
    get_reverse(nums, 0, n-k-1)
    get_reverse(nums, n-k, n-1)
    get_reverse(nums, 0, n-1)
    
    return

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]
# print("Before:", id(nums))
# k = 102
# # nums = nums[k+1:] + nums[:k+1]
# rotate_right(nums, k)
# print(nums)
# print("After:", id(nums))


## case2: For all integers with the same sign, the order in which they were present in nums is preserved.
## solve it without taking any extra space.

def rightRotate(nums, si, ei, k=1):
    n = len(nums[si:ei])
    
    def get_reverse(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return
    
    get_reverse(nums, 0, n-k-1)
    get_reverse(nums, n-k, n-1)
    get_reverse(nums, 0, n-1)
    
    return

def rearrange_negatives_positivesII(nums):
    wrongPlaced = -1
    
    for i in range(len(nums)):
        if wrongPlaced >= 0:
            if (nums[wrongPlaced] >= 0 and nums[i] < 0) or \
                (nums[wrongPlaced] < 0 and nums[i] >= 0):
                    rightRotate(nums, wrongPlaced, i)
                    if (i - wrongPlaced) > 2:
                        wrongPlaced += 2
                    else:
                        wrongPlaced = -1
        if wrongPlaced == -1:
            if (nums[i] >= 0 and i % 2 != 0) or (nums[i] < 0 and i % 2 == 0):
                wrongPlaced = i
    
    return


# # arr = [3, -4, -1, 6, -9, 10, 11, -12, 12, 5, -8]
# arr = [2, 3, -4, -1, 6, -9]
# # arr = [1, 4, -2, 3, -1, 6, -4, -8]
# # arr = [-1, 2, 3, -5] ## output: [2, -1, 3, -5]
# # arr = [-1, 1]
arr = [2, 3, -4, -1, 6, -9]
rearrange_negatives_positivesII(arr)
print(arr)