from get_path import *

f = open(str(get_data_path() ) + "/day_6.csv", "r")

lns = f.read().split("\n\n")
lns2 = lns[:]
n_lns = []
for ln in lns:
    n_lns.append(ln.replace('\n',''))
lns = []
for ln in n_lns:
    lns.append(ln.replace(' ',''))

# print(lns)
char_lns = [set(ln) for ln in lns]
count = [len(ln) for ln in char_lns]
cnt = 0
for c in count:
    cnt += c
print(cnt)

n_lns = [ln.split('\n') for ln in lns2]

counts = []
for i, ln in enumerate(n_lns):
    length = len(ln)
    count = 0
    for char in char_lns[i]:
        sub_count = 0
        for l in ln:
            # print(l)
            if char in l:
                "print: yes!"
                sub_count += 1

        if sub_count == length:
            count+= 1

    counts.append(count)

cnt = 0
for c in counts:
    cnt += c
print(cnt)