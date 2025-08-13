# Dimethyl_benzene
# November 9th

a, b = input().split()
atom_max, pair_len = int(a), int(b)

atom_pairs = []
depth_nodes = []

for x in range(atom_max):
    atom_pairs.append([])
    depth_nodes.append([])

for x in range(pair_len):
    num_1, num_2 = input().split()
    atom_pairs[int(num_1) - 1].append(int(num_2) - 1)
    atom_pairs[int(num_2) - 1].append(int(num_1) - 1)

answer = 0
starting_node = 0
his_node = [0, 0, 0, 0, 0]


def cycle_search(depth, node):
    global answer
    global atom_pairs
    global starting_node
    global his_node

    if depth < 5:
        if node == starting_node and depth != 0:
            pass

        else:
            to_scan = atom_pairs[node]

            for path in to_scan:
                if his_node[depth] != path:

                    his_node[depth] = path
                    cycle_search(depth + 1, path)

    elif depth == 5 and node == starting_node:
        if len(set(his_node)) == 5:
            answer = 1


for x in range(atom_max):
    starting_node = x
    cycle_search(0, 0)

if answer == 1:
    print("YES")
else:
    print("NO")
