graph = []
ending_person = 0
min_depth = 0
path_history = []

existing_1 = [[1, 6], [2, 6], [3, 4], [3, 5], [3, 6], [3, 15], [4, 5], [4, 6], [5, 6], [6, 7]]
existing_2 = [[7, 8], [8, 9], [9, 10], [9, 12], [10, 11], [11, 12], [12, 13], [13, 14], [13, 15]]
existing_3 = [[16, 17], [16, 18], [17, 18]]

for x in range(49):
    graph.append(set())
    path_history.append(0)

for x in existing_1 + existing_2 + existing_3:
    graph[x[0]].add(x[1])
    graph[x[1]].add(x[0])


def find_degree(depth, current_person):
    global graph
    global ending_person
    global min_depth
    global path_history

    current_history = path_history[:depth]

    if current_person == ending_person:
        if len(set(current_history)) == len(current_history) and depth < min_depth:
            min_depth = depth

    elif current_person not in current_history:

        path_history[depth] = current_person

        for path in graph[current_person]:
            find_degree(depth + 1, path)


while 1:
    selection = input()

    if selection == "i":
        person_x, person_y = int(input()), int(input())
        graph[person_x].add(person_y)
        graph[person_y].add(person_x)

    if selection == "d":
        person_x, person_y = int(input()), int(input())
        graph[person_x].remove(person_y)
        graph[person_y].remove(person_x)

    if selection == "n":
        person_x = int(input())
        print(len(graph[person_x]))

    if selection == "f":
        person_x = int(input())

        friends_of_friends = set()

        for x in graph[person_x]:
            for y in graph[x]:
                friends_of_friends.add(y)

        not_count = graph[person_x]
        not_count.add(person_x)

        print(len(friends_of_friends.difference(not_count)))

    if selection == "s":
        person_x, ending_person = int(input()), int(input())

        min_depth = 51

        find_degree(0, person_x)

        if min_depth == 51:
            print("Not connected")
        else:
            print(min_depth)

    if selection == "q":
        break
