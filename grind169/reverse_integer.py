class Solution:
    def reverse(self, x: int) -> int:
        # 算绝对值的逆转
        retval = int(str(abs(x)))[::-1]

        if retval.bit_length() > 31:
            return 0

        return -1 * retval if x < 0 else retval

    def reverseI(self, x: int) -> int:
        # 非负数直接转为数组逆转，负数去掉符号位逆转
        result = int(str(x)[::-1]) if x >= 0 else -int(str[x])[1:][::-1]
        # 在整数范围内返回值，否则返回0
        if -2 ** 31 <= result <= (2 ** 31) - 1:
            return result
        else:
            return 0
