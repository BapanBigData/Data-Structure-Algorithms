## Frequency Count: 
def first_occ(arr, key):
    s = 0
    e = len(arr)-1
    
    ans = -1
    
    while s <= e:
        mid = (s+e) // 2
        
        if arr[mid] == key:
            ans = mid
            e = mid - 1
        
        elif arr[mid] > key:
            e = mid - 1
        
        else:
            s = mid + 1
    
    return ans         

def last_occ(arr, key):
    s = 0
    e = len(arr)-1
    
    ans = -1
    
    while s <= e:
        mid = (s+e) // 2
        
        if arr[mid] == key:
            ans = mid
            s = mid + 1
        
        elif arr[mid] > key:
            e = mid - 1
        
        else:
            s = mid + 1
    
    return ans       

def freq_count(arr: list, key: int):
    fo = first_occ(arr, key)
    lo = last_occ(arr, key)
    
    return -1 if fo == -1 or lo == -1 else lo - fo + 1

# arr = [0, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 10]
# key = 11
# res = freq_count(arr, key)
# print(res)
##-------------------------------------------------------------------------------------
## Rotated Search:
def rotated_search(arr, key):
    n = len(arr)
    
    s = 0
    e = n-1
    
    while s <= e:
        mid = (s + e) // 2
        
        if arr[mid] == key:
            return mid
        
        ## mid is in the line 1
        if arr[s] <= arr[mid]:
            if arr[s] <= key < arr[mid]:
                ## search in the left of line-1
                e = mid -1
            else:
                ## search in the rest of the array
                s = mid + 1
        
        ## mid is in the line 2
        elif arr[mid] <= arr[e]:
            if arr[mid] < key <= arr[e]:
                ## search in the right of line-2
                s = mid + 1
            else:
                ## search in the rest of the array
                e = mid - 1
    
    return -1

# # arr = [7, 9, 10, 1, 2, 3, 4, 5, 6]
# arr = [1, 3, 5]
# key = 5
# indx = rotated_search(arr, key)
# print(indx)
##--------------------------------------------------------------------------------------------------------
## Finding Roots:
def find_square_root(n: int, p: int):
    ## integer part (Binary Search)
    ## search space 0 to n
    s = 0
    e = n
    ans = 0.0
    while s <= e:
        mid = (s + e) // 2
        
        if (mid*mid) == n:
            return mid/1.0
        
        elif (mid*mid) > n:
            ## go left
            e = mid - 1
            
        else:
            ans = mid
            ## go right
            s = mid + 1
    
    ## Linear Search at each decimal place ... upto p places
    inc = 0.1
    for _ in range(p):
        while (ans*ans) <= n:
            ans += inc
        
        ## take one step back
        ans -= inc
        
        ## going to next precision place (next decimal place)
        inc /= 10.0
    
    return round(ans, p)

# n = 729
# p = 12
# res = find_square_root(n, p)
# print(res)
##-------------------------------------------------------------------------------------------------------
## Angry Birds:
def can_place_birds(n: int, bird: int, nests: list, sep: int):
    
    birds = 1
    location = nests[0]
    
    for i in range(1, n):
        curr_location = nests[i]
        if (curr_location - location) >= sep:
            birds += 1
            location = curr_location
            
            if birds == bird:
                return True
            
    return False


def angry_birds(bird: int, nests: list):
    n = len(nests)
    ## sort the nests
    nests.sort()
    
    ## Binary Search to find the largest minimum distance
    ## initializing the search space
    s = 0
    e = nests[n-1] - nests[0]
    ans = -1
    
    while s <= e:
        mid = (s + e) // 2
        can_place = can_place_birds(n, bird, nests, mid)
        if can_place:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    
    return ans

# nests = [1, 2, 4, 8, 9, 12, 14, 15, 19, 23]
# bird = 7
# res = angry_birds(bird, nests)
# print(res)
##-------------------------------------------------------------------------------------------------------
## ceiling of a number
## arr = [2, 3, 5, 9, 14, 16, 18], target = 15 ---> ceiling is 16
def floor_ceil(arr: list, num, is_ceil):
    n = len(arr)
    s = 0
    e = n-1
    ans = -1
    while s <= e:
        mid = (s + e) // 2
        
        if is_ceil:
            if arr[mid] == num:
                return arr[mid]
            
            elif arr[mid] > num:
                ans = arr[mid]
                e = mid - 1
            
            else:
                s = mid + 1
        else:
            if arr[mid] == num:
                return arr[mid]
            
            elif arr[mid] < num:
                ans = arr[mid]
                s = mid + 1
            
            else:
                e = mid - 1
    
    return ans

# arr = [15, 17, 26, 134, 135]
# target = 17
# ceil = floor_ceil(arr, target, True)
# print(ceil)  
##-----------------------------------------------------------------------------------------------------
## minimum pair: given two non-empty array find the pair of number (one from each array) whose absolute
## difference is minimum
import math
import bisect

def get_ceiling(lst, num, n):
    s = 0
    e = n-1
    indx = -1
    while s <= e:
        mid = (s + e) // 2
        if lst[mid] == num:
            return mid
        
        elif lst[mid] > num:
            indx = mid
            e = mid - 1
        
        else:
            s = mid + 1
    
    return indx
    
def min_pair(arr: list, brr: list):
    m = len(brr)
    ## sort the second array (we can sort any of the array)
    brr.sort()
    
    diff = math.inf
    p1 = None
    p2 = None
    
    for e in arr:
        # ceil_indx = bisect.bisect_left(brr, e)
        ceil_indx = get_ceiling(brr, e, m)
        
        ## check the indx (ceil_indx - 1), which will be smaller than e
        if (ceil_indx - 1) >= 1 and (e - brr[ceil_indx-1]) <= diff:
            diff = e - brr[ceil_indx-1]
            p1 = e
            p2 = brr[ceil_indx-1]
        
        ## now, check the ceil_indx itself
        if ceil_indx != m and (brr[ceil_indx] - e) <= diff:
            diff = brr[ceil_indx] - e 
            p1 = e
            p2 = brr[ceil_indx]
    
    return [p1, p2]

# arr = [-1, 5, 10, 20, 3]
# brr = [26, 134, 135, 15, 17]
# pair = min_pair(arr, brr)
# print(pair)
##---------------------------------------------------------------------------------------------------
## Game Of Greedy:
def divide_among_k(k, coins, n, min_coins) -> bool:
    
    partitions = 0
    curr_coins = 0
    
    for i in range(n):
        if (curr_coins + coins[i]) >= min_coins:
            partitions += 1
            curr_coins = 0
        else:
            curr_coins += coins[i]
    
    return partitions >= k

def maximize_min_partition(k: int, coins: list) -> int:
    n = len(coins)
    ans = -1
    
    ## initializing the search space
    s = 0
    e = sum(coins)
    
    while s <= e:
        mid = (s + e) // 2
        is_possible = divide_among_k(k, coins, n, mid)
        
        if is_possible:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    
    return ans

coins = [10, 22, 40, 45]
k = 3
res = maximize_min_partition(k, coins)
print(res)