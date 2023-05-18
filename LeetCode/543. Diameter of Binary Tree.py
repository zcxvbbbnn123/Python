# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.maxDepth = 0
        
    def diameterOfBinaryTree(self, root: TreeNode):
        
        def depth(node: TreeNode):
            if not node: return 0
            left = depth(node.left)
            right = depth(node.right)
            self.maxDepth = max(self.maxDepth, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.maxDepth
        
