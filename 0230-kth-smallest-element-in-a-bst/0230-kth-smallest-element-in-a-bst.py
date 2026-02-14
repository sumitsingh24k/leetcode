# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index=0
        result=None
        def inorder(root):
            nonlocal index,result
            if root is None:
                return 
            inorder(root.left)
            index+=1
            if index==k:
                result=root.val
                return 
            inorder(root.right)
        inorder(root)
        return result