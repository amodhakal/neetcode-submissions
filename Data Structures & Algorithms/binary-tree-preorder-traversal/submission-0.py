# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []
        if root is None:
            return data
        
        data.append(root.val)
        data += self.preorderTraversal(root.left)
        data += self.preorderTraversal(root.right)

        return data

        