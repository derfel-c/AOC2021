from collections import Counter


def count_fish_slow(state: list[int], days: int) -> int:
    for i in range(days):
        popping_fish = [i for i, x in enumerate(state) if x == 0]
        for j, x in enumerate(state):
            if j not in popping_fish:
                state[j] -= 1
        for j in popping_fish:
            state.append(8)
            state[j] = 6
        print("Day: {} -> Fish: {}".format(i, len(state)))
    return len(state)


def count_fish_fast(state: list[int], days: int) -> int:
    day_count = [0 for _ in range(9)]
    initial_count = Counter(state)
    for key, val in initial_count.items():
        day_count[key] = val
    for i in range(days):
        day_count_copy = day_count.copy()
        day_count_copy[0] = day_count_copy[1]
        day_count_copy[1] = day_count_copy[2]
        day_count_copy[2] = day_count_copy[3]
        day_count_copy[3] = day_count_copy[4]
        day_count_copy[4] = day_count_copy[5]
        day_count_copy[5] = day_count_copy[6]
        day_count_copy[6] = day_count_copy[7] + day_count[0]
        day_count_copy[7] = day_count_copy[8]
        day_count_copy[8] = day_count[0]
        day_count = day_count_copy
    return sum(day_count)


with open("input.txt", "r") as f:
    fish = list(map(int, f.read().split(",")))
    print(count_fish_fast(fish, 256))
