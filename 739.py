class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #trying with a stack containing tuples (num, index)
        n = len(temperatures)
        answer = [0] * n
        stk = []
        for i,t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                answer[stk_i] = i - stk_i
            stk.append((t,i))
        return answer

sol = Solution()
print(sol.dailyTemperatures([30,38,30,36,35,40,28]))