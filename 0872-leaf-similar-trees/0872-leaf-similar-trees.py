# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1=[]
        arr2=[]
        def helper(root,result):
            if not root:
                return 
            if root.left is None and root.right is None:
                result.append(root.val)
            helper(root.left,result)
            helper(root.right,result)
        helper(root1,arr1)
        helper(root2,arr2)
        return arr1==arr2
