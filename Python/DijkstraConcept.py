import heapq
from collections import defaultdict
def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    #Problem #743 Network Delay Time - Medium 

    adjacentVertex = defaultdict(list)

    for source, destination, weight in times:
        adjacentVertex[source].append([destination, weight])

    shortestPath = {} 
    minHeap = [[0, k]]    
    
    while minHeap:
        weight0, node0 = heapq.heappop(minHeap)
        
        if node0 in shortestPath:
            continue

        shortestPath[node0] = weight0

        for node1, weight1 in adjacentVertex[node0]:
            if node1 not in shortestPath:
                heapq.heappush(minHeap, [weight0 + weight1, node1])

    if len(shortestPath) == n:
        return max(shortestPath.values())
    else: 
        return -1
    
def shortestPath(n: int, edges: list[list[int]], src: int) -> dict[int, int]:
    adj = {}
    for i in range(n):
        adj[i] = []
    
    for s, d, weight in edges:
        adj[s].append([d, weight])
    print(adj)

    shortest = {} # Map vertex -> dist of shortest path
    minHeap = [[0, src]]

    while minHeap:
        weight1, node1 = heapq.heappop(minHeap)
        print(f'weight1: {weight1} node1: {node1}')
        if node1 in shortest:
            continue
        
        shortest[node1] = weight1
        print(f'shortest: {shortest}')
        for node2, weight2 in adj[node1]:
            print(f'node2: {node2} weight2: {weight2}')
            if node2 not in shortest:
                heapq.heappush(minHeap, [weight1 + weight2, node2])
            print(f'minHeap{minHeap}')
            print(f'minHeap top: {minHeap[0]}')

    return shortest

if __name__ == "__main__":
    n = 5
    edges = [[1, 2, 1]]
    src = 0

    print(networkDelayTime(edges, 2, 2))