# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width=0
        queue = deque([(0, root)]) 
        while queue:
            curr_len=len(queue)
            first_index=queue[0][0]
            second_index=queue[-1][0]
            max_width = max(max_width, second_index - first_index + 1)
            for i in range(curr_len):
                index,node=queue.popleft()
                if node.left:
                    queue.append((2 * index, node.left))
                if node.right:
                    queue.append((2 * index + 1, node.right))
        return max_width