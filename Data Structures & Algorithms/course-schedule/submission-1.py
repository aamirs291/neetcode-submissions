class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # b - source
        # a - dest

        adj_list = {}
        in_degree = [0 for i in range(numCourses)]

        for src in range(numCourses):
            adj_list[src] = adj_list.get(src, [])

        for prereq in prerequisites:
            source = prereq[1]
            dest = prereq[0]

            adj_list[source].append(dest)

            in_degree[dest]+=1

        q = deque()

        for i in range(len(in_degree)):
            if in_degree[i]==0:
                q.append(i)

        count = 0
        while q:
            currNode = q.popleft()
            count+=1
            neighbors = adj_list[currNode]

            for neighbor in neighbors:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    q.append(neighbor)
        

        return count==numCourses


        

        