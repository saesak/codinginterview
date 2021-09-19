#Brute Force

class Solution:
    def trap(self, height: List[int]) -> int:
        #difference in heights is the way to go
        #look for sandwiches
        
        n = len(height)
        
        Lmax = 0
        Rmax = 0
        total = 0
        
        for i in range(n):
            if i > 0 and i < n-1:
                Lmax = 0 #need to reset each time so variables dont screw you
                Rmax = 0
                for left in range(0,i):
                    Lmax = max(Lmax, height[left])
                for right in range(i+1, n):
                    Rmax = max(Rmax, height[right])
                curr = min(Lmax, Rmax) - height[i]
                total += max(curr, 0)
            
        return total
    
#dynamic approach 

class Solution:
    def trap(self, height: List[int]) -> int:
        #difference in heights is the way to go
        #look for sandwiches
        
        n = len(height)
        
        Lmax = 0
        Rmax = 0
        total = 0

        for i in range(n):
            if i > 0 and i < n-1:
                Lmax = 0 #need to reset each time so variables dont screw you
                Rmax = 0
                for left in range(0,i):
                    Lmax = max(Lmax, height[left])
                for right in range(i+1, n):
                    Rmax = max(Rmax, height[right])
                curr = min(Lmax, Rmax) - height[i]
                total += max(curr, 0)
            
        return total
    
'''
For right, iterate once, save all
For left, continually update using current value as you move along
while looking at i = 0 value at beginning since you start looking at i = 1

Add all to 2 separate dictionaries / hashmaps 
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        #difference in heights is the way to go
        #look for sandwiches
        
        n = len(height)
        
        Lmax = 0
        Rmax = 0
        total = 0
        
        Rdict = dict()
        Ldict = dict()
        
        for i in range(n):
            if i > 0 and i < n-1:
                Lmax = 0 #need to reset each time so variables dont screw you
                Rmax = 0
                
                if len(Ldict) > 0:
                    Lmax = max(Lmax, Ldict[i-1])
                    Ldict[i] = max(Ldict[i-1], height[i])
                if len(Ldict) == 0:
                    Lmax = max(Lmax, height[i], height[i-1]) #to account for leftmost height height[i-1]
                    Ldict[i] = Lmax
                
                
                if len(Rdict) > 0:
                    Rmax = Rdict[i+1]
                if len(Rdict) == 0:    
                    #reverse because need max from right
                    for right in range(n-1, i, -1): #i+1 --> i + 1 - 1 = i to get to i+1th element
                        if right in Rdict:
                            Rmax = Rdict[right]
                            break #break since you already have the max value 
                        else:
                            Rmax = max(Rmax, height[right])
                            Rdict[right] = Rmax
                
                curr = min(Lmax, Rmax) - height[i]
                total += max(curr, 0)
                
        return total
    

'''
Could refactor code to make better by replacing Ldict with a variable so it takes up less space
and also could clean up the logic so we can do all the right iteration before
we get into the loop 
'''

'''
https://leetcode.com/problems/trapping-rain-water/solution/
Better solution is soln 4
currently we use O(n) time and space but soln 4 uses only O(n) time and O(1) space
'''