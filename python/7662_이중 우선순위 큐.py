import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        maxheap = []
        minheap = []
        delete_list = [False] * k
        for id in range(k):
            command, n = map(str, input().split())
            n = int(n)

            if command == "I":
                heapq.heappush(maxheap, (-n, id))
                heapq.heappush(minheap, (n, id))
                delete_list[id] = True
            elif command == "D":
                if n == 1:
                    while maxheap and not delete_list[maxheap[0][1]]:
                        heapq.heappop(maxheap)
                    if maxheap:
                        delete_list[heapq.heappop(maxheap)[1]] = False
                elif n == -1:
                    while minheap and not delete_list[minheap[0][1]]:
                        heapq.heappop(minheap)
                    if minheap:
                        delete_list[heapq.heappop(minheap)[1]] = False

        while maxheap and not delete_list[maxheap[0][1]]:
            heapq.heappop(maxheap)
        while minheap and not delete_list[minheap[0][1]]:
            heapq.heappop(minheap)

        if not maxheap or not minheap:
            print("EMPTY")
        else:
            print(-heapq.heappop(maxheap)[0], heapq.heappop(minheap)[0])