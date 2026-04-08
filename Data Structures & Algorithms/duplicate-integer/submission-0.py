class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashmap
        seen={}
        for i in nums: 
            if i not in seen: 
                # adding the element into hashmap with initial count of 1
                seen[i]=1
            else: 
                # INCREASING THE FREQUENCY, COUNT OF array element.
                seen[i] = seen[i]+1
        
        for key,value in seen.items():
            if value>1: 
                return True
        return False 
