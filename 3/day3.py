from typing import List


def calculate_power_consumption(data: list) -> int:
    gamma_rate = ''
    epsilon_rate = ''
    for val in zip(*data):
        one_count = val.count('1')
        zero_count = val.count('0')
        if one_count > zero_count:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_life_support(data: list, oxygen: bool) -> int:
    copy: List[str] = data.copy()
    to_remove = []
    idx = 0
    length = len(data)
    while length > 1:
        val = [x[idx] for x in copy]
        one_count = val.count('1')
        zero_count = val.count('0')
        if one_count > zero_count or one_count == zero_count:
            if oxygen:
                [to_remove.append(copy[i]) for i in range(len(copy)) if copy[i][idx] == '0']
            else:
                [to_remove.append(copy[i]) for i in range(len(copy)) if copy[i][idx] == '1']
        else:
            if oxygen:
                [to_remove.append(copy[i]) for i in range(len(copy)) if copy[i][idx] == '1']
            else:
                [to_remove.append(copy[i]) for i in range(len(copy)) if copy[i][idx] == '0']
        copy = [val for val in copy if val not in to_remove]
        idx += 1
        to_remove = []
        length = len(copy)
    return int(copy[0], 2)


with open('input.txt', 'r') as f:
    test_data = ['00100',
                 '11110',
                 '10110',
                 '10111',
                 '10101',
                 '01111',
                 '00111',
                 '11100',
                 '10000',
                 '11001',
                 '00010',
                 '01010']
    puzzle_input = f.read().splitlines()
    a = list(puzzle_input[0])
    p1 = calculate_power_consumption(puzzle_input)
    p2_oxygen = calculate_life_support(puzzle_input, True)
    p2_co2 = calculate_life_support(puzzle_input, False)
    print('Power consumption: {}\nOxygen generator rating: {}\nCO2 scrubber rating: {}\nLife support rating: {}'
          .format(p1, p2_oxygen, p2_co2, p2_co2 * p2_oxygen))
