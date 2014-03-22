# -*- coding: utf-8 -*-
dict = {
    "fz": 26,
    "xx": 27
}
dict["cc"] = 28
print dict["fz"]
print dict.get("aa")
print dict.get("bb", "not found")
print dict
print dict.pop("cc")
print dict

#key = [1, 2, 3]
#dict[key] = "1 2 3"

s = set([1, 2, 3, 1])
print s
s.add(4)
print s
s.remove(1)
print "s:", s

s2 = set([3, 4, 5])
print 's2:', s2

s3 = s & s2
print "s3=s & s2:", s3

s4 = s | s2
print "s4=s | s2:", s4

tuple = (
    1,
    2,
    3,
)
tuple2 = (1, [2, 3])

s.add(tuple)
print "s.add(1, 2, 3):", s
s.add(tuple2)
print "s.add(1, [2, 3]):", s

