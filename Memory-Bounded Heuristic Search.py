import heapq

graph = {
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 2)],
    'C': [('E', 2)],
    'D': [],
    'E': []
}

heuristic = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0,
    'E': 0
}

queue = [(heuristic['A'], 'A')]
memory_limit = 2
visited = set()

while queue:
    h, node = heapq.heappop(queue)

    if node in visited:
        continue

    visited.add(node)
    print(node, end=" ")

    if node == 'E':
        print("\nGoal found")
        break

    for neighbor, cost in graph[node]:
        if neighbor not in visited:
            heapq.heappush(
                queue, (cost + heuristic[neighbor], neighbor)
            )

    if len(queue) > memory_limit:
        queue = heapq.nsmallest(memory_limit, queue)
        heapq.heapify(queue)
