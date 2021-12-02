def calculate_distance(directions: list) -> int:
    depth = 0
    horizontal = 0
    aim = 0
    for i in range(0, len(directions)):
        direction, val = directions[i].split(" ")
        val = int(val)
        if direction == "forward":
            horizontal += val
            depth += aim * val
        elif direction == "down":
            aim += val
        elif direction == "up":
            aim -= val
    return depth * horizontal


with open("input.txt", "r") as f:
    puzzle_input = f.read().splitlines()
    print(calculate_distance(puzzle_input))
