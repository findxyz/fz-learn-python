age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

names = ['mike', 'zhangsan', 'lisi']
for name in names:
    print name

sum = 0
for i in range(101):
    sum += i
print sum

sum = 0
n = 99
while n > 0:
	sum += n
	n -= 2
print sum

while sum > 0:
    print 'Endless loop'