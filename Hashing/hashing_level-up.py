import collections

def common_elements(v1: list, v2: list):
    s1 = set(v1)
    s2 = set(v2)
    
    return s1.intersection(s2)

# v1 = [1, 45, 54, 71, 76, 12]
# v2 = [1, 7, 5, 4, 6, 12]
# res = common_elements(v1, v2)
# print(res)
##---------------------------------------------------------------------------------------------------
def first_repeating_element(string: str):
    s = set()
    
    for e in string:
        if e in s:
            return e
        else:
            s.add(e)
    
    return None

# s = 'purnima'
# res = first_repeating_element(s)
# print(res)
##---------------------------------------------------------------------------------------------------------
## Triplets in GP:
def cnt_triplets_gp(nums: list, r: int):
    n = len(nums)
    
    ## initializing the left and right frequency map
    freq_left = {}
    for num in nums:
        freq_left[num] = 0
        
    freq_right = collections.Counter(nums)
    
    # freq_right = {}
    # for num in nums:
    #     if num in freq_right:
    #         freq_right[num] += 1
    #     else:
    #         freq_right[num] = 1
    
    ## sliding hashing (algo)
    cnt = 0
    for i in range(n):
        
        freq_right[nums[i]] -= 1
        
        if nums[i] % r == 0:
            ## nums[i]/r, nums[i], nums[i] * r => a, b, c
            a = nums[i] // r
            b = nums[i]
            c = nums[i] * r
            
            cnt += freq_left.get(a, 0) * freq_right.get(c, 0)
            
        freq_left[nums[i]] += 1
    
    return cnt

# arr = [64, 4, 4, 16, 64, 4, 64, 8, 4, 16, 64, 4]
# # arr = [1, 16, 4, 16, 64, 16]
# r = 2
# cnt = cnt_triplets_gp(arr, r)
# print(cnt)
##---------------------------------------------------------------------------------------------------------------
## Count Rectangles: Given n pairs of point on cartesian plane return number of rectangles possible with sides 
## parallel to X and Y axes. 
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def cnt_rectangles(n: int, points: list[tuple]):
    ## insert all the points to lookup (set())
    lookup = set(points)
    cnt = 0

    ## brut force two points + lookup other two points
    for i in range(0, n-1):
        for j in range(i+1, n):
            p1, p2 = points[i], points[j]

            ## small check to make
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue

            ## p3, p4
            p3 = (p1[0], p2[1])
            p4 = (p2[0], p1[1])

            ## lookup in the lookup table
            if p3 in lookup and p4 in lookup:
                cnt += 1

    return cnt // 2

## taking input from user
# n = int(input())
# points = []

# for _ in range(n):
#     x, y = map(int, input().split())
#     point = Point(x, y)
#     points.append((point.x, point.y))

# print(points)
# cnt = cnt_rectangles(n, points)
# print(cnt)
##--------------------------------------------------------------------------------------------------------
## Count Right Angle Triangles: Given n cartesian points in a 2D plane, find the number of right angle
## triangles such that base and perpendicular is parallel to the X and Y axes.
def cnt_triangles(n: int, points: list[tuple]):
    ## initializing the maps -> <x, cnt_x> <y, cnt_y>
    map_x = {}
    map_y = {}

    for x, y in points:
        ## inserting into map_x
        if x in map_x:
            map_x[x] += 1
        else:
            map_x[x] = 1
        
        ## inserting into map_y
        if y in map_y:
            map_y[y] += 1
        else:
            map_y[y] = 1

    cnt = 0
    for x, y in points:
        cnt_x = map_x[x]
        cnt_y = map_y[y]

        cnt += (cnt_x-1) * (cnt_y-1)
    
    return cnt

## taking input from user
# n = int(input())
# points = []

# for _ in range(n):
#     x, y = map(int, input().split())
#     point = Point(x, y)
#     points.append((point.x, point.y))

# print(points)
# cnt = cnt_triangles(n, points)
# print(cnt)
############################################################################################################
## Anagrams in substrings: Given a string find the number of pairs of substrings of the string that are
## anagrams of each other
def cnt_anagrams_in_substrings(string: str):
    pass