from graph_creation2 import lst

def floyd(v):
    m = len(v)
    dist = [row[:] for row in v]
    p = [[None for _ in range(m)] for _ in range(m)]

    for k in range(m):
        for i in range(m):
            for j in range(m):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    p[i][j] = k

    return dist, p


for graph in lst:
    dist, p = floyd(graph)
    print(dist)