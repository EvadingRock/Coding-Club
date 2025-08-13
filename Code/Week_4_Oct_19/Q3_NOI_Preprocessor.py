def_dict = {}


def expand(base_string, current_expands):
    list_string = list(base_string)
    state_char = []

    list_string.append(";")

    for char in list_string:
        if char.isalnum():
            state_char.append(True)
        else:
            state_char.append(False)

    current_symbol = ""
    last_state_false = False
    state = 0
    while state < len(state_char):

        if state_char[state]:
            current_symbol += list_string[state]
            last_state_false = False

        elif not last_state_false:
            if current_symbol in def_dict and current_symbol not in current_expands:
                current_expands.append(current_symbol)
                expanded = expand(def_dict[current_symbol], current_expands)
                current_expands.pop(-1)

                list_string[state - len(current_symbol):state] = expanded

                change_len = len(current_symbol) - len(expanded)

                if change_len >= 0:
                    for x in range(change_len):
                        state_char.pop(0)
                else:
                    for x in range(abs(change_len)):
                        state_char.insert(0, False)

                state -= change_len

            current_symbol = ""
            last_state_false = True

        state += 1

    list_string.pop(-1)

    return "".join(list_string)


all_lines = [input() for _ in range(int(input()))]

for line in all_lines:

    if line[0] == "#":
        line = line.split(" ", 2)

        if line[0][1] == "d":
            def_dict[line[1]] = line[2]
        else:
            def_dict.pop(line[1])

        print()

    else:
        print(expand(line, []))
