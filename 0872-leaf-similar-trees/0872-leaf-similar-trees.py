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
        def check(root,result):
            if not root:
                return 
            if not root.left and not root.right:
                result.append(root.val)
            check(root.left,result)
            check(root.right,result)
        check(root1,arr1)
        check(root2,arr2)
        return arr1==arr2