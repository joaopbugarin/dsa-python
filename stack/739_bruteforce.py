class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            acc = 0
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    answer[i] = acc+1
                    break
                else:
                    acc += 1
            print(answer)
        return answer

test = Solution()
print(test.dailyTemperatures([73,74,75,71,69,72,76,73]))