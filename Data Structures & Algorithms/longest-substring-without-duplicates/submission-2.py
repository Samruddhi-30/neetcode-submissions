class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res =[]
        op=[]
        for i in range(0,len(s)):
            if s[i] in op:
                res.append(op)
                op = []
            if i not in op:
                op.append(s[i])
        a=0
        for i in res:
            a = max(a , len(i))

        return a
        