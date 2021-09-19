'''
Brute force O(n^3) time
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #use sliding window
        #but sliding window doesn't capture all the possibillities
        final = []
        n = len(nums)
        
        if n < 3:
            return []
        
        for i in range(n):
            if i < n - 1 - 1: #fits this way
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        if i != j and i != k and j != k:
                            if nums[i] + nums[j] + nums[k] == 0:
                                tmp = sorted([nums[i], nums[j], nums[k]])
                                if tmp not in final:
                                    final.append(tmp)
                                    
                                    
        return final