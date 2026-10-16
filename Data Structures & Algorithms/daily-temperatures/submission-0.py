
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        left = 0
        answer = []

        while left < len(temperatures):
            right = left + 1

            while right < len(temperatures) and temperatures[right] <= temperatures[left]:
                right += 1

            if right < len(temperatures):
                answer.append(right - left)
            else:
                answer.append(0)

            left += 1

        return answer

        