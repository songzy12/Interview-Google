# https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/366/
class Solution:

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        from collections import defaultdict

        father = defaultdict(list)

        # we need to count undirected degree to find out circle
        degree = defaultdict(int)
        neigh = defaultdict(set)

        nodes = set()

        candidates = []
        order = {}

        for o, (u, v) in enumerate(edges):
            nodes.add(u)
            nodes.add(v)
            degree[v] += 1
            degree[u] += 1

            order[u, v] = o

            neigh[u].add(v)
            neigh[v].add(u)

            father[v].append(u)  # NOTE: in reverse order
            if len(father[v]) == 2:
                candidates = [(x, v) for x in father[v]]

        # we find out the nodes in circle
        visited = set()

        queue = []
        for t in list(nodes):
            if degree[t] == 1:
                queue.append(t)
                nodes.remove(t)

        while queue:
            cur = queue.pop()
            visited.add(cur)
            for s in neigh[cur]:
                degree[s] -= 1
                neigh[s].remove(cur)
                if degree[s] == 1:
                    queue.append(s)
        # if a node is not visited, then it is in circle
        # print(candidates)
        # print(visited)
        for u, v in candidates[::-1]:
            if u not in visited and v not in visited:
                return [u, v]

        # now no node has two fathers, so we find the last one in circle

        head = nodes.pop()
        cur = neigh[head].pop()
        neigh[cur].remove(head)

        if (cur, head) in order:
            res = [cur, head]
            max_order = order[cur, head]
        else:
            res = [head, cur]
            max_order = order[head, cur]

        while neigh[cur]:
            next_ = neigh[cur].pop()
            neigh[next_].remove(cur)
            if (cur, next_) in order and order[cur, next_] > max_order:
                max_order = order[cur, next_]
                res = [cur, next_]
            if (next_, cur) in order and order[next_, cur] > max_order:
                max_order = order[next_, cur]
                res = [next_, cur]
            cur = next_
        return res


edges = [[4,2],[1,5],[5,2],[5,3],[2,4]]
print(Solution().findRedundantDirectedConnection(edges))

# 1. there must be a circle
# 2. there may be one node has two fathers

# if there is one node has two fathers
#    remove the edge comes later
# else
#   remove the last edge forms the circle

# to find the one with two father is simple
# to find the edges in the circle, use degree
