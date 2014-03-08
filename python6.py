def myAbs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def blankFuc():
    pass

def calc(*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum

def power(x, n=2):
    sum = 1
    while(n > 0):
        n -= 1
        sum *= x
    return sum

    
def person(name, age, **kw):
    print "name:", name, "age:", age, "other:", kw

def argFunc(a, b, c=0, *args, **kw):
    print 'a', a
    print 'b', b
    print 'c', c
    print 'args', args
    print 'kw', kw
    
print myAbs(-200)
#print myAbs('A')
blankFuc()

print power(5)
print power(5, 3)

list = range(101)
print calc(*list)
print calc(1, 2)

person("et", "??", height="very high", width="so large")
person("fz", 26, **{"sex": "male"})

argFunc(1, 2, 12, *('hello', 'world'), keyword1='keyword first', keyword2='am keyword second')
argFunc(1, 2, 13, 1, 4, 5, **{"key": "hello", "word": "world"})

args = (1, 4, 16, 0)
kw = {"key-a": 'value-a', "key-b": 'value-b'}
# args filled a & b & c
argFunc(*args, **kw)

