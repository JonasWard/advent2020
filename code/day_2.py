from get_path import *

f = open(str(get_data_path() ) + "/day_2.csv", "r")

val_a, val_b = "i", "j"
letter = "letter"
text = "text"

data_list = []

# constructing the dictionary containing the data
for ln in f.read().split("\n"):
    loc_dict = {}
    a, b, c = ln.split(' ')
    vals = [ int(val) for val in a.split('-') ]
    vals.sort()
    loc_dict[val_a], loc_dict[val_b] = vals
    loc_dict[letter], _ = b.split(':')
    loc_dict[text] = c

    data_list.append(loc_dict)
    # numbers.append(int(ln) )

valid_count = 0

# checking the password validity
for data in data_list:
    letter_count = data[text].count(data[letter])
    if ( letter_count >= data[val_a] and letter_count <= data[val_b] ):
        valid_count += 1

print("rule 1 : ", valid_count)

valid_count = 0

# checking indexes
for data in data_list:
    loc_validity = 0
    try:
        if data[text][data[val_a]-1] == data[letter]:
            loc_validity += 1
    except:
        pass
    try:
        if data[text][data[val_b]-1] == data[letter]:
            loc_validity += 1
    except:
        pass

    if loc_validity == 1:
        valid_count += 1

print("rule 2 : ", valid_count)