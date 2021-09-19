'''
WRONG INITIAL SOLUTION
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr = 0
        ans = 0
        
        n = len(height)
        
        L = 0
        R = n - 1
        
        while(L < R):
            y1 = height[L]
            y2 = height[R]
            y = 0
            if y1 >= y2:
                y = y2
            else:
                y = y1
            
            curr = (R-L) * y
            ans = max(curr, ans)
            
            if y1 > y2:
                R -= 1
            if y1 < y2:
                L += 1
            else:
                R -= 1
            
        return ans


    '''
    CORRECT SOLN FOUND IN DISCUSSION
    https://leetcode.com/problems/container-with-most-water/discuss/6131/O(N)-7-line-Python-solution-72ms

    explanation:
    https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
    '''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr = 0
        ans = 0
        
        n = len(height)
        
        L = 0
        R = n - 1
        
        for width in range(0, n):
            y1 = height[L]
            y2 = height[R]
            
            if y1 < y2:
                ans = max(ans, y1 * (R-L))
                L = L + 1
            else:
                ans = max(ans, y2 * (R-L))
                R = R - 1
            
            
        return ans

'''
Time complexity is O(n) since we only loop through the entire thing once

But the difference between my soln and their soln was kind of minor. I used a while loop that
aimed for a O(n/2) time and they used a for loop through the entire loop. 

The ideas behind both were similar --> We both knew that brute force caused time out so needed
the optimal O(n) soln where if we know that the water is at certain height limited by the lower
bar then the possibillity for a bigger area is only opened up if we move the lower bar forward
(in whatever direction is forward for it). 

So why use a for loop instead of a while loop? I would assume that the for loop
covers all the possibillities while while loop only covers half?

I'll have to keep that in mind when i see stuff like this in the future.
Rather than going straight for the O(n/2), go for O(n) first.
'''