while True:
    m_word = input()
    if m_word == "X":
        break

    good_word = True
    checker = [0, 0, 0]

    val_dict = {
        "A": [["S", "N"], 0],
        "S": [["S", "N"], 1],
        "N": [["A", "B"], 0],
        "B": [["A", "B"], 2]
    }

    for c in range(len(m_word) - 1):
        if m_word[c] in val_dict:
            to_check, add_place = val_dict[m_word[c]]
            if m_word[c + 1] in to_check:
                checker[add_place] += 1
                continue

        good_word = False
        break

    if m_word[-1] == "S":
        checker[1] += 1

    if checker[1] != checker[2]:
        good_word = False

    if good_word:
        print("YES")
    else:
        print("NO")
