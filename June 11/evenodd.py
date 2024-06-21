class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_even_odd_nodes(node):
    if node is None:
        return (0, 0)  # Return (even_sum, odd_sum)
    
    left_even_sum, left_odd_sum = sum_even_odd_nodes(node.left)
    right_even_sum, right_odd_sum = sum_even_odd_nodes(node.right)
    
    if node.value % 2 == 0:
        return (node.value + left_even_sum + right_even_sum, left_odd_sum + right_odd_sum)
    else:
        return (left_even_sum + right_even_sum, node.value + left_odd_sum + right_odd_sum)

# Create the nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)

# Calculate the sum of even and odd nodes
even_sum, odd_sum = sum_even_odd_nodes(root)
print("Sum of even nodes:", even_sum)
print("Sum of odd nodes:", odd_sum)