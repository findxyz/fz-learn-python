import os
list = range(1, 11)
print list

list2 = [x * x for x in range(1, 11)]
print list2

list3 = [x * 2 for x in range(1, 11) if x % 2 == 0]
print list3

list4 = [m + n for m in "ABC" for n in "XYZ"]
print list4

list5 = [d for d in os.listdir('.')]
print list5

dic = {"pythonMap": "dict", "javaMap": "HashMap"}
list6 = [k + '=' + v for k, v in dic.iteritems()]
print list6

list7 = ["HelloWorld", "HelloPython"]
list8 = [s.lower() for s in list7]
print list8

list9 = ["HelloWorld", "Hello123", 123]
list10 = [s.lower() for s in list9 if isinstance(s, str)]
print list10

list11 = [str(x) + "_even" if x % 2 == 0 else str(x) + "_odd" for x in range(1, 11)]
print list11