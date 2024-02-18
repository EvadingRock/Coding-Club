extra_badge = [[], []]
totals = [0, 0]
badge = [0, 0, 0]
r = 0

try:
    while True:
        current_pack = list(input())
        half_1 = set(current_pack[:int(len(current_pack) / 2)])
        half_2 = set(current_pack[int(len(current_pack) / 2):])
        extra_badge[0].append(list(half_1.intersection(half_2))[0])

        badge[r] = (set(current_pack))
        if r == 2:
            for x in [1, 2]:
                badge[0] = badge[0].intersection(badge[x])
            extra_badge[1].append(list(badge[0])[0])
            r = -1
        r += 1
except IndexError:
    pass

for x in [0, 1]:
    for char in extra_badge[x]:
        char_num = ord(char)
        if char_num < 96:
            totals[x] += char_num - 38
        else:
            totals[x] += char_num - 96

print(f"Part 1: {totals[0]}   Part 2: {totals[1]}")
