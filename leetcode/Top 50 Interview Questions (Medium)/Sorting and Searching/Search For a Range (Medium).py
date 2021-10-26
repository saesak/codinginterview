class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        L = 0
        R = len(nums) - 1
        
        res = [-1, -1]
        
        while L <= R:
            mid = L + ((R-L) //2)
            
            if nums[mid] > target:
                R = mid - 1
            if nums[mid] < target:
                L = mid + 1
            if nums[mid] == target:
                res = [mid, mid]
                origmid = mid
                while mid > 0 and nums[mid - 1] == target:
                    res[0] = mid - 1
                    mid = mid - 1
                mid = origmid
                while mid < len(nums)-1 and nums[mid + 1] == target:
                    res[1] = mid + 1
                    mid = mid + 1
                mid = origmid
                break
        
        return res

#works but is very slow because of the middle part where it is O(n) not O(log(n)) like binary search should be

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            
            while l < r:
                m = (l + r) // 2 
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            
            return r if nums[r] == target else -1 #can return r or l since they end on same element of list
        
        def bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            
            while l < r:
                m = ((l + r) // 2) + 1
                if nums[m] > target:
                    r = m - 1 
                else:
                    l = m
            return l if nums[l] == target else - 1
        
        
        return [bisect_left(nums, target), bisect_right(nums, target)]

'''
better version, actually o log (n)
'''