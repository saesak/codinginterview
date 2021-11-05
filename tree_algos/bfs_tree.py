#BFS


'''
BFS DFS ARE REALLY SIMILAR

except BFS uses queue and DFS uses stack
'''

def bfs(root):
    if not root:
        #in case there's nothing given and root is just null
        return root

    queue = [root]

    while queue:
        #can either pop(0) and append
        #or pop() and insert(0, root)
        #your choice really
        curr = queue.pop()
        #do something to nodes in between here
        queue.insert(0, curr.left)
        queue.insert(0, curr.right)