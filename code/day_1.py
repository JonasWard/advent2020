from get_path import *

f = open(str(get_data_path() ) + "/day_1.csv", "r")

numbers = []
for ln in f.read().split("\n"):
    numbers.append(int(ln) )

for i, val in enumerate(numbers):
    for j, val_2 in enumerate(numbers[i:]):
        for val_3 in numbers[i+j:]:
            if val + val_2 + val_3 == 2020:
                print(val * val_2 * val_3)
