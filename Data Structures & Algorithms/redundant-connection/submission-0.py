class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)

        for src, dst in edges:
            if len(adjlist[dst]) >= 1:
                return [src, dst]

            adjlist[dst].append(src)

        print(adjlist)
        return []

