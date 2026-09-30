class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = 0
        word =[]
        for i in s:
            if i in word:
                word=[]
                sub = max(len(word),sub)
            if i not in word:
                word.append(i)
                sub = max(len(word),sub)
        return sub
        