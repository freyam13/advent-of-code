from twenty_twenty_four.common.utilities import split_columns_to_lists

location_ids = split_columns_to_lists('input.txt')

sorted_column_a = sorted(location_ids[0])
sorted_column_b = sorted(location_ids[1])
difference = []

# puzzle one
for column_a_value, column_b_value in zip(sorted_column_a, sorted_column_b):
    difference.append(abs(int(column_a_value) - int(column_b_value)))

# puzzle one output
print(sum(difference))


# puzzle two
similar_number_dict = {}
similarity_scores = []

for column_a_value in sorted_column_a:
    if column_a_value in sorted_column_b:
        similar_number_dict[column_a_value] = sorted_column_b.count(column_a_value)

for key, value in similar_number_dict.items():
    similarity_scores.append(int(key) * value)

# puzzle two output
print(sum(similarity_scores))
