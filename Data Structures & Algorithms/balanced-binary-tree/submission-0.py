# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalancedHelper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.isBalancedHelper(root.left)
        right = self.isBalancedHelper(root.right)

        if left == -1 or right == -1:
            return -1

        diff = abs(left - right)
        if diff > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root) != -1
    
        