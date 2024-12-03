from twenty_twenty_four.common.utilities import split_rows_to_lists

reports = split_rows_to_lists('input.txt')

# puzzle one (and puzzle two attempt but had to switch to recursive approach)
safe_reports = 0
safe_report_list = []
off_by_one_safe_reports = []

for report in reports:
    delta = None
    safe = None
    unsafe_transitions = 0

    for index, level in enumerate(range(len(report) - 1)):
        value_a = int(report[level])
        value_b = int(report[level + 1])

        if not delta and value_a < value_b:
            delta = 'increasing'

        elif not delta and value_a > value_b:
            delta = 'decreasing'

        if (
            delta == 'increasing'
            and value_a != value_b
            and 1 <= (value_b - value_a) <= 3
        ):
            safe = True

        elif (
            delta == 'decreasing'
            and value_a != value_b
            and 1 <= (value_a - value_b) <= 3
        ):
            safe = True

        else:
            safe = False
            unsafe_transitions += 1

        if safe == True and index == len(report) - 2:
            safe_reports += 1
            safe_report_list.append(report)

        elif unsafe_transitions <= 1 and index == len(report) - 2:
            safe_reports += 1
            safe_report_list.append(report)

# puzzle one (and puzzle two attempt but had to switch to recursive approach)
print(safe_reports)
print(safe_report_list)


# puzzle two (take two)
safe_reports = 0
safe_report_list_two = []


def is_safe(report):
    increasing = all(
        report[level] < report[level + 1] and (report[level + 1] - report[level]) <= 3
        for level in range(len(report) - 1)
    )
    decreasing = all(
        report[level] > report[level + 1] and (report[level] - report[level + 1]) <= 3
        for level in range(len(report) - 1)
    )

    return increasing or decreasing


def can_be_safe(report):
    for level in range(len(report)):
        modified_report = report[:level] + report[level + 1 :]

        if is_safe(modified_report):
            return True

    return False


for report in reports:
    if is_safe(report):
        safe_reports += 1
        safe_report_list_two.append(report)

    elif can_be_safe(report):
        safe_reports += 1

# puzzle two output (take two)
print(safe_reports)
print(safe_report_list_two)
