def get_sums(values: list) -> list:
    return [sum(values[i:i + 3]) for i in range(0, len(values) - 2)]


def get_increases(values: list) -> int:
    return sum(1 for i in range(0, len(values) - 1) if values[i] < values[i + 1])


f = open("input.txt", "r")
puzzle_input = list(map(int, f.read().splitlines()))
summed_content = get_sums(puzzle_input)
increase_count = get_increases(puzzle_input)
summed_increase_count = get_increases(summed_content)
print('P1: {}\nP2: {}'.format(increase_count, summed_increase_count))
