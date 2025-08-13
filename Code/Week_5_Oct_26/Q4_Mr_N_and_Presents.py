orders_dict = {}
o_list = []
n_list = []
len_o = int(input())

for x in range(len_o):
    pair = input().split()
    orders_dict[pair[1]] = pair[0]
    orders_dict[pair[1]] = orders_dict.pop(pair[1])

for x in orders_dict:
    if orders_dict[x] == "F":
        n_list.insert(0, x)
    elif orders_dict[x] == "E":
        n_list.append(x)

for x in n_list:
    print(x)
