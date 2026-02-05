# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue=deque([root])
        count=0
        while queue:
            root=queue.popleft()
            count+=1
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
        return count 