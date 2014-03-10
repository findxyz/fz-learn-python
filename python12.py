import collections

# list = map(lambda x,y: x * y, (2, 3, 4), [5, 6, "a"])
# print list

# map(function, iterable, ...)
def my_map(f, *argsIt):
    for x in argsIt:
        if not isinstance(x, collections.Iterable):
            raise TypeError("argument must be a iterable type")

    itCount = len(argsIt)
    itLen = len(argsIt[0])
    result = []
    for j in range(itLen):
        args = []
        for i in range(itCount):
            args.append(argsIt[i][j])
        result.append(f(*args))
    return result

print my_map(lambda x,y: x * y, (1, 2, "a", 4), [1, 4, 3, 8])

print reduce(lambda x, y: x * y, [x if x < 0 else 6 for x in range(13)])
