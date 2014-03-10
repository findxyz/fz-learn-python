import functools
def f(a, b, c):
    print a
    print b
    print c

f_ac = functools.partial(f, a=1, c=3)

f_ac(b=2)

f_bc = functools.partial(f, b='b', c='c')

f_bc('a')