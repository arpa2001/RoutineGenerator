import random
import sys


# Adding suffix to number
def numsuffix(num):
    nS = ""
    n_l = num % 10
    if num % 100 >= 11 and num % 100 <= 19:
        nS = str(num)+"th"
    elif n_l == 1:
        nS = str(num)+"st"
    elif n_l == 2:
        nS = str(num)+"nd"
    elif n_l == 3:
        nS = str(num)+"rd"
    else:
        nS = str(num)+"th"
    return nS


# Remove section part
def sec_rem(text):
    i = 7
    while i<len(text) and text[i].isdigit():
        i+=1
    return text[:i]

# Find teachers for the corresponding class and subject
def fetchconditions(con1, con2, dictionary):
    out_list = []
    for i in dictionary.keys():
        subs = dictionary.get(i)[2].get(con1)
        if subs:
            if con2 in subs:
                out_list.append(i)
    if not out_list: print(con1,con2)
    return out_list


# Getting Classes
nC = int(input("Number of Classes: "))
classes_dict = {}
for i in range(1, nC+1):
    class_list = []
    class_name = input(f"\nName of {numsuffix(int(i))} class: ")
    sec = int(input("Number of sections of this class: "))
    class_list.append(sec)
    c = int(input("Number of subjects in this class: "))
    sub_list = []
    for j in range(1, c+1):
        sub_name = input(f"Name of {numsuffix(int(j))} subject: ")
        sub_list.append(sub_name)
    class_list.append(sub_list)
    classes_dict["Class " + str(class_name)] = class_list

# Getting Teachers
nT = int(input("Number of Teachers: "))
teachers_dict = {}
for i in range(1, nT+1):
    t_list = []
    t_name = input(f"\nName of {numsuffix(int(i))} teacher: ")
    t_list.append(t_name)
    t_list.append("")
    class_dict = {}
    class_num = int(input("\tNumber of classes to be teached: "))
    for j in range(1, class_num+1):
        class_name = input(f"\tName of {numsuffix(int(j))} class: ")
        class_name = "Class " + str(class_name)
        sub_num = int(
            input(f"\tNumber of subjects to be teached in {class_name}: "))
        sub_list = []
        for k in range(1, sub_num+1):
            sub_name = input(f"\tName of {numsuffix(int(k))} subject: ")
            sub_list.append(sub_name)
        class_dict[class_name] = sub_list
    t_list.append(class_dict)
    teachers_dict[i] = t_list

# Assigning Teachers to Classes
buffer_list = classes_dict.keys()
for i in buffer_list:
    classdict_list = classes_dict.get(i)
    buffer_list = teachers_dict.keys()
    teachers4classses = []
    for j in buffer_list:
        info = teachers_dict.get(j)
        t_classes = info[2]
        buffer_list = t_classes.keys()
        for k in buffer_list:
            if k == i:
                teachers4classses.append(j)
    classdict_list.append(teachers4classses)

# Adding sections to classes
t_d_c = {}
buffer_list = classes_dict.keys()
for i in buffer_list:
    classinfo = classes_dict.get(i)
    n = int(classinfo[0])
    section_list = []
    section_dict = {}
    start = 97
    for j in range(1, n+1):
        cl_sec = str(i) + chr(start)
        section_dict[cl_sec] = []
        section_list.append(str(cl_sec))
        start += 1
    add_class_subs = [classinfo[1], classinfo[2], section_dict]
    t_d_c[i] = add_class_subs

# Assigning Class Teachers
buffer_list = t_d_c.keys()
for i in buffer_list:
    classinfo = t_d_c.get(i)
    t_list = classinfo[1].copy()
    sections_dict = classinfo[2]
    buffer_list = sections_dict.keys()
    for j in buffer_list:
        sections_list = sections_dict.get(j)
        t_buffer = random.choice(t_list)
        t_list.remove(t_buffer)
        while t_list and teachers_dict[t_buffer][1]=='ct':
            t_buffer = random.choice(t_list)
            t_list.remove(t_buffer)
        if not t_list:
            print('Need more teachers')
            sys.exit()
        the_teacher = teachers_dict.get(t_buffer)
        the_teacher[1] = "ct"
        the_teacher_classes = the_teacher[2]
        the_teacher_clsub = the_teacher_classes.get(i)
        ct_sub = random.choice(the_teacher_clsub)
        sections_list.append([t_buffer, ct_sub])

# Creating Routine data
days = {"Mon": {}, "Tue": {}, "Wed": {}, "Thu": {}, "Fri": {}}
slots = 3

for i in days.keys():
    for j in t_d_c.keys():
        for k in t_d_c.get(j)[2].keys():
            day_dict = days.get(i)
            day_dict[k] = t_d_c.get(j)[2].get(k)

columns = {"Mon": {}, "Tue": {}, "Wed": {}, "Thu": {}, "Fri": {}}
for i in columns.keys():
    columns.get(i)[0] = [[], []]
    for j in t_d_c.keys():
        for k in t_d_c.get(j)[2].keys():
            columns.get(i).get(0)[0].append(t_d_c.get(j)[2].get(k)[0][0])
            columns.get(i).get(0)[1].append(t_d_c.get(j)[2].get(k)[0][1])
for i in range(1, slots):
    for j in columns.keys():
        columns.get(j)[i] = [[], []]

for i in days.keys():   # Mon, Tue, ...
    rw = 0
    for j in days.get(i).keys():    # Class8a, Class8b, ...
        for k in range(1, slots):    # 0, 1, 2
            subjects = t_d_c[sec_rem(j)][0].copy()
            repeat = True
            while(repeat):
                if not subjects:
                    print(columns)
                    print('Need more subject teachers')
                    sys.exit()
                nxt_subject = random.choice(subjects)
                subjects.remove(nxt_subject)
                for l in range(k):
                    if nxt_subject == columns.get(i).get(l)[1][rw]:
                        break
                    else:
                        if l == (k - 1):
                            repeat = False
            columns.get(i).get(k)[1].append(nxt_subject)
            repeat = True
            teachers = fetchconditions(sec_rem(j), nxt_subject, teachers_dict)
            while(repeat):
                if not teachers:
                    print(columns)
                    print('Need more subject teachers for classes')
                    sys.exit()
                nxt_teacher = random.choice(teachers)
                teachers.remove(nxt_teacher)
                if not (nxt_teacher in columns.get(i).get(k)[0]):
                    repeat = False
            columns.get(i).get(k)[0].append(nxt_teacher)
        rw += 1

# Printing teachers for reference
print('\nTeacher and their codes')
for i in teachers_dict:
    print(f"{i}: {teachers_dict[i][0]}")

# Printing routine
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
                n = 5 - len(str(columns.get(a).get(b)
                            [1][rw]) + str(columns.get(a).get(b)[0][rw]))
                print(
                    f"{columns.get(a).get(b)[1][rw]} - {columns.get(a).get(b)[0][rw]}{' '*n} | ", end='')
            print(f"\n{('-'*41)}")
        rw += 1