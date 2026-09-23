class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in op:
                op[sorted_word] = []
            
            op[sorted_word].append(word)

        return list(op.values())
        