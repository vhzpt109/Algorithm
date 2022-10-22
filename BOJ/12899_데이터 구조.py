import sys
import heapq

input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    heap = []
    count = 0
    for _ in range(n):
        t, x = map(int, input().split())
        if t == 1:
            heapq.heappush(heap, x)
        else:
            value = heapq.nsmallest(x, heap)[x - 1]
            print(value)
            heap.remove(value)