from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)
        count_s2 = defaultdict(int)

        for char in s1:
            count_s1[char] += 1

        l = 0
        for r in range(len(s2)):
            count_s2[s2[r]] += 1

            while count_s2[s2[r]] > count_s1[s2[r]]:
                count_s2[s2[l]] -= 1
                l += 1

            if r - l + 1 == len(s1):
                return True

        return False
sol = Solution()
print(sol.checkInclusion("ab","edibaooo"))
