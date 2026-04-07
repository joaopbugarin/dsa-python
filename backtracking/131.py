class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol= [], []

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i == len(s):
                res.append(sol[:])
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    sol.append(s[i:j+1]) #last element not included
                    dfs(j+1)
                    sol.pop()

        dfs(0)
        return res