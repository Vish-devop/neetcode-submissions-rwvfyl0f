class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimized: Using a hashmap || # tc: o(N)
        seen={}
        for i,v in enumerate(nums): 
            comp=target-v
            if comp in seen: 
                return [seen[comp],i]
            seen[v]=i
        return None

        
        