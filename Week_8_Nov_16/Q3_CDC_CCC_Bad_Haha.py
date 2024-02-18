cases = [[input(), int(input())] for _ in range(int(input()))]


def b_sorted(nums_list):
    bucket_list = [0] * 10

    for d in nums_list:
        bucket_list[d] += 1

    unpack_list = []

    for x in range(1, 10):
        unpack_list += bucket_list[x] * [x]

    return unpack_list


def stringify(nums_list):
    return "".join([str(n) for n in nums_list])


for score, moves in cases:
    num_score = [int(s) for s in score]

    if moves >= len(score):
        print(stringify(b_sorted(num_score)))
        continue
    elif moves <= 0:
        print(score)
        continue

    end_bucket = [0] * 10
    left_bucket = [0] * 10
    left_bucket_max = num_score[0]

    left_bucket[num_score[0]] += 1
    num_score.pop(0)

    moves_left = moves

    while True:
        if moves_left == 0:
            break

        elif len(num_score) == 0:
            broken_out = False

            for x in range(9, 0, -1):
                can_move = moves_left - left_bucket[x]

                if can_move >= 0 and moves_left > 0:
                    end_bucket[x] += left_bucket[x]
                    moves_left -= left_bucket[x]
                    left_bucket[x] = 0
                    left_bucket_max = x

                else:
                    end_bucket[x] += moves_left
                    left_bucket[x] -= moves_left
                    moves_left = 0
                    broken_out = True
                    break

        elif left_bucket_max > num_score[0]:
            broken_out = False

            for x in range(9, num_score[0], -1):
                can_move = moves_left - left_bucket[x]

                if can_move >= 0 and moves_left > 0:
                    end_bucket[x] += left_bucket[x]
                    moves_left -= left_bucket[x]
                    left_bucket[x] = 0
                    left_bucket_max = x

                else:
                    end_bucket[x] += moves_left
                    left_bucket[x] -= moves_left
                    moves_left = 0
                    broken_out = True
                    break

            if not broken_out:
                left_bucket[num_score[0]] += 1
                num_score.pop(0)

        else:
            left_bucket[num_score[0]] += 1

            left_bucket_max = num_score[0]

            num_score.pop(0)

    final_ans = []

    for n in range(1, 10):
        final_ans += left_bucket[n] * [n]

    final_ans += num_score

    for n in range(1, 10):
        final_ans += end_bucket[n] * [n]

    print(stringify(final_ans))
