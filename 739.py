class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # guarda índices

        for i in range(n):
            # enquanto temp atual é maior que temp no topo da stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx

            stack.append(i)

        return answer

test = Solution()
print(test.dailyTemperatures([73,74,75,71,69,72,76,73]))