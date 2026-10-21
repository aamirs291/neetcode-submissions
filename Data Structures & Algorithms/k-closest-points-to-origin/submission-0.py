class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        res = []
        for i in points:
            val = i[0]**2 + i[1]**2
            heapq.heappush(minHeap, (val, i))
        
        while k:
            point = heapq.heappop(minHeap)[1]
            res.append(point)
            k-=1
        
        print(res)
        return res

        