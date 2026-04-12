class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, sol = [], []
        invalid = {}

        def create_board(n):
            board = [ [ '.' for _ in range (n) ] for _ in range(n) ]
            return board

        def mark(r, c, val):
            invalid[(r,c)] = invalid.get((r,c), 0) + val
            if invalid[(r,c)] == 0:
                del invalid[(r,c)]

        def make_invalid(j, k):
            mark(j, k, 1)
            for i in range(n):
                if i != j:
                    mark(i, k, 1)
                if i != k:
                    mark(j, i, 1)
                if i > 0:
                    if j + i < n and k + i < n:
                        mark(j+i, k+i, 1)
                    if j - i >= 0 and k + i < n:
                        mark(j-i, k+i, 1)
                    if j - i >= 0 and k - i >= 0:
                        mark(j-i, k-i, 1)
                    if j + i < n and k - i >= 0:
                        mark(j+i, k-i, 1)

        def make_valid(j, k):
            mark(j, k, -1)
            for i in range(n):
                if i != j:
                    mark(i, k, -1)
                if i != k:
                    mark(j, i, -1)
                if i > 0:
                    if j + i < n and k + i < n:
                        mark(j+i, k+i, -1)
                    if j - i >= 0 and k + i < n:
                        mark(j-i, k+i, -1)
                    if j - i >= 0 and k - i >= 0:
                        mark(j-i, k-i, -1)
                    if j + i < n and k - i >= 0:
                        mark(j+i, k-i, -1)


        board = create_board(n)
        def dfs(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if (row, col) not in invalid:
                    board[row][col] = 'Q'
                    make_invalid(row, col)
                    dfs(row + 1)
                    make_valid(row, col)
                    board[row][col] = '.'

        dfs(0)
        return res
