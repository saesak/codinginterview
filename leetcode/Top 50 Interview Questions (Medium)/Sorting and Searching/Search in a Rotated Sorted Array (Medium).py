class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_mod(arr, tar):
            r = len(arr) - 1
            l = 0
            
            while l <= r:
                m = (r+l) // 2
                
                if arr[m] == target:
                    return m
                
                if arr[l] <= arr[m]:
                    if arr[l] <= target <= arr[m]:
                        r = m-1
                    else:
                        l = m+1
                else:
                    if arr[m] <= target <= arr[r]:
                        l = m+1
                    else:
                        r = m-1
            
            return -1
        
        if target in nums:
            return binary_mod(nums, target)
        else:
            return -1

'''
QUICK REVISIT
'''