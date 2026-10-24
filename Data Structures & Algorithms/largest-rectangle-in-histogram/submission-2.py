class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)+1):
            for j in range(i+1 ,len(heights)+1):
                myArr = heights[i:j]
                area = min(myArr) * len(myArr)
                maxArea = max(area , maxArea)

        return maxArea
        