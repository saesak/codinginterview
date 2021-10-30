'''
Runtime: 2680 ms, faster than 5.07% of Python3 online submissions 
Memory Usage: 20.3 MB, less than 10.85% of Python3 online submissions

aka awful. But this was the most simple way to do it.

quick note --> int(number / number) rounds towards 0 in python

'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        def recurse(tok):
            
            if len(tok) == 1:
                return int(tok[0])
            
            for i in range(len(tok)):
                curr = tok[i]
                
                #print(tok)
                
                if curr == "+":
                    val = int(tok[i-2]) + int(tok[i-1])
                    tok.insert(i+1,val)
                    tok.pop(i-2)
                    tok.pop(i-2)
                    tok.pop(i-2)
                    return recurse(tok)
                elif curr == "-":
                    val = int(tok[i-2]) - int(tok[i-1])
                    tok.insert(i+1,val)
                    tok.pop(i-2)
                    tok.pop(i-2)
                    tok.pop(i-2)
                    return recurse(tok)
                elif curr == "*":
                    val = int(tok[i-2]) * int(tok[i-1])
                    tok.insert(i+1,val)
                    tok.pop(i-2)
                    tok.pop(i-2)
                    tok.pop(i-2)
                    return recurse(tok)
                elif curr == "/":
                    val = int(int(tok[i-2]) / int(tok[i-1]))
                    tok.insert(i+1,val)
                    tok.pop(i-2)
                    tok.pop(i-2)
                    tok.pop(i-2)
                    return recurse(tok)
        
        return recurse(tokens)


'''
better soln using stack

o(n) time and o(n) memory
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for tok in tokens:
            
            if tok not in "+/-*":
                stack.append(int(tok))
                continue
            
            n1 = stack.pop()
            n2 = stack.pop()
            
            
            if tok == '+':
                val = n2 + n1
            if tok == '/':
                val = int(n2 / n1)
            if tok == '*':
                val = n2 * n1
            if tok == '-':
                val = n2 - n1
            
            stack.append(val)
        
        return stack.pop()