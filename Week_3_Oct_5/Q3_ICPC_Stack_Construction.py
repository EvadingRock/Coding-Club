stack_string = list(input())

char_dict = {}
existence_dict = {}

# The dictionary will store each character as a key
# Each value will be a 3 term list
# Term 1 positions of the character
# Term 2 contains the


def bi_in(array, end_val):
    minimum = 0
    maximum = len(array)

    while 1:
        mid = (minimum + maximum) // 2

        if maximum - minimum == 1:
            if end_val == array[mid]:
                return True
            else:
                return False
        elif end_val < array[mid]:
            maximum = mid
        elif end_val > array[mid]:
            minimum = mid


for char in range(len(stack_string)):
    char_dict[stack_string[char]][0].append(char)

    char_dict[stack_string[char]] = [[char], [], 0]

print(char_dict)

stack = []
current_output = ""
moves = 0

distance_next = 1
origin_dis = len(stack)
pop_loc = []


def calc_stack():
    pass


for char in range(len(stack_string)):
    char_dict[stack_string[char]][2] += 1
    counter = char_dict[stack_string[char]][2]
    pop_loc = char_dict[stack_string[char]][0][counter:]

    print(stack_string[char])
    print(counter)
    print(pop_loc)
    print()

    if len(char_dict[stack_string[char]][1]) == 0:
        char_dict[stack_string[char]][1].append(char)
        stack.append(char)
        current_output = f"{current_output}{stack_string[char]}"
        moves += 2

