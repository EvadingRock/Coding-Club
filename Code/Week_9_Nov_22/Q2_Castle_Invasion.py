castle_size = int(input())

front_heights, right_heights = [int(h) for h in input().split()], [int(h) for h in input().split()]
front_dict, right_dict = {}, {}
front_max, right_max = 0, 0

for h in front_heights:
    if h not in front_dict:
        front_dict[h] = 1
    else:
        front_dict[h] += 1

for h in right_heights:
    if h not in right_dict:
        right_dict[h] = 1
    else:
        right_dict[h] += 1

front_keys, right_keys = sorted(front_dict), sorted(right_dict)

if front_keys[-1] != right_keys[-1]:
    print(-1)
else:
    total_volume = 0

    col_sum = 0
    col_nums = 0
    s_tower = 0

    for h in range(len(front_keys)):
        while right_keys[s_tower] < front_keys[h]:
            col_sum += right_dict[right_keys[s_tower]] * right_keys[s_tower]
            col_nums += right_dict[right_keys[s_tower]]
            s_tower += 1

        total_volume += col_sum * front_dict[front_keys[h]]
        total_volume += (castle_size - col_nums) * front_keys[h] * front_dict[front_keys[h]]

    print(total_volume)
