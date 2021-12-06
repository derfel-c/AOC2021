def find_hazards1(lines: list[list[list[int]]], board: list[list[int]]):
    for set in lines:
        if set[0][0] == set[1][0] or set[0][1] == set[1][1]:
            x_step = set[1][0] - set[0][0]
            y_step = set[1][1] - set[0][1]
            if x_step != 0:
                for i in range(0, x_step, 1 if x_step > 0 else -1):
                    board[set[0][0] + i][set[0][1]] += 1
            if y_step != 0:
                for i in range(0, y_step, 1 if y_step > 0 else -1):
                    board[set[0][0]][set[0][1] + i] += 1
            board[set[1][0]][set[1][1]] += 1


def find_hazards2(lines: list[list[list[int]]], board: list[list[int]]):
    for set in lines:
        x_step = set[1][0] - set[0][0]
        y_step = set[1][1] - set[0][1]
        if abs(x_step) == abs(y_step) and x_step != 0:
            for i in range(0, x_step, 1 if x_step > 0 else -1):
                j = i if y_step == x_step else i * -1
                board[set[0][0] + i][set[0][1] + j] += 1
        elif x_step != 0:
            for i in range(0, x_step, 1 if x_step > 0 else -1):
                board[set[0][0] + i][set[0][1]] += 1
        elif y_step != 0:
            for i in range(0, y_step, 1 if y_step > 0 else -1):
                board[set[0][0]][set[0][1] + i] += 1
        board[set[1][0]][set[1][1]] += 1


def find_most_dangerous_spots(board: list[list[int]]) -> int:
    return sum([1 for a in board for p in a if p > 1])


with open("input.txt", "r") as f:
    split = list(map(lambda x: x.split("->"), f.read().splitlines()))
    int_list = []
    for x in split:
        a = [map(int, y.split(',')) for y in x]
        int_list.append([list(h) for h in a])
    max_coordinate = max([max(c) for j in int_list for c in j]) + 1
    board = [[0] * (max_coordinate) for _ in range(max_coordinate)]
    find_hazards2(int_list, board)
    print(find_most_dangerous_spots(board))
