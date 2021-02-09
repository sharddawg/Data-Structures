def BFS(g, s):
    n = len(g)
    bfs = [s]
    queue = [s]
    i = 0
    for _ in range(n - 1):
        to_be_explored = queue[i]
        potential_vertices = g[to_be_explored]
        for j in potential_vertices:
            if j not in bfs:
                bfs.append(j)
            if j not in queue:
                queue.append(j)
        i += 1
    return f"The order for Breadth first search is {bfs}"


# graph1 = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
graph2 = {1: [2, 4], 2: [5, 7, 8, 3], 3: [2, 4, 9, 10], 4: [1, 3], 5: [2, 7, 8, 6], 6: [5], 7: [2, 5, 8], 8: [2, 5, 7]}
start = int(input("What vertex do you want to start from? - "))
print(BFS(graph2, 1))
