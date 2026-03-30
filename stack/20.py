class Solution:
    def isValid(self, s: str) -> bool:
        if len(list(s)) % 2 != 0:
            return False
        stk = []
        mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for char in s:
            if char in mapping:
                stk.append(char) #take notes on opening
            else:
                if not stk:
                    return False
                if char != mapping[stk.pop()]:
                    return False
        return len(stk) == 0 #remove all


solution = Solution()
print(solution.isValid(s="([])"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(("))
print(solution.isValid(s="){"))
print(solution.isValid(s="()))"))