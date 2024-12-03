from collections import Counter
from typing import List, Tuple


def split_columns_to_lists(file, number_of_columns=2) -> Tuple[List[str], List[str]]:
    puzzle_input = open(file, 'r')
    column_a = []
    column_b = []

    for line in puzzle_input.readlines():
        stripped_line = line.strip()

        if number_of_columns == 2:
            column_a_value, column_b_value = stripped_line.split('  ')
            column_a.append(column_a_value.strip())
            column_b.append(column_b_value.strip())

        else:
            print('add supporting logic')

    return column_a, column_b


def split_rows_to_lists(file) -> List[List[int]]:
    puzzle_input = open(file, 'r')
    rows = []

    for line in puzzle_input.readlines():
        stripped_line = line.strip()

        row = list(map(int, stripped_line.split(' ')))
        rows.append(row)

    return rows



def transform_input(file, type='list', split_values=False, split_character=None):
    puzzle_input = open(file, 'r')
    values = None

    if type == 'list':
        values = []
        for line in puzzle_input.readlines():
            if split_values:
                split_line = line.strip().split(split_character)
                values.append({split_line[0]: split_line[1]})
            else:
                values.append(line.strip())

    return values


def transform_input_to_columns(file, length):
    puzzle_input = open(file, 'r')
    lines = puzzle_input.readlines()
    column_number = 0
    results = []

    for character in range(length):
        result_set = []
        for x in lines:
            result_set.append(x.strip()[column_number])
        puzzle_input.close()
        column_number += 1
        results.append(result_set)

    return results


def least_common(list):
    return min(set(list), key=list.count)


def most_common(list):
    return max(set(list), key=list.count)


# def count_most_common(elements: list):
#     count_dict = Counter(elements)
#     ones = count_dict['0']
#     zeros = count_dict['1']
#     return '1' if ones >= zeros else '0'
#
#
# def count_least_common(elements: list):
#     count_dict = Counter(elements)
#     ones = count_dict['0']
#     zeros = count_dict['1']
#     return '0' if zeros >= ones else '1'


def get_rating(numbers, bit):
    idx = 0
    while len(numbers) > 1:
        count = sorted(
            Counter(list(zip(*numbers))[idx]).most_common(), key=lambda x: (x[1], x[0])
        )
        numbers = [item for item in numbers if item[idx] == count[bit][0]]
        print(numbers)
        idx += 1

    return int(numbers[0], 2)
