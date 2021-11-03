'''
okay soln

think there are better ways to do it though

came out on my first oracle interview

https://leetcode.com/problems/top-k-frequent-words/

REVISIT -- might be worth it
'''


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = dict()
        
        for i in range(len(words)):
            if words[i] in dic:
                dic[words[i]] += 1
            else:
                dic[words[i]] = 1
        
        def merge(L, R):
            
            tmp = []
            i, j = 0,0
            
            while i < len(L) and j < len(R):
                if L[i][1] > R[j][1]:
                    tmp.append(L[i])
                    i += 1
                elif L[i][1] < R[j][1]:
                    tmp.append(R[j])
                    j += 1
                elif L[i][1] == R[j][1]: #sort based on freq then if that is equal, sort on alphabetical order
                    if L[i][0] < R[j][0]:
                        tmp.append(L[i])
                        i += 1
                    else:
                        tmp.append(R[j])
                        j += 1
                        
            tmp.extend(L[i:])
            tmp.extend(R[j:])
            
            return tmp
        
        def mergesort(arr):
            m = len(arr) // 2
            
            if len(arr) <= 1:
                return arr
            
            left = mergesort(arr[0:m])
            right = mergesort(arr[m:])
            
            return merge(left, right)
        
        sort_words = mergesort(list(dic.items()))
        
        res = []
        
        for j in range(k):
            res.append(sort_words[j][0])
        
        return res