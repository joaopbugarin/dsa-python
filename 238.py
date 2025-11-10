class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        # for i in range(0, len(nums)):
        #     left_product = 1
        #     right_product = 1
        #     for j in range(0, i):
        #         left_product *= nums[j]
        #     for k in range(i + 1, len(nums)):
        #         right_product *= nums[k]
        #     answer[i] = left_product * right_product
        # return answer
        # Approach too slow!

        # calculate the left side and store in the array
        # then calculate right products and multiply

        left_product = 1
        for i in range(len(nums)):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


solution = Solution()
print(solution.productExceptSelf([0, 0]))
