# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def create(root,val):
            if root is None:
                return TreeNode(val)
            if val<root.val:
                root.left=create(root.left,val)
            else:
                root.right = create(root.right, val)     
            return root
        root=None
        for val in preorder:
            root=create(root,val)
        return root 