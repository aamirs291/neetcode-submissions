class MedianFinder:

    def __init__(self):

        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        
        if not self.max_heap or num < -1 * (self.max_heap[0]):
            heapq.heappush(self.max_heap, -1 * num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            pop_value = -1 * (heapq.heappop(self.max_heap))
            heapq.heappush(self.min_heap, pop_value)
        
        elif len(self.min_heap) > len(self.max_heap) + 1:
            pop_value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * pop_value)

    def findMedian(self) -> float:

        if len(self.max_heap) == len(self.min_heap):
            self.max_heap_val = -1 * self.max_heap[0]
            self.min_heap_val = self.min_heap[0]

            return (self.min_heap_val + self.max_heap_val)/2
        
        elif len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]

        else:
            return self.min_heap[0]
        