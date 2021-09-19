class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        #iterate
        m = len(board)
        n = len(board[0])
        
        rows = [[] for i in range(9)]
        cols = [[] for i in range(9)]
        boxes = [[] for i in range(9)]
        '''
        rows = [[]]*9
        cols = [[]]*9
        boxes = [[]]*9
        
        This doesn't work because this works by creating
        one list then creating a new list with 9 references
        to that one list you originally made. loools
        '''
        
        
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                
                if curr == ".":
                    continue #break out of current iteration if period
                #rows
                
                #print(rows)
                if curr in rows[i]:
                    return False
                if curr not in rows[i]:
                    rows[i].append(curr)
                    
                #cols
                #print(cols)
                if curr in cols[j]:
                    return False
                if curr not in cols[j]:
                    cols[j].append(curr)
                
                #boxes
                #order of boxes is left to right
                #top to bottom
                div_i = i // 3 #floor division to get everything to the indices we want
                div_j = j // 3 
                box_n = div_i*3 + div_j

                if curr in boxes[box_n]:
                    return False
                if curr not in boxes[box_n]:
                    boxes[box_n].append(curr)
                
                
        return True