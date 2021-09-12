# A binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None



#Recursive Version

def recTraversal(root):
    if root.left == None and root.right == None:
        return root.val
    #or can also add a if root != None statement
    #so it doesn't go to the None ones

    recTraversal(root.left)
    #do something to the nodes
    recTraversal(root.right)
    
#Iterative Version

def iterTraversal(root):
    #if we use append and pop for a list
    #it functions practically the same as a stack
    
    inorderlist = []
    stack = []
    curr = root

    while len(stack) > 0 or curr != None:
        #go all the way left
        #starting with node since we have to go right as well later
        if curr != None:
            stack.append(curr)
            curr = curr.left
        
        #retrieve right nodes
        #if it doesn't exist, it'll go to the next one stored for the left branches
        #when it goes right from the root
        #it'll go first to the left bottom then back to the right
        #since it'll satisfy curr != None and go iterate to the right again
        else: 
            curr = stack.pop()
            inorderlist.append(curr.val)
            curr = curr.right
    return inorderlist



if __name__ == '__main__':

	""" Construct the following tree
			   1
			 /   \
			/     \
		   2       3
		  /      /   \
		 /      /     \
		4      5       6
			  / \
			 /   \
			7     8
	"""
#correct order
#[4, 2, 1, 7, 5, 8, 3, 6]
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.right.left = Node(5)
	root.right.right = Node(6)
	root.right.left.left = Node(7)
	root.right.left.right = Node(8)

	print(iterTraversal(root))