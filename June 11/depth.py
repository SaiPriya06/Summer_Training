class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_depth(node):
    if node is None:
        return 0  # Return 0 for null nodes
    else:
        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)
        return 1 + max(left_depth, right_depth)

# Create the nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)

# Calculate the maximum depth of the tree starting from the root
tree_max_depth = max_depth(root)
print("Maximum depth of the tree:", tree_max_depth)

# Define the function to calculate the depth of a specific node
def node_depth(root, target, depth=0):
    if root is None:
        return -1  # Node not found
    if root.value == target:
        return depth
    # Check left subtree
    left_depth = node_depth(root.left, target, depth + 1)
    if left_depth != -1:
        return left_depth
    # Check right subtree
    return node_depth(root.right, target, depth + 1)

# Calculate the depth of a specific node
specific_node_depth = node_depth(root, 4)
print("Depth of the node with value 4:", specific_node_depth)