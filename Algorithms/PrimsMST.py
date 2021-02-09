def PrimsMST(g):
    num_of_vertices = len(g)
    start_node = 0
    visited_nodes = [start_node]
    included_edges = []
    cost = 0
    for _ in range(num_of_vertices - 1):
        minimum = g[start_node][0]
        for i in visited_nodes:
            for j in range(num_of_vertices):
                if g[i][j] < minimum and j not in visited_nodes:
                    minimum = g[i][j]
                    x = i
                    y = j
        if y not in visited_nodes:
            visited_nodes.append(y)
            g[x][y] = float('inf')
            g[y][x] = float('inf')
            cost += minimum
            included_edges.append([x, y])
    return f"The minimum cost is {cost} and the included edges (starting from vertex 0) are {included_edges}"


graph1 = [[float('inf'), 28, float('inf'), float('inf'), float('inf'), 10, float('inf')],
          [28, float('inf'), 16, float('inf'), float('inf'), float('inf'), 14],
          [float('inf'), 16, float('inf'), 12, float('inf'), float('inf'), float('inf')],
          [float('inf'), float('inf'), 12, float('inf'), 22, float('inf'), 18],
          [float('inf'), float('inf'), float('inf'), 22, float('inf'), 25, 24],
          [10, float('inf'), float('inf'), float('inf'), 25, float('inf'), float('inf')],
          [float('inf'), 14, float('inf'), 18, 24, float('inf'), float('inf')]]
graph2 = [[float('inf'), 2, float('inf'), 6, float('inf')],
          [2, float('inf'), 3, 8, 5],
          [float('inf'), 3, float('inf'), float('inf'), 7],
          [6, 8, float('inf'), float('inf'), 9],
          [float('inf'), 5, 7, 9, float('inf')]]
graph3 = [[float('inf'), 12, float('inf'), 25, float('inf')],
          [12, float('inf'), 11, 8, 12],
          [float('inf'), 11, float('inf'), float('inf'), 17],
          [25, 8, float('inf'), float('inf'), 15],
          [float('inf'), 12, 17, 15, float('inf')]]
graph4 = [[float('inf'), 1, 8, 1, 4],
          [1, float('inf'), 12, 4, 9],
          [8, 12, float('inf'), 7, 3],
          [1, 4, 7, float('inf'), 2],
          [4, 9, 3, 2, float('inf')]]
graph1_copy = graph1.copy()
graph2_copy = graph2.copy()
graph3_copy = graph3.copy()
# print(PrimsMST(graph1_copy))
# print(PrimsMST(graph2_copy))
print(PrimsMST(graph4))
