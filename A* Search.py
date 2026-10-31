import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

queue = [(heuristic['A'], 0, 'A')]
visited = set()

while queue:
    f, cost, node = heapq.heappop(queue)

    if node in visited:
        continue

    visited.add(node)
    print(node, end=" ")

    if node == 'D':
        print("\nMinimum cost:", cost)
        break

    for neighbor, weight in graph[node]:
        new_cost = cost + weight

        if neighbor not in visited:
            new_f = new_cost + heuristic[neighbor]
            heapq.heappush(
                queue, (new_f, new_cost, neighbor)
            )
