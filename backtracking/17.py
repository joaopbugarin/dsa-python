class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, sol = [], []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        i = 0 #digit pos
        n = len(digits)
        def dfs(i):
            if i == n:
                res.append("".join(sol))
                return
            
            for char in phone[digits[i]]:
                sol.append(char)
                dfs(i+1)
                sol.pop()
        dfs(i)
        return res
            