class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = []
        for i in range(len(nums)):
            val = nums[i]
            res = 1
            nums[i]=1
            for num in nums:
                res= res*num
            op.append(res)
            nums[i]=val

        return op
        