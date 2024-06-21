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

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")
    
    def sum_of_nodes(self, root):
        if root is None:
            return 0
        return root.data + self.sum_of_nodes(root.left) + self.sum_of_nodes(root.right) #preorder 

    def sum_even(self, root):
        if (root==None):
            return 0
        if(root.data%2==0):
            return root.data + self.sum_even(root.left) + self.sum_even(root.right)
        else:
            return self.sum_even(root.left) + self.sum_even(root.right)
            
            # Return (even_sum, odd_sum)
    def sum_odd(self, root):
        if (root==None):
            return 0
        if(root.data%2!=0):
            return root.data + self.sum_odd(root.left) + self.sum_odd(root.right)
        else:
            return self.sum_odd(root.left) + self.sum_odd(root.right)
        
    def diff(self,root):
        even_sum = self.sum_even(root)
        odd_sum = self.sum_odd(root)
        return even_sum - odd_sum
    
    def diff1(self,root):
        if (root==None):
            return 0
        if(root.data%2!=0):
            return root.data + self.diff1(root.left) + self.diff1(root.right)
        return self.diff1(root.left) + self.diff1(root.right)-root.data
    
    def height(self,root):
        if root==None:
            return -1
        return 1+max(self.height(root.left),self.height(root.right))
    
    def is_balanced(self, root):
        return abs(self.height(root.left)-self.height(root.right))<=1
 
    def sum_even_odd_nodes(self, root):
        if root is None:
            return (0, 0)
        left_even_sum, left_odd_sum = self.sum_even_odd_nodes(root.left)
        right_even_sum, right_odd_sum = self.sum_even_odd_nodes(root.right)

        if root.data % 2 == 0:
            return (root.data + left_even_sum + right_even_sum, left_odd_sum + right_odd_sum)
        else:
            return (left_even_sum + right_even_sum, root.data + left_odd_sum + right_odd_sum)
        
    def count_leaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.count_leaf_nodes(root.left) + self.count_leaf_nodes(root.right)


    def sum_leaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        return self.sum_leaf_nodes(root.left) + self.sum_leaf_nodes(root.right)
    
    def search(self, root, x):
        if root is None or root.data == x:
            return root
        if x < root.data:
            return self.search(root.left, x)
        return self.search(root.right, x)
    
    



# Create and populate the tree
t1 = Tree()
t1.insert(10)
t1.insert(5)
t1.insert(20)
t1.insert(1)
t1.insert(7)
t1.insert(6)
t1.insert(8)
t1.insert(25)

# Print traversals
print("Inorder traversal:")
t1.inorder(t1.root)  
print("\nPreorder traversal:")
t1.preorder(t1.root)  
print("\nPostorder traversal:")
t1.postorder(t1.root)
print()

# Print sum of all nodes
print("Sum of all nodes:")
print(t1.sum_of_nodes(t1.root))

print("\neven sum")
print(t1.sum_even(t1.root))

print("\nodd sum")
print(t1.sum_odd(t1.root))

print("\ndifference even odd")
print(t1.diff(t1.root))

print("\ndifference alternate odd even")
print(t1.diff1(t1.root))

print("\nheight of root")
print(t1.height(t1.root))

print("\nBalance of tree is")
t1.is_balanced(t1.root)
if(t1.is_balanced(t1.root)):
    print("Balanced")
else:
    print("not Balanced")
    
leaf_count = t1.count_leaf_nodes(t1.root)
print("Number of leaf nodes:", leaf_count)

leaf_sum = t1.sum_leaf_nodes(t1.root)
print("Sum of all leaf nodes:", leaf_sum)

even_sum, odd_sum = t1.sum_even_odd_nodes(t1.root)
print("Sum of even nodes:", even_sum)
print("Sum of odd nodes:", odd_sum)

print("\nleft subtree sum")
print(t1.sum_of_nodes(t1.root.left))

print("\nright subtree sum")
print(t1.sum_of_nodes(t1.root.right))

search_value = 7
found_node = t1.search(t1.root, search_value)
if found_node:
    print("found")
else:
    print("not found")

