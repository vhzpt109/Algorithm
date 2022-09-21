import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())

    minheap = []
    maxheap = []
    for _ in range(n):
        x = int(sys.stdin.readline().rstrip())

        if len(minheap) == len(maxheap):
            heapq.heappush(minheap, -x)
        else:
            heapq.heappush(maxheap, x)

        if maxheap and maxheap[0] < -minheap[0]:
            minValue = heapq.heappop(minheap)
            maxValue = heapq.heappop(maxheap)

            heapq.heappush(minheap, -maxValue)
            heapq.heappush(maxheap, -minValue)

        print(-minheap[0])