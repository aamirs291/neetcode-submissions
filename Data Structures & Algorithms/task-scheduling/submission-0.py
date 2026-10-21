class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq_map = {}

        for i in tasks:
            freq_map[i] = freq_map.get(i,0) + 1
        
        max_heap = [-count for count in freq_map.values()]
        heapq.heapify(max_heap)
        q = deque()

        time = 0
        while max_heap or q:
            time+=1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append([count, time+n])
            
            if q and q[0][1]==time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time



