class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []

        for i in range(len(stones)):
            heapq.heappush(max_heap, -stones[i])
        
        while len(max_heap)>1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if x<y:
                heapq.heappush(max_heap, -(y-x))
        
        if max_heap:
            return abs(max_heap[0])
        
        return 0

        