class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen  = set()
        l = 0
        r = 0
        max_size = float('-inf')

        if len(s) == 0:
                return 0

        while l <= len(s) - 1 and r <= len(s) - 1:
            if s[r] not in seen :
                seen.add(s[r])
                max_size = max(max_size, r-l+1)
                r += 1
                continue

            if l < r:
                seen.remove(s[l])
                l += 1

        return max_size
