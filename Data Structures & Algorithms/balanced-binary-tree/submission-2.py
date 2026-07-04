# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_diff(val):
            if val is None:
                return 0

            left = height_diff(val.left)
            if left == -1:
                return -1

            right = height_diff(val.right)
            if right == -1:
                return -1
            
            diff = abs(left - right)
            if diff > 1:
                return -1

            return max(left, right) + 1

        return height_diff(root) != -1

