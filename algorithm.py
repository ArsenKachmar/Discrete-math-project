def algorithm(matrix):
    vertices_number = len(matrix)
    for k in range(vertices_number):
        for i in range(vertices_number):
            for j in range(vertices_number):
                d = matrix[i][k] + matrix[k][j]
                if matrix[i][j] > d:
                    matrix[i][j] = d
                if matrix[i][j] < 0:
                    raise ValueError("The path cannot be smaller than 0")
