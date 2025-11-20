class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                nums.append(int(token))
            else:
                operator = token
                if operator == '+':
                    res = nums[-1] + nums[-2]
                elif operator == '-':
                    res = nums[-2] - nums[-1]
                elif operator == '*':
                    res = nums[-2] * nums[-1]
                elif operator == '/':
                    res = int(nums[-2] / nums[-1])
                nums.pop()
                nums.pop()
                nums.append(res)

        return nums[0]

test = Solution()
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))