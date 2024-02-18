pairs = int(input())

daughters_dict = {}
mothers_dict = {}
check_list = []

for x in range(pairs):
    mother_daughter = input().split()
    daughters_dict[mother_daughter[1]] = mother_daughter[0]
    mothers_dict[mother_daughter[0]] = []

for x in range(10):
    check_list.append(input())

for x in daughters_dict:
    mothers_dict[daughters_dict[x]].append(x)

for x in check_list:
    sisters = len(mothers_dict[daughters_dict[x]]) - 1
    cousins = -sisters - 1
    for y in mothers_dict[daughters_dict[daughters_dict[x]]]:
        try:
            cousins += len(mothers_dict[y])
        except KeyError:
            pass
    print(f"Cousins: {cousins}, Sisters: {sisters}")
