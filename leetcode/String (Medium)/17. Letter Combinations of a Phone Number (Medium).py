class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        p_dict = {'2': 'abc', '3':'def', '4':'ghi',
                 '5':'jkl', '6':'mno', '7':'pqrs',
                 '8':'tuv', '9':'wxyz'}
        
        res = []
        str_len = len(digits)
        
        def recurse(digits, string, str_len):
            if len(digits) == 0 and str_len == len(string):
                res.append(string)
                return
            
            
            for ind, d in enumerate(digits):
                letters = p_dict[d]
                for let in letters:
                    recurse(digits[ind+1:], string + let, str_len)
            
            return
                    
        recurse(digits, '', str_len)
        
        
        return res