class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] >= 10:
                digits[i] -= 10
                if i != 0:
                    digits[i-1] += 1
                else:
                    digits = [1] + digits
                    break
            else:
                break
        return digits

# >= 10 而不是 > 10