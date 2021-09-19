'''
https://leetcode.com/problems/bricks-falling-when-hit/

'''

'''
Initial intuitions --> iterate through entire thing every time something
is removed and check for the values to see if connected and erase if needed.

Thought that for checking, recursion might be a good idea but had never seen
it before so I was like, no way jose. Turns out you can do dfs for these
grids as well!!!! Did not think of it that way cause I only used them on 
Trees and graphs!
'''

'''
original solution:
https://leetcode.com/problems/bricks-falling-when-hit/discuss/119829/Python-Solution-by-reversely-adding-hits-bricks-back
more intuitive explanation in javascript:
https://leetcode.com/problems/bricks-falling-when-hit/discuss/450482/From-bad(general-intuition)-to-good(-reversely-adding-bricks)
'''
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if not(0<=i<m and 0<=j<n) or grid[i][j] !=1:
                return 0 #base case is it returns if it hits a non brick or goes out of bounds
            ret = 1 #since if it passed the above conditions, it means that it is itself a brick
            grid[i][j] = 2 #mark if it is a non falling brick
            
            w, a, s, d = 0, 0, 0, 0 #need to check all directions
            
            w = dfs(i-1, j) + w
            a = dfs(i, j-1) + a
            s = dfs(i+1, j) + s
            d = dfs(i, j+1) + d
            
            ret = ret + w + a + s + d #sum all of the non falling bricks collected
            #or just all the bricks connected to the brick you specified
            return ret 
        
        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            if i == 0: #if ceiling then is a non falling brick
                return True
            #if within boundaries or there are non falling marked bricks next to it (will equal 2 due to dfs)
            if any([0<=x<m and 0<=y<n and grid[x][y]==2 for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]]):
                return True
            return False #if nothing 
        
        # Mark whether there is a brick at the each hit
        # Result will be that it will be -1 if no brick was there
        # 0 if there was a brick there
        for i, j in hits:
            grid[i][j] -= 1
        
        # Get grid after all hits
        for i in range(n):
            dfs(0, i)
        
        
        # Reversely add the block of each hits and get count of newly add brick
        ret = [0]*len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1 #revert the -1 you did earlier
            if grid[i][j]==1 and is_connected(i, j): #if it is a brick and is connected to non falling brick
            #we can use the is_connected function here because earlier
            #we used dfs to mark all the bricks connected to non falling bricks 
            #after all the hits 
            #and now dfs will return all the ones that are connected
            #unless it was marked as non falling earlier when we first used dfs
            #then it will ignore that using grid[i][j] != 1 since non falling is equal to 2 
                ret[k] = dfs(i, j)-1
            
        return ret