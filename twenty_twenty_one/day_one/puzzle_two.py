from twenty_twenty_one.common.utilities import transform_input

depth_readings = transform_input('input.txt')
increased_count = 0
measurement_windows = []

for index, depth in enumerate(depth_readings):
    if index > 1997:
        continue

    second_measurment = depth_readings[index + 1]
    third_measurment = depth_readings[index + 2]
    measurement_windows.append(int(depth) + int(second_measurment) + int(third_measurment))

for index, depth in enumerate(measurement_windows):
    if index == 0:
        continue
    if depth > measurement_windows[index - 1]:
        increased_count += 1
        print(f'{depth} is larger than {measurement_windows[index - 1]}')

print(increased_count)