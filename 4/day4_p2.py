from typing import List
import copy

def parse_boards(data: list) -> list:
    boards = []
    single_board = []
    for i in range(2, len(data)):
        if content[i] != "":
            row = list(filter(None, content[i].split(" ")))
            single_board.append(list(map(int, row)))
        else:
            single_board = []
        if len(single_board) == 5:
            boards.append(single_board)
    return boards


def bingo(boards: List[List[List[int]]], draws: list) -> int:
    placeholder = -1
    copied_boards = copy.deepcopy(boards)
    winner = []
    winning_draw = 0
    winning_idx = []
    for draw in draws:
        for wi, board in enumerate(copied_boards):
            if wi in winning_idx:
                continue
            for row in board:
                for i, n in enumerate(row):
                    if n == draw:
                        row[i] = placeholder
                if all(x == placeholder for x in row):
                    winning_draw = draw
                    winner.append(board)
                    winning_idx.append(wi)
                tup = zip(*board)
                if all(x == placeholder for x in tup):
                    winning_draw = draw
                    winner.append(board)
                    winning_idx.append(wi)
    return sum(val for row in winner[-1] for val in row if val != placeholder) * winning_draw


with open("input.txt", "r") as f:
    content = f.read().splitlines()
    drawing = list(map(int, content[0].split(",")))
    boards = parse_boards(content)
    print(bingo(boards, drawing))
