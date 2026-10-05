class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left =0
        substr = list(t)
        len_s = len(substr)
        res = []

        for right in range(len(s)):
            if s[right] in substr:
                while len_s>=0:
                    res.append(s[right])
                    len_s-=1

        print(''.join(res))
        