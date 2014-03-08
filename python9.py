# iterator
from collections import Iterable
list = ['a', 'ab', 'abc']
tuple = (1, 2, 'a')
dic = {'ak': 'ak-v', 'bk': 'bk-v', 'ck': 'ck-v'}
s = set([1, 2, 3, 4])
str = 'abcdefg'

for l in list:
    print "l in list", l

for t in tuple:
    print "t in tuple", t

for k in dic:
    print "k in dic", k

for k, v in dic.iteritems():
    print "k, v in dic.iteritems()", k, v

for v in dic.itervalues():
    print "v in dic.itervalues()", v

print "isinstance(dic, Iterable)", isinstance(dic, Iterable)

for i, v in enumerate(s):
    print "i, v in enumerate(s)", i, v

for ch in str:
    print "ch in str", ch

for x, y in (('a', 'b'),('c', 'd'),('e', 'f')):
    print "x, y in (('a', 'b'),('c', 'd'),('e', 'f'))", x, y

for x in (('a', 'b'),('c', 'd'),('e', 'f')):
    print "x in (('a', 'b'),('c', 'd'),('e', 'f'))", x
