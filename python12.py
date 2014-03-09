def my_map(f, *list):
    newList = []
    for x in list:
        newList.append(f(x))
    return newList

def my_func(x):
    if isinstance(x, (int, float)):
        return x * x
    else:
        return "is not number"

print my_map(my_func, *(1, 2, "abc", 4))

list = map(lambda x,y: x * y, (2, 3, 4), [5, 6, "a"])
print list