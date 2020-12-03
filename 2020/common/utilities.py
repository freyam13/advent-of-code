def transform_input(file, type='list'):
    puzzle_input = open(file, 'r')
    values = None

    if type == 'list':
        values = []
        for line in puzzle_input.readlines():
          values.append(line.strip())

    return values
