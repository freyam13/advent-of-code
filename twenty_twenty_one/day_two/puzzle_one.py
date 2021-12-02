from twenty_twenty_one.common.utilities import transform_input

parsed_coordinates = transform_input('input.txt', split_values=True, split_character=' ')
horizontal_position = 0
depth = 0

for coordinate in parsed_coordinates:
    direction = next(iter(coordinate.keys()))
    distance = next(iter(coordinate.values()))

    if direction == 'forward':
        horizontal_position += int(distance)

    if direction == 'down':
        depth -= int(distance)

    if direction == 'up':
        depth += int(distance)

print(f'horizontal_position = {horizontal_position}, depth = {depth}')
print(f'{horizontal_position * depth}')