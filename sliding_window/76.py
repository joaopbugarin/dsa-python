from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for char in t:
            count_t[char] += 1
        have = 0
        need = len(count_t)
        l = 0
        min_len = float('inf')
        result = ''
        for r in range(len(s)):
            count_s[s[r]] += 1
            if s[r] in count_t and count_t[s[r]] == count_s[s[r]]:
                have += 1
                while have == need:
                    if r - l + 1 < min_len:
                        min_len = r - l + 1
                        result = s[l:r+1]
                    count_s[s[l]] -= 1
                    if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                        have -= 1
                    l += 1
        return result

print(Solution().minWindow("A","A"))
