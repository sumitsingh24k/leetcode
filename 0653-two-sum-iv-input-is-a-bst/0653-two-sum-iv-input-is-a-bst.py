# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen=set()
        def check(root):
            if root is None:
                return False
            if root.val in seen:
                return True
            val=k-root.val
            seen.add(val)
            return check(root.left) or check(root.right)
        return check(root)
