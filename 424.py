from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, max_freq, letter_count,result = 0,0,defaultdict(int),0
        for right in range(len(s)):
            letter_count[s[right]] += 1
            max_freq = max(max_freq, letter_count[s[right]])
            if (right - left + 1) - max_freq > k:
                letter_count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
            print("result:",result)
        return result
print(Solution().characterReplacement("ABAB",2))