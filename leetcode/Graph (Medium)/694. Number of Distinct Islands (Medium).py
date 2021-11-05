'''
Time --> O(M * N)
I didn't really "hash" per say but I solved it similarly to their third question. Instead of storing
directions though, I stored unique global coordinates based on distance from origin and I stored them not
in a set, but I stored them in a list. 

Space --> O(N * M)
'''

'''
explanation

classic dfs to just go through entire thing to find any islands,
while keeping visited updated with what island coords you visited to not
do more work than needed. 

You also keep unique list updated with lists containing lists of global coordinates
that you can refer to in order to filter out islands that are not 
distinct(same shape but diff coords)
'''

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        #take islands as squares and index them out of it 
        
        visited = set()
        r, c = len(grid), len(grid[0])
        unique = []
        res = 0
        
                    
        
        def dfs(i,j,tmp,origin):            
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1:
                return
            if (i,j) in visited or grid[i][j] == 0:
                return
            if grid[i][j] == 1:
                visited.add((i,j))            
            
            
            tmp.append((i - origin[0], j - origin[1]))
            dfs(i+1,j, tmp, origin)
            dfs(i, j+1, tmp, origin)
            dfs(i-1, j, tmp, origin)
            dfs(i, j-1, tmp, origin)
        
        for i in range(r):
            for j in range(c):
                if (i,j) not in visited and grid[i][j] == 1:
                    curr = []
                    origin = (i,j)
                    dfs(i,j,curr, origin)
                    print(curr)
                    if curr not in unique:
                        res += 1
                        unique.append(curr)
                    
        return res 

'''
REVISIT 
'''