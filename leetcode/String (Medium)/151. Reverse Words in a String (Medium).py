class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_list = s.split(' ')
        
        
        res = []
        
        for i in range(len(s_list)-1, -1, -1):
            if s_list[i] != '':
                res.append(s_list[i])
        
        final = ' '.join(res)
        
        return final