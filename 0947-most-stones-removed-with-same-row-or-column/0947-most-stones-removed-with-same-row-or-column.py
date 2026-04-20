class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        size = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if size[px] < size[py]:
                parent[px] = py
                size[py] += size[px]
            else:
                parent[py] = px
                size[px] += size[py]

        nodes = set()

        for r, c in stones:
            row = r
            col = c + 10001   # shift columns

            if row not in parent:
                parent[row] = row
                size[row] = 1
            if col not in parent:
                parent[col] = col
                size[col] = 1

            union(row, col)

            nodes.add(row)
            nodes.add(col)

        components = 0
        for node in nodes:
            if find(node) == node:
                components += 1
        return len(stones) - components