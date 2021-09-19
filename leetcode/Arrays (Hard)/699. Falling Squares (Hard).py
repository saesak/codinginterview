'''class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        
        #keep track of ans
        ans = []
        
        #keep track of squares
        squares = []
        
        for ele in positions:
            if len(squares) == 0:
                leftX = ele[0]
                rightX = ele[1] + ele[0]

                thelist = [(leftX, 0), (rightX, 0), (leftX, ele[1]), (rightX, ele[1])]
                
                #leftbot cor, left right cor, top left cor top right cor
                squares.append(thelist)
                ans.append(ele[1])
            else:
                max_h = 0
                curr = ele[1]
                leftX = ele[0]
                rightX = ele[1] + ele[0]
                thelist = [(leftX, 0), (rightX, 0), (leftX, ele[1]), (rightX, ele[1])]
                
                lensq = len(squares)
                for i in range(0, lensq):
                    curr= ele[1]
                    rangesq = set(range(squares[i][0][0], squares[i][1][0]+1))
                    rangeele = set(range(leftX, rightX+1))
                    if len(rangesq & rangeele) > 1: #if more than just a corner intersection then they're stacking
                        for j in range(0, i+1):
                            currrange = set(range(squares[j][0][0], squares[j][1][0]+1))
                            if len(currrange & rangeele) > 1:
                                curr = curr + squares[j][2][1]
                                #accounts for stacking of blocks if they cont to stack
                        max_h = max(max_h, curr, ans[-1])
                if max_h == 0:
                    max_h = max(curr, ans[-1])
                squares.append(thelist)
                ans.append(max_h)
        
        #difference between and and &? What is diff?
        #what if there are 2 stacks at the same time?
        return ans'''

'''
Above is inefficient and bad solution that doesn't work that
I tried to implement

Below is a solution i found in discuss
'''

class Solution:
    def fallingSquares(self, positions):
        intervals = []
        res = []
        h = 0
        for pos in positions:
            st, en, height = pos[0], pos[0] + pos[1] - 1, pos[1]
            current = [st, en, height]
            prev_h = 0
            for interval in intervals:
                if st > interval[1]:continue
                if en < interval[0]:continue
                prev_h = max(prev_h, interval[2])
                print(prev_h)
            current[2] += prev_h #updates total height of that block so you only have to look one back
            #genius lmao #so you don't have to add each and every one up again, just the one before
            #which is the one you're intersecting with anyways 
            h = max(h, current[2])
            res.append(h)
            intervals.append(current)
        return res
'''
Lessons to take --> know how to use continue 
be smart about storing stuff
I think I had the right idea, at least for iterating twice, once in the total
positions and once in the past positions, but I didn't think early
enough about all the edge cases and that was why my implementation
was poorly thought out and hacky and therefore incorrect. 
'''

'''
Think one of my current weak points is hard array problems on leetcode
going to start doing those right nowwww
'''