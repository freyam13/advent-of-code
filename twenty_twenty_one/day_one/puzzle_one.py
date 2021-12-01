from twenty_twenty_one.common.utilities import transform_input

depth_readings = transform_input('input.txt')
increased_count = 1

for index, depth in enumerate(depth_readings):
    if index == 0:
        continue
    if depth > depth_readings[index - 1]:
        increased_count += 1
        print(f'{depth} is larger than {depth_readings[index - 1]}')

print(increased_count)