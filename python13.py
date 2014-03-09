def build(x, y):
    return lambda z: x * x + y * y + z

f = build(1, 2);
print f(3)
