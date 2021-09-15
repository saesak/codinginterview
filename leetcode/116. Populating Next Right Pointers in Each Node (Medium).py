"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

#https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/

'''
Inefficient Version

Mistakes made: iterated on the wrong way when I was popping elements
Next time, implement the code then trace through it by hand instead of using print statements

Used in order traversal, a form of DFS(Depth First Search)

'''

class Solution:
    def depth(self, root, depth, stack):
        if len(stack) < depth + 1:
            stack.append([])
        if root == None:
            return root
        
        stack[depth].append(root)

        self.depth(root.right, depth + 1, stack)
        self.depth(root.left, depth + 1, stack)
        
        
        return root
    
    
    def connect(self, root: 'Node') -> 'Node':
        stack = []

        self.depth(root, 0, stack)
        
        
        for ele in stack:
            while len(ele) > 0:
                if len(ele) == 1:
                    node = ele.pop()
                    node.next = None
                if len(ele) > 1:
                    node = ele.pop()
                    node.next = ele[-1]
        
        
        return root


