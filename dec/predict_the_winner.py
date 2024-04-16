from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.canWin(nums, 0, n - 1, dp) >= 0

    def canWin(self, nums: List[int], start: int, end: int, dp: List[List[int]]) -> int:
        if dp[start][end] == -1:
            if start == end:
                dp[start][end] = nums[start]
            else:
                dp[start][end] = max(nums[start] - self.canWin(nums, start + 1, end, dp),
                                     nums[end] - self.canWin(nums, start, end - 1, dp))

        return dp[start][end]

    # def predictTheWinner(self, nums: List[int]) -> bool:
    #     return self.canWin(nums, 0, 0, 1)

    # def canWin(self, nums: List[int], sum1: int, sum2: int, player: int) -> bool:
    #     if not nums:
    #         return sum1 >= sum2
    #
    #     if len(nums) == 1:
    #         if player == 1:
    #             return sum1 + nums[0] >= sum2
    #         elif player == 2:
    #             return sum2 + nums[0] > sum1
    #
    #     va = nums[1:]
    #     vb = nums[:-1]
    #
    #     if player == 1:
    #         return not self.canWin(va, sum1 + nums[0], sum2, 2) or not self.canWin(vb, sum1 + nums[-1], sum2, 2)
    #     elif player == 2:
    #         return not self.canWin(va, sum1, sum2 + nums[0], 1) or not self.canWin(vb, sum1, sum2 + nums[-1], 1)
