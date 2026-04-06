class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        seen = set()
        def dfs(i):
            if i == len(nums):
                res.append(sol[:])

            for num in nums:
                if num in seen:
                    continue

                sol.append(num)
                seen.add(num)
                dfs(i+1)
                sol.pop()
                seen.remove(num)

        dfs(0)
        return res
