# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path=[]
        result=[]
        def dfs(root):
            if root is None:
                return
            path.append(str(root.val))
            if root.left is None and root.right is None:
                result.append("->".join(path))
            else:
                dfs(root.left)
                dfs(root.right)
            path.pop()

        dfs(root)
        return result