class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer] :
                if height[left_pointer] >= left_max :
                    left_max = height[left_pointer]
                else:
                    water += left_max - height[left_pointer]
                left_pointer += 1
            else:
                if height[right_pointer] >= right_max:
                    right_max = height[left_pointer]
                else:
                    water += right_max - height[right_pointer]
                right_pointer -= 1
        return water

sol = Solution()
print(sol.trap([4,2,3]))