def write2file(filename, content):
    filename = str(filename) + ".txt"
    txt_file = open(filename, 'w')
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


n = int(input("Number of Classes: "))
classes_dict = {}
for i in range(1,n+1):
    class_list = []
    class_name = input(f"\nName of {numsuffix(int(i))} class: ")
    sec = int(input("Number of sections of this class: "))
    class_list.append(sec)
    c = int(input("Number of subjects in this class: "))
    sub_list = []
    for j in range(1,c+1):
        sub_name = input(f"Name of {numsuffix(int(j))} subject: ")
        sub_list.append(sub_name)
    class_list.append(sub_list)
    classes_dict["Class " + str(class_name)] = class_list

write2file("Classes", classes_dict)