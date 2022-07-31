import random

def write2file(filename, content):
    filename = str(filename) + ".txt"
    txt_file = open(filename, 'w')
    txt_file.write(str(content))
    txt_file.close()
    print("File updated")


teachers_dict = {
    1: ['avi', "", {
        'Class 8': ['s', 'm'],
        'Class 9': ['s', 'm']
    }],
    2: ['iva', "", {
        'Class 8': ['evs']
    }],
    3: ['avi2', "", {
        'Class 9': ['m']
    }],
    4: ['avi3', "", {
        'Class 8': ['e', 'sst', 'evs'],
        'Class 9': ['e']
    }],
    5: ['avi4', "", {
        'Class 8': ['s'],
        'Class 9': ['m']
    }],
    6: ['avi5', "", {
        'Class 8': ['m'],
        'Class 9': ['m']
    }],
    7: ['avi6', "", {
        'Class 8': ['s'],
        'Class 9': ['s']
    }],
    8: ['avi7', "", {
        'Class 9': ['m']
    }],
    9: ['avi8', "", {
        'Class 8': ['sst', 'evs', 'e']
    }],
    10: ['avi9', "", {
        'Class 9': ['e']
    }],
    11: ['avi10', "", {
        'Class 8': ['e'],
        'Class 9': ['e']
    }],
    12: ['avi11', "", {
        'Class 8': ['sst']
    }],
    13: ['avi12', "", {
        'Class 8': ['e', 'evs'],
        'Class 9': ['e']
    }],
    14: ['avi13', "", {
        'Class 8': ['sst', 'evs'],
        'Class 9': ['e']
    }],
    15: ['avi14', "", {
        'Class 8': ['evs'],
        'Class 9': ['s']
    }]
}

t_d_c = {
    'Class 8': [['s', 'm', 'e', 'sst', 'evs'], [1, 2, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15], {
        'Class 8a': [],
        'Class 8b': [],
        'Class 8c': []
    }],
    'Class 9': [['s', 'm', 'e'], [1, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15], {
        'Class 9a': [], 
        'Class 9b': [], 
        'Class 9c': []
    }]
}

buffer_list = t_d_c.keys()
for i in buffer_list:
    classinfo = t_d_c.get(i)
    t_list = classinfo[1]
    sections_dict = classinfo[2]
    buffer_list = sections_dict.keys()
    for j in buffer_list:
        sections_list = sections_dict.get(j)
        ct_check = True
        while(ct_check):
            t_buffer = random.choice(t_list)
            the_teacher = teachers_dict.get(t_buffer)
            if str(the_teacher[1]) != "ct":
                the_teacher[1] = "ct"
                ct_check = False
        the_teacher_classes = the_teacher[2]
        the_teacher_clsub = the_teacher_classes.get(i)
        ct_sub = random.choice(the_teacher_clsub)
        sections_list.append([t_buffer, ct_sub])


write2file("Teachers", teachers_dict)
write2file("ClassesWithCT", t_d_c)
