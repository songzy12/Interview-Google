# https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/331/

class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict
        edge = defaultdict(dict)

        for i in range(len(equations)):
            u, v = equations[i]
            w = values[i]
            edge[u][v] = w
            edge[v][u] = 1 / w # NOTE: there may be invert edge
        
        def solve(head, tail, edge):
            if head not in edge: # NOTE: not defined
                return -1.
            queue = [(head, 1.)]
            visited = set([head])
            while queue:
                cur, prod = queue.pop(0)
                if cur == tail:
                    return prod
                for next in edge[cur]:
                    if next in visited:
                        continue
                    visited.add(next)
                    queue.append((next, edge[cur][next] * prod))
            return -1.
        
        result = []
        for query in queries:
            head, tail = query
            temp = solve(head, tail, edge)
            if temp != -1:
                result.append(temp)
            else:
                result.append(1. / solve(tail, head, edge))
        return result