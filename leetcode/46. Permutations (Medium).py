class Solution:
    
    def backtrack(self, start, end, nums, final):
        if start == end:
            final.append(nums[:])
        else:
            for i in range(start, end):
                nums[i], nums[start] = nums[start], nums[i]
                self.backtrack(start + 1, end, nums, final)
                nums[i], nums[start] = nums[start], nums[i]
                
    def permute(self, nums):
        n = len(nums)
        final = []
        self.backtrack(0, n, nums, final)
        
        
        return final

'''
swap nums, backtrack, then swap nums so they're back to normal

we use nums[:] to access the modified version of nums. nums alone will give you
the original array. 



'''