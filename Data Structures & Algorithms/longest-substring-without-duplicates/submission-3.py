class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        window = set()
        left=0

        for right in range(len(s)):
            while(s[right] in window):
                window.remove(s[left])
                left+=1
            
            window.add(s[right])
            max_len=max(len(window) , max_len)

        return max_len
        

    
        