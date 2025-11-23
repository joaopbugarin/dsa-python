class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stk = []
        for char in s:
            if char in mapping:
                stk.append(mapping[char])
            elif stk and char == stk[-1]:
                stk.pop()
            else: return False
        return True and len(stk) == 0

sol = Solution()
print(sol.isValid("["))
