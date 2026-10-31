# AND-OR graph example

graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E']],
    'C': [['F']],
    'D': [['G']],
    'E': [],
    'F': [],
    'G': []
}

cost = {
    'B': 2, 'C': 2, 'D': 5,
    'E': 1, 'F': 1, 'G': 1
}

def ao_star(node):
    if not graph[node]:
        return cost.get(node, 0)

    best_cost = float('inf')

    for option in graph[node]:
        total = 0

        for child in option:
            total += cost.get(child, 0) + ao_star(child)

        best_cost = min(best_cost, total)

    return best_cost

print("Minimum cost:", ao_star('A'))
