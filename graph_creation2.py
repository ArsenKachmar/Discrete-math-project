import random

lst = []

def create_graph(weight_range=(1, 10)):
    n_vertices = int(input("Enter the quantity of vertexes: "))
    density = float(input("Enter graph density (1 - 100): "))
    max_possible_edges = n_vertices * (n_vertices - 1) // 2
    required_edges = int(density / 100 * max_possible_edges)

    matrix = [[float('inf') for _ in range(n_vertices)] for _ in range(n_vertices)]

    for i in range(n_vertices):
        matrix[i][i] = 0

    possible_edges = [(i, j) for i in range(n_vertices) for j in range(i+1, n_vertices)]
    selected_edges = random.sample(possible_edges, min(required_edges, len(possible_edges)))

    for i, j in selected_edges:
        weight = random.randint(*weight_range)
        matrix[i][j] = weight
        matrix[j][i] = weight

    lst.append(matrix)

if True:
    for i in range(3):
        create_graph()
    print(lst)