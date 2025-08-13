stu_count = int(input())
old_graph = [[] for _ in range(stu_count)]

for s in range(stu_count):
    can_gift = [int(x) for x in input().split()]
    can_gift.pop(0)
    old_graph[s] = [s + 1, can_gift]


def heur_sort(val):
    return len(val[1])


sorted_graph = sorted(old_graph, key=heur_sort)
rev_sorted_graph = [0] * (stu_count + 1)


def finder(val):
    for x in range(len(sorted_graph)):
        if sorted_graph[x][0] == val:
            return x


for s in range(1, stu_count + 1):
    rev_sorted_graph[s] = finder(s)


def sorted_sort(val):
    return rev_sorted_graph[val]


gift_graph = {}

for s in sorted_graph:
    gift_graph[s[0]] = sorted(s[1], key=sorted_sort)

check_list = [s[0] for s in sorted_graph]


def find_rem(history):
    for node in check_list:
        if node not in history:
            return node
    return True


def node_ify(di):
    value = list(di.keys())[-1]
    if type(value) is str:
        return int(value)
    return value


def assign(visited, entry):
    for path in gift_graph[node_ify(visited)]:
        if path in visited:
            continue

        new_visited = dict(visited)

        if path == entry:
            new_visited[path] = path

            leap_to = find_rem(new_visited)
            if leap_to is True:
                return new_visited
            else:
                new_visited[str(leap_to)] = leap_to

            calc_val = assign(new_visited, leap_to)
            if calc_val is not None:
                return calc_val

            continue

        new_visited[path] = path
        calc_val = assign(new_visited, entry)
        if calc_val is not None:
            return calc_val


start = sorted_graph[0][0]
computed = list(assign({str(start): str(start)}, start))

final_gifts = [0] * (stu_count + 1)
for n in range(len(computed) - 1):
    if type(computed[n]) is str:
        final_gifts[int(computed[n])] = computed[n + 1]
    elif type(computed[n + 1]) is not str:
        final_gifts[computed[n]] = computed[n + 1]

final_gifts.pop(0)
print(" ".join([str(x) for x in final_gifts]))
