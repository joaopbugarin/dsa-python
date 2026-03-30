class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #ologn calls for binary search
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        print(l,r,m)

        while l <= r:
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
                m = (l + r) // 2
            elif target < nums[m]:
                r = m - 1
                m = (l + r) // 2
        return -1

sol = Solution()
print(sol.search([5],5))