from get_path import *

f = open(str(get_data_path() ) + "/day_3.csv", "r")

main_list = []

for ln in f.read().split("\n"):
    sub_list = []
    for char in ln:
        if char == '.':
            sub_list.append(0)
        elif char == '#':
            sub_list.append(1)

    main_list.append(sub_list)

def row_check(row_delta_per_step = 1, row_step = 3):
    global main_list
    line_len = len(main_list[0])
    line_cnt = len(main_list)
    diagonal_sum = 0
    idx = 0

    row_idx = 0

    while row_idx < line_cnt:
        diagonal_sum += main_list[row_idx][idx]
        idx += row_step
        idx %= line_len

        row_idx += row_delta_per_step

    return diagonal_sum

total_product = 1
step_cnt = []
for b, a in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    loc_value = row_check(a, b)
    step_cnt.append(loc_value)

    total_product *= loc_value

print(total_product)


