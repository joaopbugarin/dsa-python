class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair: (index, height)
        #NC solution approach, very hard exercise
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
