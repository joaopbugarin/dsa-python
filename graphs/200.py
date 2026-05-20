class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        def dfs(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == '0' or (row, col) in seen:
                return

            seen.add((row, col))

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    islands += 1
                    dfs(row, col)

        return islands

