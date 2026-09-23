class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        op = {}
        
        for num in nums: 
            if num not in op:
                op[num] =[]
                count = 0
                
            op[num].append(num)

        sorted_dict = dict(sorted(op.items(), key=lambda item: len(item[1]), reverse=True))
        return list(sorted_dict.keys())[:k]
        