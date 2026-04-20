# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Nothing tree
        if root is None:
            return TreeNode(val)

        current = root
        while True:
            currentval = current.val

            if currentval > val:
                # Traverse left if possible
                if current.left is not None:
                    current = current.left
                    continue

                # Add to left and return
                current.left = TreeNode(val)
                return root

            if currentval < val:
                # Traverse right if possible
                if current.right is not None:
                    current = current.right
                    continue

                # Add to right and return
                current.right = TreeNode(val)
                return root

        