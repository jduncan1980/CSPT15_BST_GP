"""
You are given a binary tree.
Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.
Example:
Given the following binary tree
    5
   / \
  12  32
     /  \
    8    4
your function should return the depth = 3.
"""
class BSTNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def maxDepth(self):
       #Base cases
        if self is None:
            return 0 
        if self.left is None and self.right is None: 
            return 1
       #get left height
        if self.left is None: 
            return self.right.maxDepth()+1
       #get right height
        if self.right is None: 
            return self.left.maxDepth() +1
        return max(self.left.maxDepth(), self.right.maxDepth())+1
    
    # def iterMaxDepth(self):
    #     stack = []
        
    #     if self is not None:
    #         stack.append((1, self))
    #     depth = 0
        
    #     while stack != []:
    #         (current_depth, root) = stack.pop()
            

b1 = BSTNode(5)
b1.left = BSTNode(12)
b1.right = BSTNode(32)
b1.right.left = BSTNode(8)
b1.right.right = BSTNode(4)
print(b1.maxDepth())