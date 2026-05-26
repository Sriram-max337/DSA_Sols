from collections import deque

def bfs(root):
    if not root:
        return
    
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)  # nodes in current level
        
        for _ in range(level_size):
            node = queue.popleft()
            # process node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if _ == level_size - 1:
                result.append(node.val)