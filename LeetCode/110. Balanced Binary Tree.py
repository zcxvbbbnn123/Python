# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, node: TreeNode) -> int:
        if not node: return 0
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return (abs(self.height(root.left) - self.height(root.right)) <= 1
               and self.isBalanced(root.left)
               and self.isBalanced(root.right))

c = TreeNode(3, None, None)
b = TreeNode(2, None, c)
a = TreeNode(1, None, b)

A = Solution()
print(A.isBalanced(a))