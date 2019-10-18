class Solution:
    def toSeq(self, x):
        for char in iter(ascii(x)):
            yield char

    def reverse(self, x: int) -> int:
        negative = x < 0
        if negative:
            x = -x

        result = ''
        started = False
        for char in reversed(list(self.toSeq(x))):
            if not started and char is '0':
                continue
            result += char
            started = True

        if not started:
            return 0
        if negative:
            x = -1 * int(result)
        else:
            x = int(result)
        if x <= -2 ** 31:
            return 0
        if x > 2 ** 31:
            return 0
        return x
