class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = {}

        q = deque()

        # b - source
        # a - dest

        in_degree = [0 for i in range(numCourses)]

        for i in range(numCourses):
            adj_list[i] = adj_list.get(i, [])

        for prereq in prerequisites:
            source = prereq[1]
            dest = prereq[0]

            in_degree[dest]+=1
            adj_list[source].append(dest)


        for i in range(len(in_degree)):
            if in_degree[i]==0:
                q.append(i)
        
        res = []
        count = 0
        while q:
            currNode = q.popleft()
            count+=1
            res.append(currNode)

            neighbors = adj_list[currNode]

            for neighbor in neighbors:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    q.append(neighbor)

        
        if count==numCourses:
            return res
        else:
            return []

        