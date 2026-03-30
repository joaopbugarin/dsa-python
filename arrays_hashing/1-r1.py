from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in nums_map:
                nums_map[nums[i]] = i
            else:
                return [i, nums_map[diff]]
sol = Solution()
print(sol.twoSum([3,2,4],6))