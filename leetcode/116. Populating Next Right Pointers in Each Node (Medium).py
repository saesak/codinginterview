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


'''
DFS Iterative Solution


'''
class Solution:
    def connect(self, root):
        if not root:
            return 
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                stack.append(curr.right)
                stack.append(curr.left)
                
        return root

'''
BFS Iterative Solution
'''

class Solution:    
    def connect(self, root):
        if not root:
            return 
        queue = [root]
        
        while queue:
            curr = queue.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                queue.insert(0, curr.left)
                queue.insert(0, curr.right)
    
        return root

'''
The beauty of the DFS and BFS iterative solutions are that they don't modify
curr.next if it doesn't point to anything because they are already initialized as null.

Just try quickly tracing through a depth 3 tree if you don't get why they work.
How it all starts is at the root initially put into the queue. From the get go, 
the bottom two are mapped to each other --> curr.left.next = curr.right
so that after that happens, the code under the curr.next if statement can use that
property to perform their operation. 


Another cool thing is that because it checks for if curr.next exists, if curr.next exists, it knows
it has access to the other side, so that it can access the curr.next.left node in order to map
the right node on the left branch to th left node on the right branch. 

'''