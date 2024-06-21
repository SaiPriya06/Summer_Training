class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(node):-
    if node is None:
        return -1  # Return -1 for null nodes, as height of a leaf node is 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return 1 + max(left_height, right_height)

# Create the nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)

# Calculate the height of the tree starting from the root
tree_height = height(root)
print("Height of the tree:", tree_height)

# Calculate the height of a specific node
node_height = height(root.left)
print("Height of the node with value 2:", node_height)