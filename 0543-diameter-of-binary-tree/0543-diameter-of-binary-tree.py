# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_val=0
        def diameter(node):
            nonlocal max_val
            if node is None:
                return 0
            left=diameter(node.left)
            right=diameter(node.right)
            max_val=max(max_val,right+left)
            return max(left,right)+1
        diameter(root)
        return max_val