# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # much shorter
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

        # kinda too long
        # if not root: return root 
        # if root.left and root.right:
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        #     root.left, root.right = root.right, root.left
        # elif root.left:
        #     self.invertTree(root.left)
        #     root.left, root.right = root.right, root.left
        # elif root.right:
        #     self.invertTree(root.right)
        #     root.left, root.right = root.right, root.left
        # return root