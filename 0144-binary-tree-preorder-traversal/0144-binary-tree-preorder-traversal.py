# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root,result):
            if root is None:
                return result
            result.append(root.val)
            preorder(root.left,result)
            preorder(root.right,result)
            return result 
        return preorder(root,[])