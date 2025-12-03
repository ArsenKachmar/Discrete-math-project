import random


def create_graph(n_vertices, density, weight_range=(1, 10)):
    max_possible_edges = n_vertices * (n_vertices - 1) // 2
    required_edges = int(density / 100 * max_possible_edges)

    matrix = [[float('inf') for _ in range(n_vertices)] for _ in range(n_vertices)]

    for i in range(n_vertices):
        matrix[i][i] = 0

    possible_edges = []
    for i in range(n_vertices):
        for j in range(i + 1, n_vertices):
            possible_edges.append((i, j))

    selected_edges = random.sample(possible_edges, min(required_edges, len(possible_edges)))

    for i, j in selected_edges:
        weight = random.randint(weight_range[0], weight_range[1])
        matrix[i][j] = weight
        matrix[j][i] = weight

    return matrix