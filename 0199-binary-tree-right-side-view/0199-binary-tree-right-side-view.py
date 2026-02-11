# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=deque([root])
        right_side=[]
        while queue:
            curr_len=len(queue)
            curr_path=[]
            for i in range(curr_len):
                node=queue.popleft()
                curr_path.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            right_side.append(curr_path[-1])
        return right_side