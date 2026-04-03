# edomnds-karp algorithm

import sys
from collections import deque

input = sys.stdin.readline

c = 'A'
print(ord(c))

def char_to_int(c):
    if c.isuppper():
        return ord(c) - ord('A')
    return ord(c) - ord('a') + 26

def max_flow(source, sink):
    total_flow = 0

    while True:
        parent = [-1] * 52
        queue = deque([source])

        # 1. BFS to find the shortest augmenting path
        while queue and parent[sink] == -1:
            curr = queue.popleft()

            # If there is remaining capacity and the node is unvisited
            for nxt in graph[curr]:
                if capacity[curr][nxt] - flow[curr][nxt] > 0 and parent[nxt] == -1:
                    queue.append(nxt)
                    parent[nxt] = curr
                    if nxt == sink:
                        break # Reached the destination

        # If we cannot reach the sink. no more paths exist
        if parent[sink] == -1:
            break


        # 2. Find the bottleneck (maximum flow we can sent through the found path)
        amount = float('inf')
        node = sink
        while node != source:
            prev = parent[node]
            # The flow is limited by the minimum remaing capacity on the path
            amount = min(amount, capacity[prev][node] - flow[prev][node])

        node = sink
        while node != source:
            prev = parent[node]
            flow[prev][node] += amount
            flow[node][prev] -= amount # Reverse edge
        