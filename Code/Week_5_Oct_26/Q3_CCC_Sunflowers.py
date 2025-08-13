dim = int(input())
table = []

for x in range(dim):
    table.append(input().split())

hoz = int(table[0][0]) < int(table[0][1])
ver = int(table[0][0]) < int(table[1][0])
flipside = hoz == ver
rotate_dict = {0: [-1, dim - 1], 1: [1, 0]}


def ro_pro(a, b):
    return rotate_dict[a][0] * b + rotate_dict[a][1]


for x in range(dim):
    for y in range(dim):
        flip = [ro_pro(hoz, x), ro_pro(ver, y)]
        print(table[flip[1 - flipside]][flip[flipside]], end=" ")
    print()
