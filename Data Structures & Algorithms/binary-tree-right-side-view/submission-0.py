# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        leftres = self.rightSideView(root.left)
        rightres = self.rightSideView(root.right)

        res = [root.val]
        idx = 0

        while idx < min(len(leftres), len(rightres)):
            res.append(max(leftres[idx], rightres[idx]))
            idx += 1

        remaining = leftres if len(leftres) > len(rightres) else rightres 
        while idx < len(remaining):
            res.append(remaining[idx])
            idx += 1

        return res


        