filename = "RoutinePrint.txt"
txt_file = open(filename, 'w')
txt_file.write("")
txt_file.close()

txt_file = open(filename, 'a')


def wrt(content):
    txt_file.write(str(content))


slots = 3

columns = {
    'Mon': {
        0: [[14, 12, 9, 10, 11, 8], ['sst', 'sst', 'e', 'e', 'e', 'm']], 
        1: [[13, 4, 14, 5, 2, 11], ['e', 'evs', 'sst', 'm', 's', 'e']], 
        2: [[6, 1, 5, 9, 3, 12], ['m', 'm', 's', 's', 'm', 's']]
    }, 'Tue': {
        0: [[14, 12, 9, 10, 11, 8], ['sst', 'sst', 'e', 'e', 'e', 'm']], 
        1: [[5, 1, 7, 6, 9, 12], ['s', 's', 's', 'm', 's', 's']], 
        2: [[13, 11, 9, 1, 2, 14], ['evs', 'e', 'evs', 's', 'm', 'e']]
    }, 'Wed': {
        0: [[14, 12, 9, 10, 11, 8], ['sst', 'sst', 'e', 'e', 'e', 'm']], 
        1: [[7, 9, 6, 12, 8, 14], ['s', 'evs', 'm', 's', 'm', 'e']], 
        2: [[13, 1, 7, 5, 15, 2], ['e', 's', 's', 'm', 's', 's']]
    }, 'Thu': {
        0: [[14, 12, 9, 10, 11, 8], ['sst', 'sst', 'e', 'e', 'e', 'm']], 
        1: [[11, 1, 12, 5, 9, 13], ['e', 'm', 'sst', 'm', 's', 'e']], 
        2: [[1, 2, 7, 15, 5, 9], ['m', 'evs', 's', 's', 'm', 's']]
    }, 'Fri': {
        0: [[14, 12, 9, 10, 11, 8], ['sst', 'sst', 'e', 'e', 'e', 'm']], 
        1: [[4, 14, 7, 12, 5, 10], ['e', 'evs', 's', 's', 'm', 'e']], 
        2: [[14, 9, 2, 3, 15, 1], ['evs', 'e', 'evs', 'm', 's', 's']]
    }
}

t_d_c = {
    'Class 8': [['s', 'm', 'e', 'sst', 'evs'], [1, 2, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15], {
        'Class 8a': [[14, 'sst']],
        'Class 8b': [[12, 'sst']],
        'Class 8c': [[9, 'e']]
    }],
    'Class 9': [['s', 'm', 'e'], [1, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15], {
        'Class 9a': [[10, 'e']],
        'Class 9b': [[11, 'e']],
        'Class 9c': [[8, 'm']]
    }]
}

for i in t_d_c.keys():
    rw = 0
    for j in t_d_c.get(i)[2].keys():
        print(f"\n\n{j} Routine:\n")
        print('\t', end='')
        for k in range(slots):
            print(f"Period {k+1} | ", end='')
        print(f"\n{('-'*41)}")
        for a in columns.keys():
            print(a, '\t', end='')
            for b in range(slots):
                n = 5 - len(str(columns.get(a).get(b)[1][rw]) + str(columns.get(a).get(b)[0][rw]))
                print(f"{columns.get(a).get(b)[1][rw]} - {columns.get(a).get(b)[0][rw]}{' '*n} | ", end='')
            print(f"\n{('-'*41)}")
        rw += 1

rw = 0
for i in t_d_c.keys():
    for j in t_d_c.get(i)[2].keys():
        if rw != 0:
            wrt('\n\n\n')
        wrt(f"{j} Routine:\n\n")
        for k in range(slots):
            wrt('\t')
            wrt(f"\tPeriod {k+1}  |")
        wrt(f"\n{('-'*52)}")
        for a in columns.keys():
            wrt(f"\n{a} |")
            # wrt('\t')
            for b in range(slots):
                period = str(columns.get(a).get(b)[1][rw]) + " - " + str(columns.get(a).get(b)[0][rw])
                n = 9 - len(period)
                sp = " " * n
                period = period + sp
                wrt(f"\t{period} | ")
            wrt(f"\n{('-'*52)}")
        rw += 1


txt_file.close()
print("File updated")
