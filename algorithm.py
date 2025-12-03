def algorithm(V):
    N = len(V)
    P = [[v for v in range(N)] for u in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = V[i][k] + V[k][j]
                if V[i][j] > d:
                    V[i][j] = d
                    P[i][j] = k