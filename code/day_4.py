from get_path import *

f = open(str(get_data_path() ) + "/day_4.csv", "r")

main_list = []

for ln in f.read().split("\n\n"):
    loc_dict = {}
    loc_string_lists = ln.split('\n')
    new_loc_strings = []
    for ln in loc_string_lists:
        new_loc_strings.extend(ln.split(' '))

    for sub_str in new_loc_strings:
        a, b = sub_str.split(':')
        
        loc_dict[a] = b
    main_list.append(loc_dict)

# tags_to_test = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
tags_to_test = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid_ids = 0

for sub_dict in main_list:
    is_valid = True
    for tag in tags_to_test:
        try:
            sub_dict[tag]
        except:
            is_valid = False
    try:
        # print("reading byr")
        byr = int(sub_dict["byr"])
        # print("reading iyr")
        iyr = int(sub_dict["iyr"])
        # print("reading eyr")
        eyr = int(sub_dict["eyr"])
        # print("reading hgt")
        hgt = sub_dict["hgt"]
        # print("reading hcl")
        hcl = sub_dict["hcl"]
        # print("reading ecl")
        ecl = sub_dict["ecl"]
        # print("reading pid")
        # cid = sub_dict["cid"]

        if not(byr > 1919 and byr < 2003):
            print("invalid byr : ", byr)
            continue
        if not(iyr > 2009 and iyr < 2021):
            print("invalid iyr : ", iyr)
            continue
        if not(eyr > 2019 and eyr < 2031):
            print("invalid eyr : ", eyr)
            continue
        
        if "in" in hgt:
            height_paramter = "in"
            height = int(hgt.replace("in", ''))

            if not(height > 58 and height < 77):
                print("invalid hgt : ", hgt)
                continue

        elif "cm" in hgt:
            height_paramter = "cm"
            height = int(hgt.replace("cm", ''))

            if not(height > 149 and height < 194):
                print("invalid hgt : ", hgt)
                continue
        else:
            print("invalid hgt : ", hgt)
            is_valid = False
            continue
        
        if hcl[0] == '#' and len(hcl) == 7:
            print("hcl : ", hcl)
            all_valid_chars = 0
            for char in hcl[1:]:
                valid_char = False

                for val_char in "0123456789abcdef":
                    if char == val_char:
                        all_valid_chars += 1
                        break
            
            if not(all_valid_chars == 6):
                print("invalid hcl : ", hcl)
                continue
        else:
            print("invalid hcl : ", hcl)
            continue
        
        if len(ecl) == 3:
            is_valid_ecl = False
            for valid_val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                if valid_val == ecl:
                    is_valid_ecl = True
                    continue

            if not(is_valid_ecl):
                print("invalid ecl : ", ecl)
                continue

        if len(pid) == 8:
            is_valid_pid = False
            valid_char_cnt = 0
            for char in pid:
                for valid_pid in "0123456789":
                    if valid_pid == char:
                        valid_char_cnt += 1
                        continue

            if not(all_valid_chars == 8):
                print("invalid pid : ", pid)
                continue
        
        try:
            cid = sub_dict["cid"]
            try:
                int(cid)
            except:
                print("invalid cid : ", cid)
                continue
        except:
            pass

        print("reached the end!")
        valid_ids += 1

    except:
        continue

print(valid_ids)
