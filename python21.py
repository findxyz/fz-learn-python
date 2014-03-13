with open('test.txt') as f:
    for line in f:
        print line,

f = file('test.txt')
for line in f:
    print line,
f.close()

f2 = open('test.txt')
for line in f2:
    print line,
f2.close()

f3 = file('abc.txt', 'w')
f3.write('python io create file')
f3.close()

f4 = file('abc.txt', 'a')
f4.write('\nadded something')
f4.close()

a = object()
print dir(a)
