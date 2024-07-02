import functools

## QUICK SORT:
def partition(arr, s, e):
    ## Choose the last element as the pivot
    pivot = arr[e]
    ## Index of the smaller element
    i = s - 1
    
    for j in range(s, e):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    ## place the pivot element at it's correct position
    arr[i+1], arr[e] = arr[e], arr[i+1]
    
    return i+1
    

def quick_sort_solver(arr, s, e):
    ## base case
    if s >= e:
        return 
    
    ## get the partition index
    p = partition(arr, s, e)
    
    quick_sort_solver(arr, s, p-1)
    quick_sort_solver(arr, p+1, e)
    
    return

def quick_sort(arr):
    n = len(arr)
    quick_sort_solver(arr, 0, n-1)
    
    return

# arr = [10, 5, 2, 0, 7, 6, 4]
# quick_sort(arr)
# print(arr)
##---------------------------------------------------------------------------------------------------
## QUICK SELECT:
def quick_select_solver(arr, s, e, k):
    ## get the partitioning index
    p = partition(arr, s, e)
    
    if p == k:
        return arr[p]
    
    elif p < k:
        return quick_select_solver(arr, p+1, e, k)
    
    else:
        return quick_select_solver(arr, s, p-1, k)
    
    
def quick_select(arr, k):
    n = len(arr)
    
    ## if k outside of the array
    if k >= n or k < 0:
        return -1
    
    return quick_select_solver(arr, 0, n-1, k)

# k = int(input("Enter the value of k:"))
# # arr = [10, 5, 2, 0, 7, 6, 4]
# arr = [10]
# kth_smallest = quick_select(arr, k)
# print(kth_smallest)
##----------------------------------------------------------------------------------------------------
## Median of a given array using Quickselect Algorithm
def quick_select_median(arr, s, e, median_indx):
    if s == e:
        return arr[s]
    
    ## get the partition index
    p = partition(arr, s, e)
    
    if p == median_indx:
        return arr[median_indx]
    
    elif p > median_indx:
        return quick_select_median(arr, s, p-1, median_indx)
    
    else:
        return quick_select_median(arr, p+1, e, median_indx)
    

def get_median(arr):
    n = len(arr)
    median_indx = n//2
    
    ## use quick select to find element at median index
    median = float(quick_select_median(arr, 0, n-1, median_indx))
    
    ## if n is even
    if n % 2 == 0:
        median_indx -= 1
        median += float(quick_select_median(arr, 0, n-1, median_indx))
        median /= 2.0
    
    return median


# # arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# arr = [10, 5, 2, 0, 7, 6, 3, 4]
# arr = [2, 1, 0]
# median = get_median(arr)
# print(median)
##-----------------------------------------------------------------------------------------------------
## Merge Sort:
def merge(arr, arr1, arr2):
    i, j, k = 0, 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr[k] = arr2[j]
            k += 1
            j += 1
    
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    
    while j < len(arr2):
        arr[k] = arr2[j]
        k += 1
        j += 1
    
    return

def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return
    
    mid = len(arr) // 2
    
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    
    merge_sort(arr1)
    merge_sort(arr2)
    
    merge(arr, arr1, arr2)
    
    return

# # arr = [10, 5, 2, 0, 7, 6, 3, 4]
# arr = ['a', 'b', 'aba', 'aac', 'ac', 'wx', 'b', 'c', 'xyz']
# # merge_sort(arr)
# # print(arr)

##----------------------------------------------------------------------------------------------------------
## Smallest String: given the list of strings output the lexicographically smallest concatenation -
def merge_process(arr, arr1, arr2):
    i, j, k = 0, 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if (arr1[i] + arr2[j]) < (arr2[j] + arr1[i]):
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        
        k += 1
    
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1
    
    return


def smallest_string(lst):
    if len(lst) == 1 or len(lst) == 0:
        return
    
    mid = len(lst) // 2
    
    lst1 = lst[:mid]
    lst2 = lst[mid:]
    
    smallest_string(lst1)
    smallest_string(lst2)
    
    merge_process(lst, lst1, lst2)
    
    return

# lst = ['a', 'ab', 'aba']
# smallest_string(lst)
# print(lst)

# arr = ['c', 'cb', 'cba']
# smallest_string(arr)
# print(arr)

# a = ['a', 'b', 'aba', 'aac', 'ac', 'wx', 'b', 'c', 'xyz']
# smallest_string(a)
# print(a)

## the given code below will solve the same (Smallest String)
## using in-built sort 

# def compare(x, y):
#     return (x + y) < (y + x)

# lst = ['a', 'ab', 'aba']
# arr = ['c', 'cb', 'cba']

# arr.sort(key=functools.cmp_to_key(compare))
# lst.sort(key=functools.cmp_to_key(compare))

# print(lst)
# print(arr)
##---------------------------------------------------------------------------------------------------
## Sparse Search: given a sorted array of strings that is interspersed with empty strings,
## write a fn to find the index of a given word in the array

def sparse_search(arr: list, key: str):
    n = len(arr)
    s = 0
    e = n - 1

    while s <= e:
        mid = (s + e) // 2
        
        mid_left = mid - 1
        mid_right = mid + 1

        # Handle empty strings
        if arr[mid] == '':

            while True:
                if mid_left < s and mid_right > e:
                    return -1

                if mid_left >= s and arr[mid_left] != '':
                    mid = mid_left
                    break

                if mid_right <= e and arr[mid_right] != '':
                    mid = mid_right
                    break

                mid_left -= 1
                mid_right += 1

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            e = mid - 1

        else:
            s = mid + 1

    return -1

lst = ['ai', '', '', 'bat', '', '', 'car', 'cat', '', '', '', 'dog', '']
key = 'car'
indx = sparse_search(lst, key)
print(indx)