class Solution:
    def romanToInt(self, s: str) -> int:
        order = {"I":1, "V":2, "X":3, "L":4, "C":5, "D":6, "M":7}
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        digit = roman_dict[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if order[s[i]] < order[s[i+1]]:
                digit -= roman_dict[s[i]]
            else:
                digit += roman_dict[s[i]]
        return digit