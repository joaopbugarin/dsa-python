class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        curr = (l + r) // 2
        while l <= r:
            curr_num = nums[curr]
            print(curr)
            print(curr_num)
            if curr_num == target:
                return curr
            if curr_num > target:
                r = curr - 1
            elif curr_num < target:
                l = curr + 1
            curr = (r + l) // 2
        return -1

sol = Solution()
print(sol.search([-1,0,3,5,9,12],9))
print(sol.search([-1,0,3,5,9,12],2))
