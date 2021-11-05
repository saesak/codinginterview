class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        
        intervals = sorted(intervals, key= lambda x: x[0])
        
        res = []
        
        for i in range(n):
            if len(res) > 0:
                #overlap
                if res[-1][0] <= intervals[i][0] <=res[-1][1]:
                    if res[-1][1] < intervals[i][1]:
                        res[-1][1] = intervals[i][1]
                #non-overlap
                else:
                    res.append(intervals[i])
            else:
                res.append(intervals[i])
                
        return res

'''
REVISIT
'''