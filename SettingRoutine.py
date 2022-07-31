import random

def write2file(filename, content):
    filename = str(filename) + ".txt"
    txt_file = open(filename, 'w')
    txt_file.write(str(content))
    txt_file.close()
    print("File updated")

def sec_rem(text):
    letters = int(len(text)) - 1
    text_f = text[0:letters]
    return text_f

def fetchconditions(con1,con2,dictionary):
    out_list = []
    for i in dictionary.keys():
        if dictionary.get(i)[2].get(con1) != None:
            subs = dictionary.get(i)[2].get(con1)
            if con2 in subs:
                out_list.append(i)
    return out_list


teachers_dict = {
    1: ['avi', '', {'Class 8': ['s', 'm'], 'Class 9': ['s', 'm']}], 
    2: ['iva', '', {'Class 8': ['evs'], 'Class 9': ['s', 'm']}], 
    3: ['avi2', '', {'Class 9': ['m']}], 
    4: ['avi3', '', {'Class 8': ['e', 'sst', 'evs'], 'Class 9': ['e']}], 
    5: ['avi4', '', {'Class 8': ['s'], 'Class 9': ['m']}], 
    6: ['avi5', '', {'Class 8': ['m'], 'Class 9': ['m']}], 
    7: ['avi6', '', {'Class 8': ['s'], 'Class 9': ['s']}], 
    8: ['avi7', 'ct', {'Class 9': ['m']}], 
    9: ['avi8', 'ct', {'Class 8': ['sst', 'evs', 'e'], 'Class 9': ['s', 'e']}], 
    10: ['avi9', 'ct', {'Class 9': ['e']}], 
    11: ['avi10', 'ct', {'Class 8': ['e'], 'Class 9': ['e']}], 
    12: ['avi11', 'ct', {'Class 8': ['sst'], 'Class 9': ['s', 'e']}], 
    13: ['avi12', '', {'Class 8': ['e', 'evs'], 'Class 9': ['e']}], 
    14: ['avi13', 'ct', {'Class 8': ['sst', 'evs'], 'Class 9': ['e']}], 
    15: ['avi14', '', {'Class 8': ['evs'], 'Class 9': ['s']}]}

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
#print(fetchconditions('Class 9','s',teachers_dict))

days = {"Mon": {}, "Tue": {}, "Wed": {}, "Thu": {}, "Fri": {}}
slots = 3

for i in days.keys():
    for j in t_d_c.keys():
        for k in t_d_c.get(j)[2].keys():
            day_dict = days.get(i)
            day_dict[k] = t_d_c.get(j)[2].get(k)

columns = {"Mon": {}, "Tue": {}, "Wed": {}, "Thu": {}, "Fri": {}}
for i in columns.keys():
    columns.get(i)[0] = [[],[]]
    for j in t_d_c.keys():
        for k in t_d_c.get(j)[2].keys():
            columns.get(i).get(0)[0].append(t_d_c.get(j)[2].get(k)[0][0])
            columns.get(i).get(0)[1].append(t_d_c.get(j)[2].get(k)[0][1])
for i in range(1,slots):
    for j in columns.keys():
        columns.get(j)[i] = [[],[]]

for i in days.keys():   # Mon, Tue, ...
    rw = 0
    for j in days.get(i).keys():    # Class8a, Class8b, ...
        for k in range(1,slots):    # 0, 1, 2
            repeat = True
            while(repeat):
                nxt_subject = random.choice(t_d_c.get(sec_rem(j))[0])
                for l in range(k):
                    if nxt_subject == columns.get(i).get(l)[1][rw]:
                        break
                    else:
                        if l == (k - 1):
                            repeat = False
            columns.get(i).get(k)[1].append(nxt_subject)
            repeat = True
            while(repeat):
                nxt_teacher = random.choice(fetchconditions(sec_rem(j),nxt_subject,teachers_dict))
                if not (nxt_teacher in columns.get(i).get(k)[0]):
                    repeat = False
            columns.get(i).get(k)[0].append(nxt_teacher)
            #days.get(i).get(j).append([nxt_teacher, nxt_subject])
        rw += 1

write2file("Routine",columns)