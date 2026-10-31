import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 1,
    'D': 2,
    'E': 0
}

start = 'A'
goal = 'E'

queue = [(heuristic[start], start)]
visited = set()

while queue:
    h, node = heapq.heappop(queue)
    print(node, end=" ")

    if node == goal:
        print("\nGoal found")
        break

    if node not in visited:
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    queue, (heuristic[neighbor], neighbor)
                )
