class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            if row >= m or row < 0 or col >= n or col < 0 or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row+1,col) + dfs(row-1,col) + dfs(row,col+1) + dfs(row,col-1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area