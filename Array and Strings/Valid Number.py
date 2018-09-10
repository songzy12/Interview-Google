# https://leetcode.com/explore/interview/card/google/59/array-and-strings/443/


class Solution:
    def isNumber(self, s):
        s = s.strip()
        if s and s[0] in '-+':  # NOTE: "+.8"
            s = s[1:]

        def is_scientific(s):
            if s.count('e') != 1:
                return False
            index = s.find('e')
            return (is_float(s[:index]) or is_integer(s[:index])) and is_integer(s[index + 1:]) # NOTE: "2e0"

        def is_positive(s):  # NOTE: "-1."
            if not s:
                return False
            for c in s:
                import string
                if c not in string.digits:
                    return False
            return True

        def is_integer(s):
            if s and (s[0] == '-' or s[0] == '+'):  # NOTE: "+.8"
                return is_positive(s[1:])
            return is_positive(s)

        def is_float(s):
            if s.count('.') != 1:
                return False
            index = s.find('.')  # NOTE: be cateful with copy & paste
            if s[:index] and not is_integer(s[:index]):
                return False
            if s[index + 1:] and not is_positive(s[index + 1:]):
                return False
            if not s[:index] and not s[index + 1:]:  # NOTE: "."
                return False
            return True

        return is_scientific(s) or is_integer(s) or is_float(s)