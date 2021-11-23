from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, s_max = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                s_now = height[i] * (j - i)
                i += 1
            else:
                s_now = height[j] * (j - i)
                j -= 1
            if s_now > s_max:
                s_max = s_now
        return s_max


s = Solution()
print(
    s.maxArea(
        [1, 8, 6, 2, 5, 4, 8, 3, 7]
    )
)
