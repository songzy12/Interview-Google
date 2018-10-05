class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in '+-*/':
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '+':
                    res = op1 + op2
                elif token == '-':
                    res = op1 - op2
                elif token == '*':
                    res = op1 * op2
                else:
                    # NOTE: // for negative numbers
                    res = abs(op1) // abs(op2) * (1 if op1 * op2 >= 0 else -1)
                stack.append(res)
            else:
                stack.append(int(token))

            # print(token, stack)
        return stack.pop()


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))
