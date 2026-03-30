class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        adding = numbers[left_pointer] + numbers[right_pointer]
        while adding != target:
            if numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
                print("right_pointer: ", right_pointer)
            else:
                left_pointer += 1
                print("left_pointer: ", left_pointer)
            if left_pointer > right_pointer:
                break
            adding = numbers[right_pointer] + numbers[left_pointer]
        return [left_pointer + 1, right_pointer + 1]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
