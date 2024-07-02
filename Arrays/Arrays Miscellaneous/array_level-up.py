import math

# def fn(lst: list):
#     print(id(lst))
#     return

# lst = [1, 2, 3, 4, 5]
# print(id(lst))
# fn(lst)


## pair sum
## the below solution is using extra space
## and the time complexity is O(n)
def pair_sum(nums, x):
    s = set()
    res = []
    for i in range(len(nums)):
        comp = x - nums[i]
        if comp in s:
            res.append(comp)
            res.append(nums[i])
            return res
        ## add the element into the set
        s.add(nums[i])
    return res


## No extra space is using but
## the time complexity is O(nlogn)
def pair_sum_(nums, x):
    ## T.C: O(nlogn) + O(n)
    res = []
    nums.sort() ## O(nlogn)
    i = 0
    j = len(nums) - 1
    ## O(n)
    while j > i:
        if nums[i] + nums[j] == x:
            res.append(nums[i])
            res.append(nums[j])
            return res
        
        if nums[i] + nums[j] > x:
            j -= 1
        else:
            i += 1
    return res

# nums = [10, 5, 2, 3, -6, 9, 11]
# x = 4
# print(pair_sum_(nums, x))

## triplet sum
## two pointer approach
def triplet_sum(nums, target):
    n = len(nums)
    ## sorting the given array
    nums.sort()
    res = []
    for i in range(n-2):
        ## two pointer approach
        j = i + 1
        k = n - 1
        
        while k > j:
            curr_sum = nums[i]
            curr_sum += nums[j]
            curr_sum += nums[k]
            
            if curr_sum == target:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            
            elif curr_sum > target:
                k -= 1
            
            else:
                j += 1
    return res
                
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
# nums = [-1, 0, 1, 2, -1, -4]
# # nums = [0, 0, 0]
# target = 0
# print(triplet_sum(nums, target))        


## longest mountain (Leetcode 845)

def longest_mountain(arr):
    n = len(arr)
    longest = 0
    i = 1
    
    while i <= n-2:
        ## check if arr[i] is a peak or not
        ## got the peak 
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            
            cnt = 1
            
            ## going backward direction
            j = i
            while j >= 1 and arr[j] > arr[j-1]:
                cnt += 1
                j -= 1
            
            ## going forward direction
            while i <= n-2 and arr[i] > arr[i+1]:
                cnt += 1
                i += 1
            
            longest = max(longest, cnt)
        
        else:
            i += 1
    
    return longest

# arr = [5, 6, 1, 2, 3, 4, 5, 4, 3, 2, 0, 1, 2, 3, -2, 4]
# print(longest_mountain(arr)) 


## get the peak index in
## a mountain array

def peak_indx(arr):
    si = 0
    ei = len(arr)-1
    while ei > si:
        mid = (si+ei) // 2
        
        if arr[mid] > arr[mid+1]:
            ei = mid
        else:
            si = mid + 1
    return si

# arr = [2, 3, 5, 6, 7, 2, 1, 0]
# print(peak_indx(arr))


## longest band in an given array

def longest_band(arr):
    ## insert data into the set
    unordered_set = set(arr)
    
    longest = 0
    
    ## iterate over the array
    for e in arr:
        parent = e - 1
        ## start of band
        if parent not in unordered_set:
            ## start of band (start chaining)
            child = e + 1
            cnt = 1
            while child in unordered_set:
                cnt += 1
                child += 1
                
            longest = max(cnt, longest)
            
    return longest

# arr = [1, 9, 3, 0, 18, 5, 2, 4, 10, 7, 12, 6]
# print(longest_band(arr))      


## Rain water trapping
def rain_water(height):
    n = len(height)
    if n <= 2:
        return 0
    
    left = [0] * n
    right = [0] * n
    max_left = -999999
    max_right = -999999
    
    for i in range(n):
        max_left = max(max_left, height[i])
        left[i] = max_left
    
    for i in range(n-1, -1, -1):
        max_right = max(max_right, height[i])
        right[i] = max_right
    
    max_area = 0
    for i in range(n):
        max_area += (min(left[i], right[i]) - height[i])
    
    return max_area

# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# area = rain_water(arr)
# print(area)


## Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in 
## non-decreasing order, then the whole array will be sorted in non-decreasing order.
def subarray_sort(nums):
    def out_of_order(nums, n, i):
        if i == 0:
            return nums[i] > nums[i+1]
        
        if i == n - 1:
            return nums[i] < nums[i-1]
        
        return nums[i] > nums[i+1] or nums[i] < nums[i-1]
    
    n = len(nums)
    if n <= 1:
        return [-1, -1]
    
    smallest = math.inf
    largest = -math.inf
    
    for i in range(n):
        if out_of_order(nums, n, i):
            smallest = min(smallest, nums[i])
            largest = max(largest, nums[i])
    
    if smallest == math.inf:
        return [-1, -1]
    
    left = 0
    while smallest >= nums[left]:
        left += 1
    
    right = n - 1
    while largest <= nums[right]:
        right -= 1
    
    return [left, right]


# # nums = [2, 6, 4, 8, 10, 9, 15]
# nums = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11]
# # nums = [1, 2, 3, 4, 5]
# print(subarray_sort(nums))


## minimum swap required to sort the given array
def min_swap(nums):
    n = len(nums)
    
    ## store the current indices with elements (before sorting)
    ## (element, index)
    ap = [(nums[i], i) for i in range(n)]
    
    ## sorting 
    ap.sort()
    
    ## taking a visited array to keep track the all elements
    ## building the main logic
    visited = [False] * n
    ans = 0
    
    for i in range(n):
        ## old index of the element (before sorting)
        old_indx = ap[i][-1]
        ## if the element is already visited or the element is in right position
        if visited[i] or old_indx == i:
            continue
        
        ## visiting the element (index) at first time
        node = i
        cycle = 0
        
        while not visited[node]:
            visited[node] = True
            next_node = ap[node][-1]
            node = next_node
            cycle += 1
            
        ans += (cycle - 1)
    
    return ans

# nums = [2, 5, 3, 0, 6, 8, 1, 9, 4, 11, -1]
# print(min_swap(nums))


## find closet pairs
def find_closest_pair(arr, brr):
    arr.sort()
    brr.sort()
    
    closest_diff = float('inf')
    closest_pair = None
    
    i, j = 0, 0
    
    while i < len(arr) and j < len(brr):
        diff = abs(arr[i] - brr[j])
        
        if diff < closest_diff:
            closest_diff = diff
            closest_pair = (arr[i], brr[j])
        
        if arr[i] < brr[j]:
            i += 1
        else:
            j += 1
    
    return closest_pair

# arr = [23, 5, 10, 17, 30]
# brr = [26, 134, 135, 14, 19]
# print(find_closest_pair(arr, brr))


## array product
def product_except_self(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    
    product = [(e*f) for e, f in zip(left, right)]
    
    return product

# arr = [1, 2, 3, 4, 5]
# print(product_except_self(arr))



## busy life (variations of merge intervals)

def busy_life(activities):
    ## sort the activities wrt end time of the activity
    ## in increasing order
    activities.sort(key=lambda x: x[-1])
    
    possible_activities = [activities[0]]
    
    for curr in activities[1:]:
        ## the end time of the last possible activity must be less than 
        ## or equal to start time of the current activity
        if possible_activities[-1][-1] <= curr[0]:
            possible_activities.append(curr)
    
    return possible_activities


def activity_selection(activities):
    ## sort the activities wrt end time of the activity
    ## in increasing order
    activities.sort(key=lambda x: x[-1])
    
    ## initialize the max_activities with 1,
    ## because the first activity is always possible (i.e first activity is the one which takes the least time)
    max_activities = 1
    prev_end_time = activities[0][-1]
    
    for curr in activities[1:]:
        start_time, end_time = curr
        if prev_end_time <= start_time:
            max_activities += 1
            prev_end_time = end_time
    
    return max_activities
    

intervals = [(7, 9), (0, 10), (4, 5), (8, 9), (4, 10), (5, 7)]
print(activity_selection(intervals))