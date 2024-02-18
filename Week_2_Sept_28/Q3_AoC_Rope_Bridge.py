head_moves = []

while True:
    user_input = input()

    if user_input == "":
        break
    else:
        direct, times = user_input.split()
        head_moves.append([direct, int(times)])


def sign(number):
    if number > 0:
        return 1
    else:
        return -1


dire_dict = {
    "U": [1, 1],
    "D": [1, -1],
    "R": [0, 1],
    "L": [0, -1]
}

# Part 1

head_pos = [0, 0]
tail_pos = [0, 0]

tail_record = {"0 0"}

for dire, reps in head_moves:
    x_y, change = dire_dict[dire]

    for _ in range(reps):
        old_pos = head_pos[:]
        head_pos[x_y] += change

        x_dif, y_dif = head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]

        if abs(x_dif) == 2 or abs(y_dif) == 2:
            tail_pos = old_pos[:]
            tail_record.add(f"{tail_pos[0]} {tail_pos[1]}")


print(f"Part 1: {len(tail_record)}")

# Part 2

current_pos = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

tail_record = set("0 0")
hi = ["0 0"]

for dire, reps in head_moves:
    x_y, change = dire_dict[dire]

    for _ in range(reps):
        current_pos[0][x_y] += change

        tail_moved = True

        for part in range(9):
            x_dif = current_pos[part][0] - current_pos[part + 1][0]
            y_dif = current_pos[part][1] - current_pos[part + 1][1]

            if abs(x_dif) + abs(y_dif) >= 3:
                current_pos[part + 1][0] += sign(x_dif)
                current_pos[part + 1][1] += sign(y_dif)
            elif abs(x_dif) == 2:
                current_pos[part + 1][0] += sign(x_dif)
            elif abs(y_dif) == 2:
                current_pos[part + 1][1] += sign(y_dif)
            else:
                tail_moved = False
                break

        if tail_moved:
            tail_record.add(f"{current_pos[9][0]} {current_pos[9][1]}")
            hi.append(f"{current_pos[9][0]} {current_pos[9][1]}")

print(f"Part 2: {len(set(hi))}")
