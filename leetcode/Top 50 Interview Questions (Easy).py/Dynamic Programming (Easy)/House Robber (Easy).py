class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob_d = dict()
        
        def recurse(nums):
            n = len(nums)
            if n in rob_d:
                return rob_d[n]
            if n == 0:
                return 0
            if n == 1:
                return max(nums)
            if n == 2:
                return max(nums)
            
            option1 = nums[0]
            option1 += recurse(nums[2:])
            
            option2 = nums[1]
            option2 += recurse(nums[3:])
            
            rob_d[len(nums)] = max(option1, option2)
            
            return max(option1, option2) 
        
        return recurse(nums)

'''
KINDA HARD RETRY

'''