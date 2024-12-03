import re


puzzle_input = open('input.txt', 'r').readlines()

# puzzle one
multiplication_operations = []

for line in puzzle_input:
    multiplication_operations.extend(re.findall('mul\(\d+,\d+\)', line))

products_one = []

for operation in multiplication_operations:
    value_a, value_b = re.findall('\d+,\d+', operation)[0].split(',')
    products_one.append(int(value_a) * int(value_b))

# puzzle one output
print(sum(products_one))


# puzzle two
multiplication_operations = []

for line in puzzle_input:
    # multiplication_operations.extend(re.findall('do\(\).+?mul\(\d+,\d+\)', line))
    multiplication_operations.extend(
        re.split(r'(?=do\(\)|don\'t\(\)|mul\(\d+,\d+\))', line)
    )
    # 36

products_two = []
enabled = True

for segment in multiplication_operations:
    if "do()" in segment:
        enabled = True

    elif "don't()" in segment:
        enabled = False

    elif "mul(" in segment and enabled:
        match = re.search(r'mul\((\d+),(\d+)\)', segment)

        if match:
            value_a, value_b = map(int, match.groups())
            products_two.append(value_a * value_b)

# puzzle two output
print(sum(products_two))
