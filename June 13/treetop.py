class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        else:
            if x < root.data:
                root.left = self.create(root.left, x)
            else:
                root.right = self.create(root.right, x)
        return root

    def insert(self, x):
        self.root = self.create(self.root, x)
    
     def top_view(self):
        if not self.root:
            return []
        queue = [(self.root, 0)]
        top_view_map = {}
        min_hd = max_hd = 0
        while queue:
            node, hd = queue.pop(0)
            if hd not in top_view_map:
                top_view_map[hd] = node.data
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        top_view_result = [top_view_map[hd] for hd in range(min_hd, max_hd + 1)]
        return top_view_result
t1 = Tree()
t1.insert(10)
t1.insert(5)
t1.insert(20)
t1.insert(1)
t1.insert(7)
t1.insert(6)
t1.insert(8)
t1.insert(25)