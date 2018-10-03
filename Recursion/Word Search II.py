class Node:
    def __init__(self):
        self.m = {}  # NOTE: rater than class static variable
        self.end = False
        self.word = ''


class Solution(object):

    def __init__(self):
        self.visited = set([])
        self.trie = Node()
        self.res = set([])
        self.board = []

    def check(self, node, i, j):
        """
        check whether board[i][j] in node
        """

        def valid(i, j):
            if i < 0 or i == len(self.board) or j < 0 or j == len(self.board[0]):
                return False
            if (i, j) in self.visited:  # NOTE: if this is a dict, then also check the value
                return False
            return True

        if self.board[i][j] not in node.m:
            return

        temp = node.m[self.board[i][j]]

        if temp.end:
            self.res.add(temp.word)

        self.visited.add((i, j))
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if valid(i+dx, j+dy):
                self.check(temp, i+dx, j+dy)
        self.visited.remove((i, j))

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []
        self.board = board

        def build_trie(words, node):
            for word in words:
                cur = node
                for c in word:
                    if c not in cur.m:
                        cur.m[c] = Node()
                        cur.m[c].word = cur.word + c
                    cur = cur.m[c]
                cur.end = True

        build_trie(words, self.trie)  # node.end for node.word

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.check(self.trie, i, j)
        return list(self.res)

