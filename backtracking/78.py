class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        i = 0
        n = len(nums)

        def dfs(i):
            if i == n: #when we hit the end of nums we append the current sol to the final result
                res.append(sol[:]) #we must pass a shallow copy instead of a reference
                return
            #let's traverse nums, for each num we can pick or not it and its subsequents
            #first case: we do not pick the current number 
            dfs(i+1) #not picking the current means moving to the next one

            #let's pick the current numbers
            sol.append(nums[i]) #append it the the current solution list
            dfs(i+1) #now we move to the next one and the cycle restarts
            sol.pop() #remove the current number from the solution list bc it has to be
            # empty everytime we restart the cycle
        dfs(i)
        return res
        