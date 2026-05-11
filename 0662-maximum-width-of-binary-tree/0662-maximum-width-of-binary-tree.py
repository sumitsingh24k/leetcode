# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width=0
        queue=deque([(0,root)])
        while queue:
            len_queue=len(queue)
            curr=[]
            for i in range(len_queue):
                index,node=queue.popleft()
                curr.append(index)
                if node.left:
                    queue.append((2*index+1,node.left))
                if node.right:
                    queue.append((2*index+2,node.right))
            max_width=max(max_width,abs(curr[0]-curr[-1])+1)
        return max_width