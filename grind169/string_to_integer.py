class Solution:
    # 有限状态机
    # state=0可以变成1或者2，state=1可以变成2,state=2可以变成2，
    # 每种状态有对应的计数办法
    def myAtoi(self, s: str) -> int:
        value = 0
        state = 0
        pos = 0
        sign = 1

        if len(s) == 0:
            return 0

        while pos < len(s):
            current_char = s[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        # 在Python中，整数的大小是动态的，它们的大小仅受系统内存的限制。
        # 因此，当你执行 value = sign * value 时，即使 value 的值超出了整数范围，
        # Python也会根据需要分配更多的内存来容纳结果，因此在理论上这行代码是有效的
        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value
