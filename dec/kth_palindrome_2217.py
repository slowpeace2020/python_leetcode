from typing import List


class Solution:
    def get_palindrome(value, intLength):
        str_val = str(value)
        rev_str = str_val[::-1]
        if intLength % 2 == 1:
            rev_str = rev_str[1:]

        return int(str_val + rev_str)

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res = [0] * len(queries)

        len_half = (intLength - 1) // 2
        start = 10 ** len_half
        end = 10 ** (len_half + 1)

        for i, query in enumerate(queries):
            value = start + query - 1
            if value >= end:
                res[i] = -1
            else:
                res[i] = self.get_palindrome(value, intLength)

        return res
