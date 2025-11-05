from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        obj = set()
        for item in nums:  # worst case N operations - time
            if item in obj:
                return True
            obj.add(item)  # worst case N additions - space
        return False


# Time: O (n)

solution = Solution()
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
