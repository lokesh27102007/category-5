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
    'E': 1,
    'F': 1,
    'G': 5
}

def ao_star(node):
    if not graph[node]:
        return cost[node]

    best = float('inf')

    for option in graph[node]:
        total = sum(ao_star(child) for child in option)
        best = min(best, total)

    return best

print("Minimum cost:", ao_star('A'))
