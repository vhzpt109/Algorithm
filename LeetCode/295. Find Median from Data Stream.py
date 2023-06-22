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
            heapq.heappush(self.maxHeap, -pop_num)

        elif len(self.minHeap) + 1 < len(self.maxHeap):
            pop_num = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, pop_num)

    def findMedian(self) -> float:
        if len(self.minHeap) < len(self.maxHeap):
            small_med = -1 * self.maxHeap[0]
            return small_med
        elif len(self.maxHeap) < len(self.minHeap):
            large_med = self.minHeap[0]
            return large_med
        else:
            small_med = -1 * self.maxHeap[0]
            large_med = self.minHeap[0]
            med = (small_med + large_med) / 2
            return med


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
