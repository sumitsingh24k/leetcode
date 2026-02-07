# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        check_previous=False
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if node is None:
                check_previous=True
            else:
                if check_previous:
                    return False 
                queue.append(node.left)
                queue.append(node.right)
        return True 