from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        result = []
        track_max = deque() #index

        for r in range(len(nums)):
            while track_max and nums[track_max[-1]] < nums[r]:
                track_max.pop()
            track_max.append(r)

            #remove leftmost if not in the window
            while track_max and l > track_max[0]:
                track_max.popleft()

            if r >= k -1:
                result.append(nums[track_max[0]])
                l += 1

        return result


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
print(sol.maxSlidingWindow([1,-1],1))
