import statistics


def part_1(data):
    median = statistics.median(data)
    fuel_sum = 0
    for v in data:
        fuel_sum += abs(v - median)
    print("Total fuel required: {}".format(fuel_sum))


def part_2(data):
    mean = round(statistics.mean(data))
    fuel = sum(gauss(abs(x - mean)) for x in data)

    for mid in range(min(data), max(data) + 1):
        fuel = min(fuel, sum(gauss(abs(x - mid)) for x in data))
    print("Total fuel required: {}".format(fuel))


def gauss(n):
    return n*(1+n) / 2


with open("input.txt", "r") as f:
    split = list(map(int, f.read().split(",")))
    split.sort()
    part_1(split)
    part_2(split)
