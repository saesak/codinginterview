#recursive version

def visit(root):
    print(visit.val)

def preorder(root):
    visit(root)
    if root.left != None:
        preorder(root.left)
    if root.right != None:
        preorder(root.right)

#iterative version 

def preorder_it(root):

    queue = []
    curr = root

    while len(queue) != 0 and curr != None:
        if curr:
            queue.insert(0,curr)
            curr = curr.left 
        else:
            curr = queue.pop()
            visit(curr)
            curr = curr.right 