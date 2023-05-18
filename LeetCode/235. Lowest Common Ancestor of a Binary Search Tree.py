# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        low, high = sorted([p.val, q.val])
        while root:
            if low > root.val:
                root = root.right
            elif high < root.val:
                root = root.left
            else:
                return root
            
        # #Kinda long code first idea came up
        # #Shit dont need to do recursion using while root
        # if p.val == root.val or q.val == root.val:
        #     return root
        # while root:
        #     if (p.val < root.val < q.val) or (p.val > root.val > q.val):
        #         return root
        #     elif p.val > root.val:
        #         return self.lowestCommonAncestor(root.right, p, q)
        #     else:
        #         return self.lowestCommonAncestor(root.left, p, q)