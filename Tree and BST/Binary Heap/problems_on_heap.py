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

nums = [5, 15, 10, 20, 8, 25, 18]
k_largest = kLargest(nums, 3)
print(k_largest)