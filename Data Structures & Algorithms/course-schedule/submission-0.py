class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # key: num; val: list

        degree = [0 for i in range(numCourses)]
        # initialize in-degree of every course to 0

        for i, j in prerequisites:
            graph[j].append(i)
            degree[i] += 1
        
        queue = deque()
        res = [] # record the courses that already taken

        for course in range(numCourses):
            if degree[course] == 0:
                # add courses that has 0 in-degree into queue b/c they are the start points
                queue.append(course)
                res.append(course)

        while len(queue) > 0:
            curr = queue.popleft()
            for next in graph[curr]:
                degree[next] -= 1
                if degree[next] == 0:
                    queue.append(next)
                    res.append(next)

        return len(res) == numCourses # no course left



