class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        
        w_l = []
        
        for letter in word:
            w_l.append(letter)
        
        copy = w_l
        
        visited = []
        
        def dfs(i, j, depth):
            if (i,j) in visited:
                return False
            if depth == len(w_l):
                return True
            if not((0 <= i < row) and (0 <= j < col)) or w_l[depth] != board[i][j]:
                return False
            
            
            res1, res2, res3, res4 = True, True, True, True
            
            visited.append((i,j))
            res1 = dfs(i+1, j, depth+1) and res1
            res2 = dfs(i-1, j, depth+1) and res2 
            res3 = dfs(i, j+1, depth+1) and res3
            res4 = dfs(i, j-1, depth+1) and res4
            visited.remove((i,j)) #this is the part i was missing why important???  
            
            print(visited)

            return res1 or res2 or res3 or res4
        
        truth = False
        
        for i in range(row):
            for j in range(col):
                curr = board[i][j]
                if curr == w_l[0]:
                    copy = w_l
                    truth = truth or dfs(i, j, 0)
        
        return truth


'''
Pretty much everything is kind of simple except the part where you have to remove
the coordinates you passed through, because by doing that, you allow it to backtrack
and discover new paths and stuff on the points they passed through previously
like for this particular test case

[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
"ABCESEEEFS"

stdout at above print statement for the testcase is 



[(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
[(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)]
[(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)]
[(0, 0), (0, 1), (0, 2), (1, 2)]
[(0, 0), (0, 1), (0, 2)]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (1, 1)]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (1, 2)]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2)]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (2, 2)]         #notice how it bounces back and forth, discovering new paths
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2)]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)]
[(0, 0), (0, 1), (0, 2), (0, 3)]
[(0, 0), (0, 1), (0, 2)]
[(0, 0), (0, 1)]
[(0, 0)]
[]




'''