class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def dfs(i, m, n):
            if i == len(word):  # ✅ base case should be FIRST
                return True
            if m < 0 or n < 0 or m == len(board) or n == len(board[0]) or (m,n) in seen:
                return False
            if board[m][n] != word[i]:  # ✅ check current cell matches
                return False

            for m in range(len(board)):
                for n in range(len(board[m])):
                    if word[i] == board[m][n]:
                        seen.add((m, n))
                        found = (dfs(i+1, m, n+1) or
                                dfs(i+1, m, n-1) or
                                dfs(i+1, m+1, n) or
                                dfs(i+1, m-1, n))
                        seen.remove((m, n))  # backtrack
                        return found



