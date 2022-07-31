def write2file(filename, content):
    filename = str(filename) + ".txt"
    txt_file = open(filename, 'w')
    txt_file.write(str(content))
    txt_file.close()
    print("File updated")


classes_dict = {
    'Class 8': [3, ['s', 'm', 'e', 'sst', 'evs'], [1, 2, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15]],
    'Class 9': [3, ['s', 'm', 'e'], [1, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15]]
}

t_d_c = {}
buffer_list = classes_dict.keys()
for i in buffer_list:
    classinfo = classes_dict.get(i)
    n = int(classinfo[0])
    section_list = []
    section_dict = {}
    start = 97
    for j in range(1,n+1):
        cl_sec = str(i) + chr(start)
        section_dict[cl_sec] = []
        section_list.append(str(cl_sec))
        start += 1
    add_class_subs = [classinfo[1], classinfo[2], section_dict]
    t_d_c[i] = add_class_subs

write2file("ClassesWithSections", t_d_c)
