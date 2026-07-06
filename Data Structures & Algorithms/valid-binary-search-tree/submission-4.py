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
        for value in values:
            # Recurse the binary tree
            def found(node, searching):
                if node is None:
                    return False

                if node.val == searching:
                    return True

                if searching < node.val:
                    return found(node.left, searching)

                if searching > node.val:
                    return found(node.right, searching)

            result = found(root, value)
            if not result:
                return False

        return True

