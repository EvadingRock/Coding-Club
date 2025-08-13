dis_min, dis_max = int(input()), int(input())

motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

for _ in range(int(input())):
    motels.append(int(input()))

motels.sort()

distances = [motels[m + 1] - motels[m] for m in range(len(motels) - 1)]

paths = [0 for _ in range(len(motels))]
paths[-1] = 1

for p in range(len(paths) - 1, 0, -1):
    if paths[p] > 0:
        current_distance = distances[p - 1]

        for new_p in range(p - 1, -1, -1):
            if current_distance < dis_min:
                pass
            elif current_distance <= dis_max:
                paths[new_p] += paths[p]
            else:
                break

            current_distance += distances[new_p - 1]

print(paths[0])
