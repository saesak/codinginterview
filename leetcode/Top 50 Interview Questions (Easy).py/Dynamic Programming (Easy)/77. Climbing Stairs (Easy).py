class Solution:
    def climbStairs(self, n: int) -> int:
        
        s_dict = dict()
        
        def recurse(n):
            
            if n in s_dict:
                return s_dict[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            one = recurse(n-1)
            two = recurse(n-2)
            
            s_dict[n-1] = one
            s_dict[n-2] = two
            
            return one + two
        
        return recurse(n)