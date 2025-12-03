import time
import statistics
import graph_creation
import algorithm

result = open('result.csv', 'w')

result.write("Vert,Dens,Min(ms),Max(ms),Average(ms),Standard deviation(ms)\n")

max_vertices, min_vertices, step_vertices = 200, 20, 10
num1 = int((max_vertices - min_vertices) / step_vertices)

max_density, min_density, step_density = 100, 60, 10
num2 = int((max_density - min_density) / step_density)


vertices = min_vertices
density = min_density
for x in range(num1 + 1):
    for y in range(num2 + 1):
        time_lst = []
        for z in range(20):
            V = graph_creation.create_graph(vertices, density)
            start = time.perf_counter()

            algorithm.algorithm(V)

            end = time.perf_counter()
            consumed_time = end - start
            time_lst.append(consumed_time)

        average = statistics.mean(time_lst)
        standard_deviation = statistics.stdev(time_lst)
        result.write(
            f"{vertices},{density},{min(time_lst) * 1000:.3f},{max(time_lst) * 1000:.3f},{average * 1000:.3f},{standard_deviation * 1000:.3f}\n")
        density += step_density
    vertices += step_vertices
    density = min_density

result.close()
