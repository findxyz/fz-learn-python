# generator
# g = (x * x for x in range(1, 11))
# print g

# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()

# for i in g:
#     print i

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

fibg2 = fib(2)

for g in fibg2:
    print g

def odd():
    print 'step 1'
    yield 1
    print 'step 3'
    yield 3
    print 'step 5'
    yield 5

o = odd()

for obj in o:
    print obj
