class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        words = sorted(list(s1))
        right = len(s1)

        left =0
        while right<=len(s2):
            window = s2[left:right]
            if sorted(list(window)) == words:
                return True
            left+=1
            right+=1

        return False
        