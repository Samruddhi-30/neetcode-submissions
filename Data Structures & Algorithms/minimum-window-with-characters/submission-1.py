class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}

        have = 0
        required = len(need)

        left = 0

        res = ""
        res_len = float("inf")

        for right in range(len(s)):

            c = s[right]

            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:

                # Current window is valid
                window_len = right - left + 1

                if window_len < res_len:
                    res = s[left:right + 1]
                    res_len = window_len

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return res
        