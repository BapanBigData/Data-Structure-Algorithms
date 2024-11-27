# 88. Merge Sorted Array

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums3 = nums1[:m]
    i, j, k = 0, 0, 0

    while (i < m) and (j < n):
        if nums3[i] <= nums2[j]:
            nums1[k] = nums3[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        
        k += 1
    
    while (i < m):
        nums1[k] = nums3[i]
        i += 1
        k += 1
    
    while ( j < n):
        nums1[k] = nums2[j]
        j += 1
        k += 1
    
    return 


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)

