# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        column_table = defaultdict(list)
        def dfs(node, row, col):
            if not node:
                return
            column_table[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)
        result = []
        for col in sorted(column_table):
            column_nodes = sorted(column_table[col])
            result.append([val for row, val in column_nodes])
        return result
