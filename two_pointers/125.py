class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Strategy: 2 pointers squeezing
        s_filtered = s.lower()
        s_filtered = [x for x in s_filtered if x.isalnum()]
        left_index = 0
        right_index = len(s_filtered) - 1
        print(s_filtered)
        while left_index < right_index:
            if s_filtered[left_index] != s_filtered[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("raceacar"))
print(sol.isPalindrome("0P"))
