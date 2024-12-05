import numpy as np

puzzle_input = [list(line.strip()) for line in open('input.txt', 'r').readlines()]

# puzzle one
matrix = np.array(puzzle_input).reshape(len(puzzle_input[0]), len(puzzle_input))

all_sequence_lists = []
count = 0

# get all rows and in reverse
for row in matrix:
    row_list = row.tolist()
    all_sequence_lists.append(row_list)
    all_sequence_lists.append(row_list[::-1])

# get all columns and in reverse
for column in matrix.transpose():
    column_list = column.tolist()
    all_sequence_lists.append(column_list)
    all_sequence_lists.append(column_list[::-1])

# get all diagonal
number_of_rows, number_of_columns = matrix.shape

for offset in range(-number_of_rows + 1, number_of_columns):
    diagonal_list = matrix.diagonal(offset=offset).tolist()
    all_sequence_lists.append(diagonal_list)
    all_sequence_lists.append(diagonal_list[::-1])

# get all diagonal in reverse
for offset in range(-number_of_rows + 1, number_of_columns):
    diagonal_list = np.fliplr(matrix).diagonal(offset=offset).tolist()
    all_sequence_lists.append(diagonal_list)
    all_sequence_lists.append(diagonal_list[::-1])

for sequence in all_sequence_lists:
    count += ''.join(sequence).count('XMAS')

# puzzle one output
print(count)


# puzzle two
MAS = 'MAS'
count_two = 0

for column in range(number_of_columns - 2):

    for row in range(number_of_rows - 2):
        part_a = (
            matrix[row, column],
            matrix[row + 1, column + 1],
            matrix[row + 2, column + 2],
        )
        part_b = (
            matrix[row + 2, column],
            matrix[row + 1, column + 1],
            matrix[row, column + 2],
        )
        part_a_str = ''.join(part_a)
        part_b_str = ''.join(part_b)

        if (part_a_str == MAS or part_a_str[::-1] == MAS) and (
            part_b_str == MAS or part_b_str[::-1] == MAS
        ):
            count_two += 1

# puzzle two output
print(count_two)
