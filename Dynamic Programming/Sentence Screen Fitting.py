class Solution(object):

    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """

        for word in sentence:
            if len(word) > cols:
                return 0

        def next_index_word(col, word):
            # return the last col after filling this word

            delta_row = 0
            col += 2

            if col >= cols:
                col = 0
                delta_row += 1

            if col + len(word) - 1 >= cols:
                col = 0
                delta_row += 1

            return delta_row, col + len(word) - 1

        dp = {}

        def next_index_sentence(col, sentence):
            _col = col
            if _col in dp:
                return dp[_col]

            delta_row = 0
            for word in sentence:
                # NOTE: do not use the same variable name
                _delta_row, col = next_index_word(col, word)
                delta_row += _delta_row
            dp[_col] = delta_row, col  # col has been changed
            return dp[_col]

        cur_row = -1
        cur_col = cols - 1  # this is a good init

        m = {}
        res = 0
        while True:
            if cur_col not in m:
                m[cur_col] = (res, cur_row)
            else:
                last_res, last_row = m[cur_col]
                delta_res, delta_row = res - last_res, cur_row - last_row

                remain_row = rows - 1 - cur_row  # NOTE: rows-1
                cnt = remain_row // delta_row

                res += cnt * delta_res
                cur_row += cnt * delta_row

            delta_row, cur_col = next_index_sentence(cur_col, sentence)

            if cur_row + delta_row >= rows:
                break

            res += 1
            cur_row += delta_row

        return res


sentence = ["f", "p", "a"]
rows = 8
cols = 7
print(Solution().wordsTyping(sentence, rows, cols))

# thought: dp(index) returns start from index
# the number of lines and the end position of one iteration
