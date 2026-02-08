# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_value_with_index={val:i for i,val in enumerate(inorder)}
        preorder_index=0
        def helper(left,right):
            nonlocal preorder_index
            if left>right:
                return None 
            root_val = preorder[preorder_index]
            index_for_root=inorder_value_with_index[root_val]
            preorder_index+=1
            root=TreeNode(root_val)
            root.left=helper(left,index_for_root-1)
            root.right=helper(index_for_root+1,right)
            return root
        return helper(0, len(preorder) - 1)