class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edgemap = { i: [] for i in range(1, n + 1)}
        for time in times:
            edgemap[time[0]].append((time[1], time[2]))

        maxtime = 0
        pq = []
        heapq.heappush(pq, (0, k))
        visited = set()
        while pq:
            time, curr = heapq.heappop(pq)
            if curr in visited:
                continue

            visited.add(curr)
            maxtime = time

            if len(visited) == n:
                break

            for nextcurr, weight in edgemap[curr]:
                heapq.heappush(pq, (time + weight, nextcurr))

            print(pq)

        return maxtime if len(visited) == n else -1