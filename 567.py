from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, count_s1, count_s2 = 0, defaultdict(int), defaultdict(int)
        for char in s1:
            count_s1[char] += 1
        for right in range(len(s2)):
            count_s2[s2[right]] += 1
            if count_s2[s2[right]] > count_s1[s2[right]] or s2[right] not in count_s1:
                count_s2.clear()
                left = right + 1
            print("s1_count:",count_s1)
            print("s2_count:",count_s2)
            if right - left + 1 == len(s1):
                return True
            return False

sol = Solution()
print(sol.checkInclusion("ab","edibaooo"))
