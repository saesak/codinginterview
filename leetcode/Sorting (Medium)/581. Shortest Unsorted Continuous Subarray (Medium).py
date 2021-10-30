'''
sorting solution which is nlogn because sorting is nlogn and this is greater
than n so when we consider nlogn + n --> only nlogn is left so 
time complexity is nlogn

space complexity is n 
'''

'''
REVISIT
better solutions available that do it in O(n) time
'''

'''
explanation --> sort array then compare with initial array
from front and back to see how many need to be changed in order to
work. 
'''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        sort_nums = sorted(nums)
        
        left = 0
        
        for i in range(n):
            if sort_nums[i] != nums[i]:
                break
            if sort_nums[i] == nums[i]:
                left += 1
        
        right = 0
        
        for j in range(n-1, -1, -1):
            if sort_nums[j] != nums[j]:
                break
            if sort_nums[j] == nums[j]:
                right += 1
        
        if left == n or right == n:
            return 0
        
        return n - left - right