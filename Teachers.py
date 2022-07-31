def write2file(filename,content):
    filename = str(filename) + ".txt"
    txt_file = open(filename,'w')
    txt_file.write(str(content))
    txt_file.close()
    print("File updated")


def numsuffix(num):
    # adding suffix to number
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


n = int(input("Number of Teachers: "))
teachers_dict = {}
for i in range(1,n+1):
    t_list = []
    t_name = input(f"\nName of {numsuffix(int(i))} teacher: ")
    t_list.append(t_name)
    t_list.append("")
    classes_dict = {}
    class_num = int(input("\tNumber of classes to be teached: "))
    for j in range(1,class_num+1):
        class_name = input(f"\tName of {numsuffix(int(j))} class: ")
        class_name = "Class " + str(class_name)
        sub_num = int(input(f"\tNumber of subjects to be teached in {class_name}: "))
        sub_list = []
        for k in range(1, sub_num+1):
            sub_name = input(f"\tName of {numsuffix(int(k))} subject: ")
            sub_list.append(sub_name)
        classes_dict[class_name] = sub_list
    t_list.append(classes_dict)
    teachers_dict[i] = t_list

write2file("Teachers",teachers_dict)
