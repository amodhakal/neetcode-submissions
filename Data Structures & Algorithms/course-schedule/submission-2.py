class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cps = {i:[] for i in range(numCourses)}

        for prereq in prerequisites:
            first, second = prereq
            cps[first].append(second)


        visit, cycle = set(), set()
        def dfs(idx):
            if idx in cycle:
                return False

            if idx in visit:
                return True

            cycle.add(idx)
            visit.add(idx)
            for course in cps[idx]:
                result = dfs(course)
                if not result:
                    return False

            cycle.remove(idx)

            return True

        
        for idx in range(numCourses):
            result = dfs(idx)
            if not result:
                return False


        return True