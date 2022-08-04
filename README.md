# RoutineGenerator
Generate Annual schedule for schools

Run the RoutineGenerator.py file with the example test case given in testcase.txt

or... Create your own test case:

```
nC = Number of classes -> int()
nC times:
  class_name = Class number -> str()
  sec = Number of sections -> int()
  c = Number of subjects in this class -> int()
  c times:
    sub_name = name of the subject -> str()

nT = Number of teachers -> int()
nT times:
  t_name = Name of teacher -> str()
  class_num = Number of classes teached by this teacher -> int()
  class_num times:
    class_name = Corresponding class number -> str()
    sub_num = Number of subjects for the corresponding class -> int()
    sub_num times:
      sub_name = Name of subject -> str()
```
