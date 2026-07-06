# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def get_values(node):
            if node is None:
                return []

            leftval = get_values(node.left)
            rightval = get_values(node.right)

            return leftval + [ node.val] + rightval

        values = get_values(root)
        if len(values) != len(set(values)):
            return False
        
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False

        return True

