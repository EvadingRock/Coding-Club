total_days, max_out = (int(x) for x in input().split())
car_schedule = []
driveway = []

for _ in range(total_days):
    car_schedule.append(input().split())

for car, state in car_schedule:
    if state == "in":
        driveway.append(car)
    elif driveway[0] == car and max_out > 0:
        driveway.pop(0)
        max_out -= 1
    elif driveway[len(driveway) - 1] == car:
        driveway.pop(len(driveway) - 1)

for car in driveway:
    print(car)
