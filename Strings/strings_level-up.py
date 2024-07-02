import re

# n: int = 5
# sarr: list = []
# temp: str

# while n:
#     temp = input()
#     sarr.append(temp)
#     n -= 1

# for e in sarr:
#     print(e, end=',')    


# s: str = """A unicode string is a different type of object from a byte string but various libraries such as regular expressions 
#             work correctly if passed either type of string."""
           
# ip = input()

# indx = s.find(ip)

# if indx == -1:
#     print('string not found!')
# else:
#     print(indx)

# if indx != -1:
#     print(f"The first occ of {ip} is in {indx}")

# indx = s.find(ip, indx+1)

# if indx != -1:
#     print(f"The second occ of {ip} is in {indx}")

# indx = s.find(ip, indx+1)

# if indx != -1:
#     print(f"The third occ of {ip} is in {indx}")


## find all occurance of a word in given string

def find_all_occurrences(find_word, input_string):
    occ = []
    indx = input_string.find(find_word, 0)
    
    while indx != -1:
        occ.append(indx)
        indx = input_string.find(find_word, indx+1)
    
    return occ

# s: str = """A unicode string is a different type of object from a byte string but various libraries such as 
#             regular expressions work correctly if passed either type of string."""
            
# word = 'string'

# bigString: str = "I liked the movie, acting in movie was great!"
# smallString: str = "movie" 
# print(find_all_occurrences(smallString, bigString))


## Replace empty spaces with %20 
def space_20(ip_string: str):
    ## 1. calculate spaces
    spaces = 0
    for i in range(len(ip_string)):
        if ip_string[i] == ' ':
            spaces += 1
    
    idx = len(ip_string) + (2*spaces)
    # ip_string += '\0'
    
    for i in range(len(ip_string)-1, -1, -1):
        if ip_string[i] == ' ':
            ip_string = ip_string[:idx-3] + '%20' + ip_string[idx:]
            idx -= 3
        else:
            ip_string = ip_string[:idx-1] + ip_string[i] + ip_string[idx:]
            idx -= 1
    
    return ip_string

# ip_string = "hello world,  how are you?"
# print(id(ip_string))
# op = space_20(ip_string)
# print(op)
# print(id(op))


## string tokenization
# ip_str = input()
# tokens = ip_str.split(' ')
# print(tokens)

def check_subsequence(ip_string: str, small_string):
    ## two pointer approach
    
    if small_string == " ":
        return True
    
    i = len(ip_string)-1
    j = len(small_string)-1
    
    while i >= 0 and j >= 0:
  
        if ip_string[i] == small_string[j]:
            i -= 1
            j -= 1
        else:
            i -= 1
            
    return True if j == -1 else False

# ip_string = "coding minutes"
# small_string = "coding minutes is aswm"
# print(check_subsequence(ip_string, small_string))

def get_subseqs(ip_string, subset, i, n, res):
    if i == n:
        res.append(subset)
        return
    
    ## inclusive
    get_subseqs(ip_string, subset + ip_string[i], i+1, n, res)
    
    ## exclusive
    get_subseqs(ip_string, subset, i+1, n, res)
    
    return

# def sort_compare(s1: str, s2: str):
#     if len(s1) == len(s2):
#         return s1 < s2
#     return len(s1) < len(s2)

def sorted_subsequences(ip_string: str):
    n = len(ip_string)
    all_subsets = []
    get_subseqs(ip_string, '', 0, n, all_subsets)
    
    # Sort the list by length and lexicographically
    all_subsets.sort(key=lambda x: (len(x), x))
    
    return all_subsets

s = 'abcd'
print(sorted_subsequences(s))