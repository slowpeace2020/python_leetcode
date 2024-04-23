from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxRes = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxRes = max(area, maxRes)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxRes
