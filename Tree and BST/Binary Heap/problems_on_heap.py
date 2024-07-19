import heapq

## ** k largest elements **
## ** soln using min heap **
## ** Overall T.C:- O(k + (n-k) * log(k)) **
## ** T.C:- (k -> n-1) O(n + log(n)); (k -> 2) O(nlog(k)) => O(n)

def kLargest(nums: list[int], k: int) -> list[int]:
    pq = nums[:k]
    heapq.heapify(pq)
    
    for e in nums[k:]:
        if e > pq[0]:
            ## replace the root with given element and heapify 
            heapq.heapreplace(pq, e)
    
    return pq

############################################################################################

## ** soln using max heap **
## ** Overall T.C:- O(n + k * log(n))
## ** T.C:- (k -> n-1) O(n + nlog(n)); (k -> 2) O(n + log(n))

def k_largest(nums: list[int], k: int) -> list[int]:
    pq = [-num for num in nums]
    
    ## build max heap
    heapq.heapify(pq)
    res = []
    
    for _ in range(k):
        x = heapq.heappop(pq)
        res.append(-x)
    
    return res

# nums = [5, 15, 10, 20, 8, 25, 18]
# k_largest = kLargest(nums, 3)
# print(k_largest)
########################################################################################################################################
## ** k smallest elements **

def usingMinHeap(nums, k):
    res = []
    
    ## heapify
    heapq.heapify(nums)
    
    for _ in range(k):
        x = heapq.heappop(nums)
        res.append(x)
    
    return res

def usingMaxHeap(nums, k):
    nums = [-num for num in nums]
    
    pq = nums[:k]
    heapq.heapify(pq)
    
    for e in nums[k:]:
        if (e > pq[0]):
            heapq.heapreplace(pq, e)
    
    return [-i for i in pq]

## nums = [100, 140, 20, 130, 5, 70, 40, 12]; k = 3
## print(usingMaxHeap(nums, k))

#######################################################################################################################################
## ** K closest elements **
def naiveKClosest(nums, k, x):
    res = []
    for _ in range(k):
        mi = 0
        for i in range(1, len(nums)):
            if  abs(nums[i] - x) < abs(nums[mi] - x):
                mi = i
        res.append(nums[mi])
        nums.pop(mi)
    return res


def kClosest(nums: list[int], k: int, x: int):
    ## Max Heap
    n = len(nums)
    pairs = [(-abs(nums[i]-x), i) for i in range(n)]
    
    pq = pairs[:k]
    heapq.heapify(pq)
    
    for val, indx in pairs[k:]:
        if (val > pq[0][0]):
            heapq.heapreplace(pq, (val, indx))
    
    return [nums[indx] for _, indx in pq]

nums = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]; k = 4; x = 35
closest = kClosest(nums, k, x)
print(closest)



