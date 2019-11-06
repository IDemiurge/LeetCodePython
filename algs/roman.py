# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        switchMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        maxVal = 0
        for char in reversed(list(s)):
            val = switchMap.get(char)
            if maxVal <= val:
                maxVal = val
                result += val
            else:
                result -= val

        return result

    print(romanToInt(None, "LVIII"))
