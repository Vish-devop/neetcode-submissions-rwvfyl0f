class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using the approach of hashmaps and dictionary 
        seen=set() 
        for num in nums: 
            if num in seen: 
                return True 
            seen.add(num)
        return False 

