# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def check(root):
            if root is None:
                return 0    
            left_value=check(root.left)
            right_value=check(root.right)
            return max(left_value,right_value)+1
        return check(root)