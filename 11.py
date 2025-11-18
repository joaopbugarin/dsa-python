class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        curr = 0
        while left_pointer < right_pointer:
            min_value = min(height[left_pointer], height[right_pointer])
            curr = min_value * (right_pointer - left_pointer)
            print(
                "LP:", height[left_pointer], "RP:", height[right_pointer], "area:", curr
            )
            if curr > max_area:
                max_area = curr
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area


print(Solution().maxArea([8, 7, 2, 1]))
