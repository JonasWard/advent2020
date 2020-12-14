# bsp
# bitwise operations
from get_path import *

f = open(str(get_data_path() ) + "/day_5.csv", "r")

def ids_from_string(string):
    a, b = string[:7], string[7:]

    a = a.replace('B', '1')
    a = a.replace('F', '0')

    b = b.replace('R', '1')
    b = b.replace('L', '0')

    a = int(a, 2)
    b = int(b, 2)
    c = a * 8 + b

    print("{}  : row {}, column {}, seat {}".format(string, a, b, c))

    return a, b, c

higest_id = 0
all_ids = []
for ln in f.readlines():
    _, _, string_id = ids_from_string(ln)
    all_ids.append(string_id)
    if higest_id < string_id:
        higest_id = string_id

print(higest_id)


not_in_list = []
for i in range(128 * 8):
    if not(i in all_ids):
        not_in_list.append(i)

print(not_in_list)