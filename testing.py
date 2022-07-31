'''
buffer_list = t_d_c.keys()
for i in buffer_list:
    classinfo = t_d_c.get(i)
    sections_dict = classinfo[2]
    sections_list = sections_dict.keys()
    for j in sections_list:
        sectionsinfo_list = sections_dict.get(j)
        sectionsinfo_list.append({"Mon": [], "Tue": [], "Wed": [], "Thu": [], "Fri": []})
        section_days = sectionsinfo_list[1]
        buffer_list = section_days.keys()
        for k in buffer_list:
            the_day = section_days.get(k)
            the_day.append(sectionsinfo_list[0])

text = "stringa"
length = int(len(text)) - 1
print(text[0:length])

lst = [1,2,3]
print(1 in lst)

for i in range(0):
    print(i)

d = {1:'',2:'',3:''}
print(len(d))
    
'''
