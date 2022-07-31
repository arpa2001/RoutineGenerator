def write2file(filename, content):
    filename = str(filename) + ".txt"
    txt_file = open(filename, 'w')
    txt_file.write(str(content))
    txt_file.close()
    print("File updated")


classes_dict = {
    'Class 8': [3, ['s', 'm', 'e', 'sst', 'evs']],
    'Class 9': [3, ['s', 'm', 'e']]
}

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

write2file("ClassesWithTeachers", classes_dict)
