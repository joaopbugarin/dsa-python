class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []
        def dfs(i, to_close, opened):
            if 2*n == i and to_close == 0:
                res.append("".join(sol))
                return

            if to_close > 0:
                sol.append(')')
                dfs(i+1, to_close - 1, opened)
                sol.pop()

            if opened < n:
                sol.append('(')
                opened += 1
                dfs(i+1, to_close + 1, opened)
                sol.pop()


        dfs(0, 0, 0)
        return res
