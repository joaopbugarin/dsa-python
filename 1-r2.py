class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff not in seen:
                seen[curr] = i
            else:
                return [i,seen.get(diff)]
