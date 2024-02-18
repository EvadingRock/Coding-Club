divisors, max_count = input().split()

max_count = int(max_count)

div_dict = {}

for x in range(int(divisors)):
    div_val, word = input().split()
    div_dict[int(div_val)] = word

div_dict = dict(sorted(div_dict.items()))

cor_div = list(div_dict.keys())

total_list = list(range(1, max_count + 1))

for x in cor_div:
    counter = 1
    current_num = x
    while current_num <= max_count:
        if type(total_list[current_num - 1]) == int:
            total_list[current_num - 1] = div_dict[x]
        else:
            total_list[current_num - 1] = f"{total_list[current_num - 1]}{div_dict[x]}"
        counter += 1
        current_num = counter * x

for x in total_list:
    print(x)
