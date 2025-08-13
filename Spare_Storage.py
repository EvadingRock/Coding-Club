# dict-carry with-dict approach

# stu_count = int(input())
# gift_graph = [{}]
# rev_graph = [[] for _ in range(stu_count + 1)]
#
# # total_calls = 0
#
# for s in range(stu_count):
#     can_gift = {int(x): int(x) for x in input().split()[1:]}
#     gift_graph.append(can_gift)
#
#     for x in can_gift:
#         rev_graph[x].append(s + 1)
#
#
# def node_ify(value):
#     if type(value) is list:
#         return value[0]
#     return value
#
#
# def copy(array):
#     return [dict(dic) for dic in array]
#
#
# def assign(current, graph, remaining, entry):
#     # global total_calls
#     #
#     # print(f"{total_calls}")
#     # total_calls += 1
#     # print(remaining)
#     n_current = node_ify(current)
#
#     for path in graph[n_current]:
#         new_graph = copy(graph)
#         for r in rev_graph[path]:
#             new_graph[r].pop(path)
#
#         new_remaining = remaining[:]
#
#         if path == entry:
#             new_remaining.remove(path)
#
#             if len(new_remaining) == 0:
#                 return [path]
#
#             calc_val = assign([new_remaining[0]], new_graph, new_remaining, new_remaining[0])
#             if calc_val is not None:
#                 return [path, [new_remaining[0]]] + calc_val
#
#             continue
#
#         new_remaining.remove(path)
#
#         if len(new_remaining) == 0:
#             continue
#
#         calc_val = assign(path, new_graph, new_remaining, entry)
#         if calc_val is not None:
#             return [path] + calc_val
#
#
# computed = [1] + assign([1], gift_graph[:], list(range(1, stu_count + 1)), 1)
# # print(computed)
#
# final_gifts = [0] * (stu_count + 1)
# for n in range(len(computed) - 1):
#     if type(computed[n]) is list:
#         final_gifts[computed[n][0]] = computed[n + 1]
#     elif type(computed[n + 1]) is not list:
#         final_gifts[computed[n]] = computed[n + 1]
#
# final_gifts.pop(0)
# print(" ".join([str(x) for x in final_gifts]))


# # dict-carry non-dict approach
#
# stu_count = int(input())
# gift_graph = [[]]
# rev_graph = [[] for _ in range(stu_count + 1)]
#
# # total_calls = 0
#
# for s in range(stu_count):
#     can_gift = [int(x) for x in input().split()]
#     can_gift.pop(0)
#     gift_graph.append(can_gift)
#
#     for x in can_gift:
#         rev_graph[x].append(s + 1)
#
#
# def node_ify(value):
#     if type(value) is list:
#         return value[0]
#     return value
#
#
# def copy(array):
#     return [li[:] for li in array]
#
#
# def assign(current, graph, remaining, entry):
#     # global total_calls
#     #
#     # print(f"{total_calls}")
#     # total_calls += 1
#     # print(remaining)
#     n_current = node_ify(current)
#
#     for path in graph[n_current]:
#         new_graph = copy(graph)
#         for r in rev_graph[path]:
#             new_graph[r].remove(path)
#
#         new_remaining = remaining[:]
#
#         if path == entry:
#             new_remaining.remove(path)
#
#             if len(new_remaining) == 0:
#                 return [path]
#
#             calc_val = assign([new_remaining[0]], new_graph, new_remaining, new_remaining[0])
#             if calc_val is not None:
#                 return [path, [new_remaining[0]]] + calc_val
#
#             continue
#
#         new_remaining.remove(path)
#
#         if len(new_remaining) == 0:
#             continue
#
#         calc_val = assign(path, new_graph, new_remaining, entry)
#         if calc_val is not None:
#             return [path] + calc_val
#
#
# computed = [1] + assign([1], gift_graph[:], list(range(1, stu_count + 1)), 1)
# # print(computed)
#
# final_gifts = [0] * (stu_count + 1)
# for n in range(len(computed) - 1):
#     if type(computed[n]) is list:
#         final_gifts[computed[n][0]] = computed[n + 1]
#     elif type(computed[n + 1]) is not list:
#         final_gifts[computed[n]] = computed[n + 1]
#
# final_gifts.pop(0)
# print(" ".join([str(x) for x in final_gifts]))


# # Visited non-dict approach

# stu_count = int(input())
# gift_graph = [[] for _ in range(stu_count + 1)]
#
# total_calls = 0
#
# for s in range(stu_count):
#     can_gift = [int(x) for x in input().split()]
#     can_gift.pop(0)
#     gift_graph[s + 1] = can_gift
#
#
# def find_rem(history, array):
#     for node in array:
#         if node not in history:
#             return node
#     return True
#
#
# def node_ify(value):
#     if type(value) is list:
#         return value[0]
#     return value
#
#
# def assign(visited, entry):
#     global total_calls
#
#     print(f"{total_calls}")
#     total_calls += 1
#     # print(visited)
#     for path in gift_graph[node_ify(visited[-1])]:
#         if path in visited:
#             continue
#
#         new_visited = visited[:]
#
#         if path == entry:
#             new_visited.append(path)
#
#             leap_to = find_rem(new_visited, list(range(1, stu_count + 1)))
#             if leap_to is True:
#                 return new_visited
#             else:
#                 new_visited.append([leap_to])
#
#             calc_val = assign(new_visited, leap_to)
#             if calc_val is not None:
#                 return calc_val
#
#             continue
#
#         new_visited.append(path)
#         calc_val = assign(new_visited, entry)
#         if calc_val is not None:
#             return calc_val
#
#
# computed = assign([[1]], 1)
# # print(computed)
#
# final_gifts = [0] * (stu_count + 1)
# for n in range(len(computed) - 1):
#     if type(computed[n]) is list:
#         final_gifts[computed[n][0]] = computed[n + 1]
#     elif type(computed[n + 1]) is not list:
#         final_gifts[computed[n]] = computed[n + 1]
#
# final_gifts.pop(0)
# print(" ".join([str(x) for x in final_gifts]))

# [[1], 2, 3, 8, 1, [4], 6, 7, 4, [5], 9, 5, [10], 22, 23, 13, 19, 12, 20, 15


# stu_count = int(input())
# gift_graph = {}
#
# for s in range(stu_count):
#     can_gift = [int(x) for x in input().split()]
#     can_gift.pop(0)
#     gift_graph[s + 1] = can_gift
#
#
# def find_entry(array):
#     for i in range(len(array) - 1, -1, -1):
#         if type(array[i]) is list:
#             return array[i][0]
#
#
# def find_rem(history, array):
#     for node in range(len(array)):
#         if type(array[node]) is not list:
#             if array[node] not in history:
#                 if node == len(array) - 1:
#                     return False
#                 return array[node]
#     return True
#
#
# def node_ify(value):
#     if type(value) is list:
#         value = value[0]
#     return value
#
#
# def assign(visited):
#     print(visited)
#     for path in gift_graph[node_ify(visited[-1])]:
#         if path in visited:
#             continue
#
#         new_visited = visited[:]
#
#         if path == find_entry(visited):
#             new_visited.append(path)
#
#             leap_to = find_rem(new_visited, list(range(1, stu_count + 1)))
#             if leap_to is False:
#                 return
#             elif leap_to is True:
#                 return new_visited
#             else:
#                 new_visited.append([leap_to])
#
#             calc_val = assign(new_visited)
#             if calc_val is not None:
#                 return calc_val
#
#             continue
#
#         new_visited.append(path)
#         calc_val = assign(new_visited)
#         if calc_val is not None:
#             return calc_val
#
#
# computed = assign([[1]])
# # print(computed)
#
# final_gifts = [0] * (stu_count + 1)
# for n in range(len(computed) - 1):
#     if type(computed[n]) is list:
#         final_gifts[computed[n][0]] = computed[n + 1]
#     elif type(computed[n + 1]) is not list:
#         final_gifts[computed[n]] = computed[n + 1]
#
# final_gifts.pop(0)
# print(" ".join([str(x) for x in final_gifts]))
#
# # [[1], 2, 3, 8, 1, [4], 6, 7, 4, [5], 9, 5, [10], 22, 23, 13, 19, 12, 20, 15, 16, 30, 24
