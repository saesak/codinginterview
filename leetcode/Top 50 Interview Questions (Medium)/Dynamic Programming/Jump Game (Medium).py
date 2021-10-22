
'''
Bad solution that doesn't work because time limit exceeded

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        nums_dict = dict()
        
        def recurse(nums, ind):
            
            if ind > len(nums) - 1:
                return False
                
            jump = nums[ind]
            
            if ind in nums_dict:
                return nums_dict[ind]
            if ind == len(nums) - 1:
                nums_dict[ind] = True
                return True
            if jump == 0 or ind > len(nums) - 1:
                nums_dict[ind] = False
                return False
            
            
            tf = False
            
            
            for i in range(1, jump+1):
                tf = recurse(nums, ind + i) or tf
            
            return tf
        
        return recurse(nums, 0)


'''
actual solution that works

O(n) time O(1) memory

'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxPos = 0
        i = 0
        while i <= maxPos: #this is what keeps it from just mindlessly continuing on, takes care of cases like [3,2,1,0,4] where there's a zero 
            maxPos = max(maxPos, i + nums[i])
            print(i, maxPos)
            if maxPos >= n - 1: return True
            i += 1
        
        return False
