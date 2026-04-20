# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []
        if root is None:
            return data

        data += self.postorderTraversal(root.left)
        data += self.postorderTraversal(root.right)
        data.append(root.val)

        return data
        