input_text = list(input())

c = 0
while c < len(input_text):
    if input_text[c].isalpha():
        if input_text[c].isupper():
            input_text[c] = input_text[c].lower()

    elif not input_text[c] in " öä’-":
        input_text.pop(c)
        c -= 1

    c += 1

input_text = "".join(input_text).split()


class Node:
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.left = 0
        self.right = 0


def add_node(current_node, new_node):
    if new_node.word == current_node.word:
        current_node.count += 1
    elif new_node.word > current_node.word:
        if current_node.right == 0:
            current_node.right = new_node
        else:
            add_node(current_node.right, new_node)
    else:
        if current_node.left == 0:
            current_node.left = new_node
        else:
            add_node(current_node.left, new_node)


starting_node = Node(input_text[0])

for w in range(1, len(input_text)):
    add_node(starting_node, Node(input_text[w]))


def rec_print(current_node):
    left_off = current_node.left == 0
    right_off = current_node.right == 0

    if left_off and right_off:
        print(f"{current_node.word}: {current_node.count}")
    elif right_off:
        rec_print(current_node.left)
        print(f"{current_node.word}: {current_node.count}")
    elif left_off:
        print(f"{current_node.word}: {current_node.count}")
        rec_print(current_node.right)
    else:
        rec_print(current_node.left)
        print(f"{current_node.word}: {current_node.count}")
        rec_print(current_node.right)


rec_print(starting_node)
