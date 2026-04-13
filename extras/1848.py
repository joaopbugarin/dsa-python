class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_seen = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                min_seen = min(min_seen, abs(i - start))

        return min_seen