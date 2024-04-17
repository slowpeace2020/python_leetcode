class Solution:
    # brute force
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 1
        max_str = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i:j + 1] == s[i:j + 1][::-1]:
                    max_len = j - i + 1
                    max_str = s[i:j + 1]

        return max_str

    # expand around center
    def longestPalindromeI(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        return max_str

    # dynamic programming
    def longestPalindromeII(self, s: str) -> str:
        if len(s)<=1:
            return s

        max_len =1
        max_str = s[0]

        # 初始化一个二维布尔类型的列表（list）
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[i]==s[j] and (i-j<=2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1>max_len:
                        max_len = i-j+1
                        max_str = s[j:i+1]

        return max_str

    # todo manacher algorithm



