import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        maxheap = []
        minheap = []
        for _ in range(k):
            command, n = map(str, input().split())
            n = int(n)

            if command == "I":
                heapq.heappush(maxheap, (n, n))
                heapq.heappush(minheap, (-n, n))
            elif command == "D":
                if n == 1:
                    heapq.heappop(maxheap)
                else:
                    heapq.heappop(minheap)

        if not maxheap or not minheap:
            print("EMPTY")
        else:
            print(heapq.heappop(maxheap)[0], heapq.heappop(minheap)[0])