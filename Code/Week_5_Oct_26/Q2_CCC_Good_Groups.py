the_dict = {0: ["0", "0"]}
groups = []
broken = 0

for x in [0, 1]:
    for y in range(int(input())):
        split = input().split()
        for z in [0, 1]:
            try:
                the_dict[split[z]][x].add(split[1 - z])
            except KeyError:
                the_dict[split[z]] = [set(), set()]
                the_dict[split[z]][x].add(split[1 - z])

for x in range(int(input())):
    groups.append(input().split())

measure = [[1, 2], [0, 2], [0, 1]]

for x in groups:
    for y in x:
        if y not in the_dict:
            y = 0

        for z in the_dict[y][0]:
            if z not in x and z != "0":
                broken += 1

        for z in the_dict[y][1]:
            if z in x:
                broken += 1

print(int(broken/2))
