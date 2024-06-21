'''views of tree
top,left,right,bottom'''

'''
                    10
                   /   \
                   5	15
                  / \	/ \
                 2   7 11  17
                / \
               1   3
               
vertical levels=6(1 2 3 (7,11-second prefer) 15 17
horizontal levels=4
top view=1 2 5 10 15 17
bottom view=1 2 3 11 15 17
left view=1 2 5 10
right view=10 15 17 3'''

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

    def left_view(self):
        def left_view_util(node, level, max_level):
            if node is None:
                return
            if level > max_level[0]:
                print(node.data, end=" ")
                max_level[0] = level
            left_view_util(node.left, level + 1, max_level)
            left_view_util(node.right, level + 1, max_level)
        
        max_level = [0]
        left_view_util(self.root, 1, max_level)
        print()

    def right_view(self):
        def right_view_util(node, level, max_level):
            if node is None:
                return
            if level > max_level[0]:
                print(node.data, end=" ")
                max_level[0] = level
            right_view_util(node.right, level + 1, max_level)
            right_view_util(node.left, level + 1, max_level)
        
        max_level = [0]
        right_view_util(self.root, 1, max_level)
        print()

    def top_view(self):
        def top_view_util(node, level, hd, level_map, hd_map):
            if node is None:
                return
            if hd not in hd_map or level < level_map[hd]:
                level_map[hd] = level
                hd_map[hd] = node.data
            top_view_util(node.left, level + 1, hd - 1, level_map, hd_map)
            top_view_util(node.right, level + 1, hd + 1, level_map, hd_map)
        
        level_map = {}
        hd_map = {}
        top_view_util(self.root, 0, 0, level_map, hd_map)
        for hd in sorted(hd_map.keys()):
            print(hd_map[hd], end=" ")
        print()
        
    
    def bottom_view(self):
        if self.root is None:
            return
        
        # Dictionary to store horizontal distance (hd) of nodes from the root
        hd_map = {}
        # Queue to perform level order traversal
        queue = [(self.root, 0)]  # Tuple containing node and its hd
        
        # Traverse the tree level by level
        while queue:
            node, hd = queue.pop(0)
            # Update the hd_map with the latest node for the current hd
            hd_map[hd] = node.data
            
            # Add left child to the queue with updated hd
            if node.left:
                queue.append((node.left, hd - 1))
            # Add right child to the queue with updated hd
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Print the nodes at the bottom view
        for hd in sorted(hd_map.keys()):
            print(hd_map[hd], end=" ")
        print()

t1 = Tree()
t1.insert(10)
t1.insert(5)
t1.insert(2)
t1.insert(1)
t1.insert(7)
t1.insert(3)
t1.insert(15)
t1.insert(11)
t1.insert(17)

print("Left view:")
t1.left_view()  
print("Right view:")
t1.right_view()  
print("Top view:")
t1.top_view()
print("Bottom view:")
t1.bottom_view()