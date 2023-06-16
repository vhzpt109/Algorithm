import heapq


class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        median = self.findMedian()
        if median < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) + 1 < len(self.minHeap):
            pop_num = heapq.heappop(self.minHeap)
            heapq.heappush(self._maxHeap, -pop_num)

        elif len(self.minHeap) + 1 < len(self.maxHeap):
            pop_num = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, pop_num)

    def findMedian(self) -> float:
        pass


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
