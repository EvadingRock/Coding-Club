from math import sqrt, floor

min_spi = int(input())
max_spi = int(input())

len_spi = max_spi - min_spi + 1
s_spi = floor(sqrt(len_spi)) + 2
pos_spi = floor(s_spi/2) - 1
len_max_spi = len(str(max_spi))
spaces = " " * len_max_spi
spiral = [[spaces] * s_spi for x in range(s_spi)]


def itr_spi():
    min_func = min_spi
    c_spi = [pos_spi, pos_spi]
    count = 1

    while True:
        for a in [1, -1]:
            for i in range(2):
                for x in range(count):
                    spiral[c_spi[0]][c_spi[1]] = min_func
                    min_func += 1
                    c_spi[i] += a
                    if min_func > max_spi:
                        return
            count += 1


itr_spi()

if spiral[0][0] == spaces:
    for x in spiral:
        x.pop(0)

for x in spiral:
    for y in range(len(x)):
        print(x[y], end=" " * (len_max_spi - len(str(x[y])) + 1))
    print()
