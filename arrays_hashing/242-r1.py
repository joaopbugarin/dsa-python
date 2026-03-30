from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for char in s:
            count_s[char] += 1
        for char in t:
            count_t[char] += 1
        for key in count_s:
            if count_s[key] != count_t[key]:
                return False
        return True

sol = Solution()
print(sol.isAnagram("anagram","nagaram"))
print(sol.isAnagram("anagram","nagarama"))
