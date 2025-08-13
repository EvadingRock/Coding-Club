vertices_amount, edges_amount = input().split()

graph_list = [[] for _ in range(int(vertices_amount))]

for _ in range(int(edges_amount)):
    point_1, point_2, weight = (int(x) for x in input().split())

    point_1 -= 1
    point_2 -= 1

    graph_list[point_1].append([point_2, weight])
    graph_list[point_2].append([point_1, weight])


def use_weight(pair):
    return pair[1]


for p in range(int(vertices_amount)):
    graph_list[p].sort(key=use_weight)

point_estimates = [float("inf") for _ in range(int(vertices_amount))]
point_estimates[0] = 0

queue = [[0, 0, -1]]

while len(queue) != 0:
    point, estimate, prev_point = queue[0]
    queue.pop(0)

    for p in range(len(graph_list[point])):
        path = graph_list[point][p]

        if path[1] + estimate < point_estimates[path[0]]:
            point_estimates[path[0]] = path[1] + estimate
            queue.append([path[0], path[1] + estimate, point])


for e in point_estimates:
    if e == float("inf"):
        print(-1)
    else:
        print(e)
