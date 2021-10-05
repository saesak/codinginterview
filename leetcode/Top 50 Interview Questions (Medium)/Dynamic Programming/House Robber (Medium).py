class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob_d = dict()
        
        def recurse(nums):
            print(nums)
            n = len(nums)
            if tuple(nums) in rob_d:
                return rob_d[tuple(nums)]
            if n == 0:
                return 0
            
            
            tot = 0
            
            for i in range(n):
                if i == n-1:
                    tot = max(nums[i] + recurse(nums[i:n-1]), tot) #length 0 array
                    rob_d[tuple(nums)] = tot
                elif i == 0:
                    tot = max(nums[i] + recurse(nums[i+2:n+1]), tot) #accounts for beginning of array
                    rob_d[tuple(nums)] = tot
                elif i > 0 and i < n:
                    tot = max(nums[i] + recurse(nums[0:i-1] + nums[i+2:]), tot) #accounts for middle of array
                    rob_d[tuple(nums)] = tot
                    
            return tot 
        
        return recurse(nums)
            
'''initial approach is above
correct but way too slow because it memoizes by elements in array which is
logical, but too inefficient

instead, memoize on length of array as done below also another problem is using for loop
to iterate is inefficient because you'll inevitably do multiple options twice
and even if you memoize it'll end up being too inefficient 
'''

