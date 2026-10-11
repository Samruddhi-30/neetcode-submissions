class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k
        op=[]

        if len(nums)==1:
            return [nums[0]]
        while right<=len(nums):
            
            op.append(max(nums[left:right]))
            left+=1
            right+=1

        return op
        