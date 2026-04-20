class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        parent = list(range(n * n))
        size = [1] * (n * n)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            # union by size
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]

        def index(i, j):
            return i * n + j

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        # Step 1: connect all 1s
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            union(index(i, j), index(ni, nj))

        # Step 2: compute area of each component
        root_area = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    r = find(index(i, j))
                    root_area[r] = size[r]

        max_area = max(root_area.values(), default=0)

        # Step 3: try flipping each 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    area = 1
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            r = find(index(ni, nj))
                            if r not in seen:
                                seen.add(r)
                                area += size[r]
                    max_area = max(max_area, area)

        return max_area