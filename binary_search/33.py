from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = 0, len(nums) - 1
        m = (l + r) // 2
        while l <= r:
            m = (l + r) // 2
            M = nums[m]
            L = nums[l]
            R = nums[r]
            if M == target:
                return m
            if L <= M: #left side of M is regularly sorted
                if L <= target < M: #if the target is here we do a regular binary search
                    r = m - 1
                else:
                    l = m + 1
            else: #if the right side is sorted regularly
                if M < target <= R: #if the target is here we do a regular binary search
                    l = m + 1
                else:
                    r = m -1
        return -1
sol = Solution()
print(sol.search([4,5,6,7,0,1,2],13))