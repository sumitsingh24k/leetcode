# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque([root])
        result=[]
        index=0
        while queue:
            curr_len=len(queue)
            curr=[]
            for i in range(curr_len):
                node=queue.popleft()
                curr.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if (index % 2)!=0:
                result.append(curr[::-1])
            else:
                result.append(curr)
            index+=1
        return result