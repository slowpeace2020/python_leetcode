class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        # dp = [[False for i in range(0, n)] for j in range(0, m)]
        # dp[i][j]代表s前i个字母和p的前j个字母匹配情况
        dp = [[False] * (n + 1) for _ in range(0, m + 1)]
        dp[0][0] = True
        # 特殊情况，前面的不匹配，不算
        for j in range(2, n):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                        # aa| .*   aaa|a.*  aaa|aa.*  aaa|aaa*  aaa|aa*
                        # 前一个字符匹配的情况分为三种情况，*重复前面的字符一次aaa|aa*，*多余用不上aaa|aaa*，*连同前面的字符多余用不上aa|aaa*,aa|aa.*
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]

        return dp[m][n]

    # def isMatchI(self, s: str, p: str) -> bool:
    #     i = len(s) - 1
    #     j = len(p) - 1
    #     return self.backtrack(s, p, i, j)
    #
    # def backtrack(self, cache, s, p, i, j):
    #     key = (i, j)
    #     if key in cache:
    #         return cache[key]
    #
    #     if i == -1 and j == -1:
    #         cache[key] = True
    #         return True
    #
    #     if i != -1 and j == -1:
    #         cache[key] = False
    #         return False
    #     if i == -1 and p[j] == '*':
    #         k = j
    #         while k != -1 and p[k] == '*':
    #             k -= 2
    #         if k == -1:
    #             cache[key] = True
    #             return True
    #
    #         cache[key] = False
    #         return cache[key]


