from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                result[1] = i
                result[0] = num_map[target - num]
                return result
            num_map[num] = i
        return num
