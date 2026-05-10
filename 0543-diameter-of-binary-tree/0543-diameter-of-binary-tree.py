# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_val=0
        def dfs(root):
            if root is None:
                return 0
            nonlocal max_val
            left=dfs(root.left)
            right=dfs(root.right)
            max_val=max(max_val,left+right)
            return 1+max(left,right)
        dfs(root)
        return max_val