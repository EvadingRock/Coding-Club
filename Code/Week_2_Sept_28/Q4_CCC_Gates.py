total_gates = int(input())
total_planes = int(input())
planes_list = [int(input()) for _ in range(total_planes)]
gate_states = list(range(1, 1 + total_gates))


def bi_sec(item):
    minimum = 0
    maximum = len(gate_states)

    while True:
        middle = (minimum + maximum) // 2

        if item == gate_states[middle] or maximum - minimum == 1:
            return middle
        elif item < gate_states[middle]:
            maximum = middle
        elif item > gate_states[middle]:
            minimum = middle


max_planes = 0

for plane in planes_list:
    p_index = bi_sec(plane)

    if gate_states[p_index] > plane:
        break
    else:
        gate_states.pop(p_index)
        max_planes += 1

print(max_planes)
