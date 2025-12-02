class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        curr = []
        maxx = float('-inf')
        while r < k:
            maxx = max(maxx, nums[r])
            r += 1
        #r vale alguma coisa
        for r in range(k-1,len(nums)):
            maxx = max(maxx, nums[r])
            curr.append(maxx)
            r += 1
            l += 1

        return curr


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
