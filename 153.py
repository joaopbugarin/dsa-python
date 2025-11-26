class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]: #isn't in the sorted sided
                l = m + 1 #let's try to move towards it
            else: #if it's already in the sorted side
                r = m #let's move toward the min
        return nums[l]

sol = Solution()
print(sol.findMin([3,1,2]))