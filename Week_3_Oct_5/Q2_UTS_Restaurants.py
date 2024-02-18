n, t, k, v = input().split()

total_blocks = int(n)
segment_len = int(t)
min_restaurants = int(k)
restaurant_list = [int(input()) for _ in range(int(v))]

block_state = [False] * total_blocks
for x in restaurant_list:
    block_state[x - 1] = True

current_block = 0
res_count = 0

for _ in range(segment_len):
    if block_state[current_block]:
        res_count += 1
    current_block += 1

back = 1
while res_count < min_restaurants:
    if not block_state[current_block - back]:
        block_state[current_block - back] = True
        res_count += 1
    back += 1

while current_block < total_blocks:
    res_count += block_state[current_block]
    res_count -= block_state[current_block - segment_len]

    if res_count < min_restaurants:
        block_state[current_block] = True
        res_count += 1

    current_block += 1

total = 0

for x in range(total_blocks):
    if block_state[x]:
        total += 1

print(total - len(restaurant_list))
