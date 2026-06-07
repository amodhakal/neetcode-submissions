class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_prereqs = [[] for i in range(numCourses)]
        valid_courses = []

        for prereq in prerequisites:
            first, second = prereq
            course_prereqs[first].append(second)

        cycle, visited = set(), set()

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)

            for prereq in course_prereqs[course]:
                result = dfs(prereq)
                if not result:
                    return False

            cycle.remove(course)
            visited.add(course)
            
            return True

        for course in range(numCourses):
            result = dfs(course)
            if not result:
                return []
            
            valid_courses.append(course)

        return valid_courses