class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        
        for i in range(len(heights)+1):
            for j in range(i+1 , len(heights)+1):
                myArr = heights[i:j]
                min_arr = min(myArr)
                length = len(myArr)
                area = min_arr * length
                max_area = max(area , max_area)

        return max_area
        