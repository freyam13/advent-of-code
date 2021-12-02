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
