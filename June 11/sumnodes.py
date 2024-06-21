class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def sum_of_nodes(node):
    if node is None:
        return 0  # Return 0 for null nodes
    return node.value + sum_of_nodes(node.left) + sum_of_nodes(node.right)
       
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

total_sum = sum_of_nodes(root)
print("Sum of all nodes:", total_sum)