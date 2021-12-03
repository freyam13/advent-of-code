from twenty_twenty_one.common.utilities import (
    get_rating,
    transform_input,
)

bytes_by_line = transform_input('input.txt')

o2 = get_rating(bytes_by_line, 1)
co2 = get_rating(bytes_by_line, 0)

print(o2)
print(co2)
print(o2 * co2)
