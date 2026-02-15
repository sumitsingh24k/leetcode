# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dictionary={}
        def check(root):
            if root is None:
                return False
            if root.val in dictionary:
                return True
            remain=k-root.val
            dictionary[remain]=root.val
            return check(root.left) or check(root.right)
        return check(root)


