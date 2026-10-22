class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        l = heights.index(max(heights))
        if l<len(heights)-1 :
            a , b , c = heights[l],heights[l-1],heights[l+1]
            res = max(min(a,b) * 2 , min(a,b,c) * 3 , min(b,c)*2 , a)
        else :
            a , b = heights[l], heights[l-1]
            res = max(min(a,b) * 2 , a)

        return res
        