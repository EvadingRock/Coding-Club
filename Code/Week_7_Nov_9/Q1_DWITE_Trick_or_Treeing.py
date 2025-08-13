# Trick or Treeing
# November 9th, 2023

for r in range(5):
    tree = list(input())
    tree.append(" ")

    candy = 0
    nodes = 0
    roads = 0
    roads_max = 0

    for x in range(len(tree)):
        if tree[x].isdigit():
            if tree[x + 1].isdigit():
                candy += 10
            else:
                candy += int(tree[x])
        elif tree[x] == "(":
            nodes += 4
            roads += 1
            if roads > roads_max:
                roads_max = roads
        elif tree[x] == ")":
            roads -= 1

    print(f"{nodes - roads_max} {candy}")
