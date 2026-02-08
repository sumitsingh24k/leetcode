# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_value={ val:i for i,val in enumerate (inorder)}
        postorder_index=len(postorder)-1
        def helper(left,right):
            nonlocal postorder_index
            if left>right:
                return None
            root_val=postorder[postorder_index]
            inorder_index=inorder_value[root_val]
            postorder_index-=1
            root=TreeNode(root_val)
            root.right=helper(inorder_index+1,right)
            root.left=helper(left,inorder_index-1)
            return root
        return helper(0, len(inorder) - 1)
    