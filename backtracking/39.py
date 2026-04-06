class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        i = 0
        res, sol = [], []
        n = len(candidates)
        def dfs (i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return

            if i == n or curr_sum > target:
                return
            
            dfs(i+1, curr_sum) #moving to the next number without picking the current
            #now, in the case we pick the current number
            sol.append(candidates[i])
            dfs(i, curr_sum + candidates[i]) #if we are picking the current num, i shouldnt move
            sol.pop()
        dfs(0, 0)
        return res