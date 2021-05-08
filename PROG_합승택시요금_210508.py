import heapq
from collections import defaultdict


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return distances

def solution(n, s, a, b, fares):
    graph = defaultdict(dict)
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
    start_distances = dijkstra(graph,s)
    min_distances = start_distances[a] + start_distances[b]
    for i in range(n):
        middle_distances = dijkstra(graph,i+1)
        distance = start_distances.get(i+1,float('inf')) + middle_distances[a] + middle_distances[b]
        min_distances = min(min_distances,distance)
    answer = min_distances
    return answer