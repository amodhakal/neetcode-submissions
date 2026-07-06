class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        curr = root
        stack = []
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if not curr.val > prev:
                    return False
                prev = curr.val
                curr = curr.right
        return True