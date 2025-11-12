class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)  # type: ignore
        max_count = 0
        for num in nums:
            if num - 1 in nums:
                continue
            else:
                count = 1
                while num + 1 in nums:
                    count += 1
                    num = num + 1
                if count > max_count:
                    max_count = count
        return max_count


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(sol.longestConsecutive([1, 0, 1, 2]))
