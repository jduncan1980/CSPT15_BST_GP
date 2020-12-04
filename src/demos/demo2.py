"""
You are given a binary tree. You need to write a function that can determin if
it is a valid binary search tree.
The rules for a valid binary search tree are:
- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.
Example 1:
Input:
    5
   / \
  3   7
Output: True
Example 2:
Input:
    10
   / \
  2   8
     / \
    6  12
Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_valid_BST(self, root):
        stack, in_order = [], float('-Infinity')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            if root.value <= in_order:
                return False
            
            in_order = root.value
            root = root.right
            
        return True

b1 = TreeNode(5)
b1.left = TreeNode(3)
b1.right = TreeNode(7)

b2 = TreeNode(10)
b2.left = TreeNode(2)
b2.right = TreeNode(8)
b2.right.left = TreeNode(6)
b2.right.right = TreeNode(12)

print(b1.is_valid_BST(b1))

print(b2.is_valid_BST(b2))