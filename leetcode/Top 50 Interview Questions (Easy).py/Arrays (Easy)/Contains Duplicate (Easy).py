class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hi = dict()
        
        for ele in nums:
            if ele in hi:
                return True
            if ele not in hi:
                hi[ele] = True
        
        return False