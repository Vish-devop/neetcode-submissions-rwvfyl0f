class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # first edge case every time we would check: if len() of both string are unequal they can't be anagram. 
        if len(s)!=len(t): return False 
        # normalizing the characters to lowercase
        s,t = s.lower(), t.lower()

        countS, countT= {},{}
        for i in range(len(s)): 
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)

        return countS==countT
        

        '''
        A01: Brute-force approach: Comparison of two strings
        TC: O(nlogn+mlogm) : because of sorting
        SC: O(n+m)

        Code -> 
        return sorted(s)==sorted(t)
        '''

