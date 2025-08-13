equation_amount = int(input())
equations = [input() for _ in range(equation_amount)]


def ender(string, state):
    if state:
        return string
    else:
        return string + " "


def rec_print(to_print, end=False):
    if type(to_print) is list:
        my_string = "("

        for val in range(len(to_print) - 1):
            my_string += rec_print(to_print[val])
        my_string += rec_print(to_print[-1], True)

        return ender(my_string + ")", end)
    else:
        return ender(to_print, end)


for equation in range(equation_amount):
    equ = equations[equation].split()

    for chars in [["X"], ["+", "-"]]:
        location_list = []
        for p in range(len(equ)):
            for c in chars:
                if equ[p] == c:
                    location_list.append(p)

        excess = 0
        for loc in location_list:
            x = loc - excess
            equ[x - 1: x + 2] = [equ[x - 1: x + 2]]
            excess += 2

    if len(equ) == 1:
        while len(equ) == 1:
            equ = equ[0]

    new_equation = ""
    for part in range(len(equ) - 1):
        new_equation += rec_print(equ[part])
    new_equation += rec_print(equ[-1], True)

    print(new_equation)

    if equation != equation_amount - 1:
        print()
