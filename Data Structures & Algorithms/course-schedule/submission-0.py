class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = [[] for i in range(numCourses)]
        in_degree = [0 for i in range(numCourses)]

        for dest, src in prerequisites:
            in_degree[dest]+=1
            #adj_list[src] = adj_list.get(src, [])
            adj_list[src].append(dest)
        
        # print(in_degree)
        # print(adj_list)

        q = deque()

        for i in range(numCourses):
            if in_degree[i]==0:
                q.append(i)
        
        course_count = 0
        while q:
            currNode = q.popleft();
            course_count+=1

            for child in adj_list[currNode]:
                in_degree[child]-=1
                if in_degree[child]==0:
                    q.append(child)
        
        if course_count ==numCourses:
            return True
        
        return False



