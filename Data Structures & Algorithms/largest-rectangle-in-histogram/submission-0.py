class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                width = i - index
                area = width * height
                maxArea = max(area, maxArea)

                start = index

            stack.append((start, h))
            
        while stack:
            start, height = stack.pop()
            width = len(heights) - start
            area = width * height
            maxArea = max(area, maxArea)
        
        return maxArea