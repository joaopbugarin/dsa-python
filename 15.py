class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left_pointer = 0
        nums = sorted(nums)  # nlogn
        print(nums)
        sol = []
        for i in range(len(nums)):
            left_pointer = i + 1
            right_pointer = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left_pointer < right_pointer:
                adds = nums[left_pointer] + nums[right_pointer]
                lookfor = -nums[i]

                if adds > lookfor:
                    right_pointer -= 1
                elif adds < lookfor:
                    left_pointer += 1
                elif adds == lookfor:
                    sol.append(
                        [
                            nums[i],
                            nums[left_pointer],
                            nums[right_pointer],  # type: ignore
                        ]
                    )
                    right_pointer -= 1
                    left_pointer += 1
                    while (
                        left_pointer < right_pointer
                        and nums[left_pointer] == nums[left_pointer - 1]
                    ):
                        left_pointer += 1
                    while (
                        left_pointer < right_pointer
                        and right_pointer < len(nums) - 1
                        and nums[right_pointer] == nums[right_pointer + 1]
                    ):
                        right_pointer -= 1
        return sol


solu = Solution()
print(solu.threeSum([0, 1, 1]))
print(solu.threeSum([-1, 0, 1, 2, -1, -4]))
print(solu.threeSum([0, 0, 0, 0]))
