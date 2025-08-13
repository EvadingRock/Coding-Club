input()
acorns = list(map(int, input().split()))

acorn_dict = {}

for a in acorns:
    if a in acorn_dict:
        acorn_dict[a] += 1
    else:
        acorn_dict[a] = 1

acorn_types = sorted(acorn_dict)

for s in range(len(acorn_types) - 1, -1, -1):
    top_acorn = acorn_dict[acorn_types[s]]
    if top_acorn > 0:
        for a in range(s):
            if acorn_dict[acorn_types[a]] - top_acorn > 0:
                acorn_dict[acorn_types[a]] -= top_acorn
            else:
                acorn_dict[acorn_types[a]] = 0

total_cost = 0

for a in acorn_types:
    total_cost += acorn_dict[a] * a

print(total_cost)
