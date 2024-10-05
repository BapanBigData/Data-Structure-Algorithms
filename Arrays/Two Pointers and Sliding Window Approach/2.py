
# Longest substring with atmost k distinct characters

def longest_k_sub_string(s: str, k: int) -> int:
    n = len(s)
    
    def solver1():
        l, r = 0, 0
        mpp = {}
        max_lenn = 0
        
        while (r < n):
            
            if s[r] in mpp:
                mpp[s[r]] += 1
            else:
                mpp[s[r]] = 1
            
            while (len(mpp) > k):
                mpp[s[l]] -= 1
                
                if (mpp[s[l]] == 0):
                    del mpp[s[l]]
                    
                l += 1
            
            if (len(mpp) <= k):
                max_lenn = max(max_lenn, r-l+1)
            
            r += 1
        
        return max_lenn
    
    
    def optimal():
        l, r = 0, 0
        mpp = {}
        max_lenn = 0
        
        while (r < n):
            
            if s[r] in mpp:
                mpp[s[r]] += 1
            else:
                mpp[s[r]] = 1
            
            if (len(mpp) > k):
                mpp[s[l]] -= 1
                
                if (mpp[s[l]] == 0):
                    del mpp[s[l]]
                    
                l += 1
            
            if (len(mpp) <= k):
                max_lenn = max(max_lenn, r-l+1)
            
            r += 1
        
        return max_lenn
    
    return optimal()


s = "aaabbccd"
res = longest_k_sub_string(s, k=2)
print(res)


