def algorithm(matrix):
    vertices_number = len(matrix)
    previous_matrix = [[v for v in range(vertices_number)] for u in range(vertices_number)]

    for k in range(vertices_number):
        for i in range(vertices_number):
            for j in range(vertices_number):
                d = matrix[i][k] + matrix[k][j]
                if matrix[i][j] > d:
                    matrix[i][j] = d
                    previous_matrix[i][j] = k
