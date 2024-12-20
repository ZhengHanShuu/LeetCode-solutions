class Solution:
    def romanToInt(self, s: str) -> int:
        # create a hashmap to store the roman numeral values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        # initial the total value to 0, and the length of the string
        total = 0
        n = len(s)

        # iterate the string by length
        for i in range(n):
            # if the current value is smaller than the next value, subtract it
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # add it otherwise
                total += roman_map[s[i]]
        return total