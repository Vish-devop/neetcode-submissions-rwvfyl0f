class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False 
        s,t=s.lower(), t.lower() #normalizing the characters to lowercase
        seen_s, seen_t = {},{} # setting up the empty dictionary to store {key-value pairs} 
        for i in range(len(s)): 
            seen_s[s[i]]= 1+seen_s.get(s[i],0)
            seen_t[t[i]]= 1+seen_t.get(t[i],0)
        return seen_s==seen_t
        
        '''
        A01: Brute-force approach: Comparison of two strings
        TC: O(nlogn+mlogm) : because of sorting
        SC: O(n+m)

        Code -> 
        return sorted(s)==sorted(t)
        '''

