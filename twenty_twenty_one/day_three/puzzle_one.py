from twenty_twenty_one.common.utilities import (
    transform_input_to_columns,
    most_common,
    least_common,
)

bits = transform_input_to_columns('input.txt', 12)

epsilon_binary = ''
epsilon_rate = 0
gamma_binary = ''
gamma_rate = 0

for byte in bits:
    epsilon_binary += least_common(byte)
    gamma_binary += most_common(byte)

epsilon_rate = int(epsilon_binary, 2)
gamma_rate = int(gamma_binary, 2)
print(gamma_rate)


power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
