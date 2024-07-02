import math

## Housing problem
## The below solution not always pass all the test cases
## Can be optimize the soln using sliding window approach
def housing_binary_search(plots: list, k: int):
    
    def binary_search(ps, si, ei, x):
        while si <= ei:
            mid = (si+ei) // 2
            
            if ps[mid] == x:
                return mid
            
            if ps[mid] < x:
                si = mid+1
            else:
                ei = mid-1
        
        return -1
    
    n = len(plots)
    
    ## initializing and building the prefix sum array
    ps = [0]*n
    ps[0] = plots[0]
    
    for i in range(1, n):
        ps[i] = ps[i-1] + plots[i]
    
    ## for every i find j such that ps[j] - ps[i] == k
    pairs = []
    
    for i in range(n):
        
        if i == 0:
            j = binary_search(ps, i+1, n-1, k+ps[i])
            
            if j != -1:
                pairs.append([i, j-1])
        
        else:
            j = binary_search(ps, i+1, n-1, k+ps[i])
            
            if j != -1:
                pairs.append([i+1, j])
    
    return pairs
 
 
## optimal and best soln
def housing_sliding_window(plots: list, k: int):
    n = len(plots)
    
    pairs = []
    
    ## initializing current sum, i and j variables
    cs = 0
    i, j = 0, 0
    
    while j < n:
        ## expand to right
        cs += plots[j]
        j += 1
        
        ## remove elements from the cs till cs > k and i < j
        while (cs > k) and (i < j):
            cs -= plots[i]
            i += 1
        
        ## check if at given point the current sum is equal to k
        if cs == k:
            pairs.append([i, j-1])
    
    return pairs


def smallest_window_housing(plots: list, k: int):
    n = len(plots)
    
    ## initializing the smallest window
    mn_window_size = math.inf
    si, ei = None, None
    
    cs = 0
    i, j = 0, 0
    
    while j < n:
        cs += plots[j]
        j += 1
        
        while (cs > k) and (i < j):
            cs -= plots[i]
            i += 1
        
        if cs == k:
            start, end  = i, j-1
            cw_size = end - start
            if cw_size < mn_window_size:
                si = start
                ei = end
                mn_window_size = cw_size
    
    return si, ei

# arr = [1, 3, 2, 1, 4, 1, 3, 2, 1, 1, 2]
# arr1 = [1, 3, 2, 1, 5]
# k = 8
# sw = housing_sliding_window(arr, k)
# print(sw)
# smallest_sw = smallest_window_housing(arr, k) 
# print(smallest_sw)

## HW: find the smallest window that contain the required sum
## also handle if the negative integers given in the array

##--------------------------------------------------------------------------------------------------------
## Unique Sub-string: largest sub-string with unique characters
def unique_substring(s: str):
    n = len(s)
    
    ## initializing the hashmap
    hash_mp = {}
    
    ## initializing the the window length, max window length, start window 
    window_len = 0
    max_window_len = 0
    start_window = None
    
    ## initializing first and last index of the window
    ## both are initialize by 0; 
    ## j is the expanding window variable (end of a window)
    ## i represents start of a window
    i = 0
    j = 0
    
    while j < n:
        ## get the current character
        curr_char = s[j]
        
        ## if curr_char is in the hashmap and it's indx >= start of the current window
        if hash_mp.get(curr_char) is not None and hash_mp.get(curr_char) >= i:
            i = hash_mp.get(curr_char) + 1
            window_len = j-i ## updated remaining window length excluding the current character
        
        ## update the last occurence of the current character
        hash_mp[curr_char] = j
        window_len += 1
        j += 1 
        
        ## update max window length at every step
        if window_len > max_window_len:
            max_window_len = window_len
            start_window = i
    
    ## building the substring from start window index to max window length
    substring = s[start_window:start_window + max_window_len]
    
    return substring

# s = 'abcaeba'
# s = 'prateekbhaiya'
s = 'abcdefgxyzw'
substring = unique_substring(s)
print(substring)