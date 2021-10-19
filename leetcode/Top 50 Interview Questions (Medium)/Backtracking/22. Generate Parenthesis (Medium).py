'''still thinking about this one

have some work to do in the backtracking and dynamic programming
department. 
'''
'''
Brute force solution: 
Time Complexity : O(2^(2n) * n) For each of 2^2n sequences, we need to create and validate the sequence, which takes O(n) work.
Space Complexity: O(2^(2n) * n)


This seems like the truest form of backtracking to me, validating with 
brute force and then going back. But the next solution takes it a step
further and optimizes it for this particular problem. Which is kind of what
I have in the subsets and permutations solution files. 
'''
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

'''
They called this approach "backtracking" and it still is
but it's like more constrained. It's only partially checking whether
things are valid and letting the general logic of the problem
filter out most of the bad options. 

Time and Space complexity both: O(4^n/sqrt(n))
IDK why LOL
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left: #NOTICE HOW IT IS right<left NOT right<n
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans