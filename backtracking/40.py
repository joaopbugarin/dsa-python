class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        i = 0

        def dfs(i, curr_sum, seen):
            if i == len(candidates):
                if curr_sum == target:
                    res.append(sol[:])
                return

            dfs(i+1, curr_sum, seen)

            if candidates[i] not in seen:
                sol.append(candidates[i])
                seen.add(candidates[i])
                curr_sum += candidates[i]
                dfs(i+1, curr_sum, seen)
                curr_sum -= candidates[i]
                seen.remove(candidates[i])
                sol.pop()

        dfs(0, 0, set())
        return res
