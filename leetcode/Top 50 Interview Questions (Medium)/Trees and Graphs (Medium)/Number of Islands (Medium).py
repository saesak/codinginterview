class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        
        row = len(grid)
        col = len(grid[0])
        
        def dfs(i,j):
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1 or (i,j) in visited or grid[i][j] == "0":
                return
            
            
            if grid[i][j] == "1":
                visited.add((i, j))
                
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    res += 1 
        
        
        return res