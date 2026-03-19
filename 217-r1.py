class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for el in nums:
            if not count.get(el):
                count[el] = 1
            else:
                return True
        return False