def visit(root):
    print(root.val)


#recursive 

def post_order(root): #remember it like this postorder so you visit after you do any recursion
    if root != None:
        post_order(root.left)
        post_order(root.right)
        visit(root)


#iterative

#run with print statements on here
#https://leetcode.com/problems/binary-tree-postorder-traversal/
#to get it 

'''it basically goes in this order

all of the left side of the tree because have to visit children first before you visit
the parents, then all of the right side of the tree because you have to visit children
first before you visit parents then since there are no children left, you can visit the
head of the tree at the top 
'''

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        postorder = []
        stack = [root]
        visited = set()
        while stack:
            root = stack[-1]
            print(root, postorder)
            if root:
                if root not in visited:
                    visited.add(root)
                    stack.append(root.left)
                elif root.right and root.right not in visited:
                    stack.append(root.right)
                else:
                    root = stack.pop()
                    postorder.append(root.val)                    
            else:
                stack.pop()
                
        return postorder