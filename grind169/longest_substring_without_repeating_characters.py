class Solution:
    def lengthofLongestSubstringI(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0;

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])

        return maxLength

    def lengthofLongestSubstringII(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0

        for right in range(n):
            # 当前字符之前出现的位置在left左边，也相当于没出现过
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right

        return maxLength

    def lengthofLongestSubstringIII(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charIndex = [-1] * 128
        left = 0

        for right in range(n):
            # ord() 是一个内置函数，它用于获取给定字符的Unicode码点（code point）
            if charIndex[ord(s[right])] >= left:
                left = charIndex[ord(s[right])] + 1
            charIndex[ord(s[right])] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength


if __name__ == "__main__":
    solution = Solution()
    solution.lengthofLongestSubstringII("tmmzuxt")
