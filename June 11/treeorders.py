class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def inorder_traversal(root):
    result = []
    def helper(node):
        if node:
            helper(node.left)
            result.append(node.value)
            helper(node.right)
    helper(root)
    return result

def postorder_traversal(root):
    result = []
    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            result.append(node.value)
    helper(root)
    return result

def preorder_traversal(root):
    result = []
    def helper(node):
        if node:
            result.append(node.value)
            helper(node.left)
            helper(node.right)
    helper(root)
    return result

# Create the nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform traversals
inorder_result = inorder_traversal(root)
postorder_result = postorder_traversal(root)
preorder_result = preorder_traversal(root)

print("Inorder Traversal:", inorder_result)
print("Postorder Traversal:", postorder_result)
print("Preorder Traversal:", preorder_result)