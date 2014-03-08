list = ['jack', 'mike', 'geek', 'johnny.R', 'tom']

# [start:stop:step]
# ['jack', 'mike', 'geek', 'johnny.R', 'tom']
# ['mike', 'geek', 'johnny.R', 'tom']
# ['mike', 'geek', 'johnny.R']
# ['jack', 'mike', 'geek', 'johnny.R']
# ['jack', 'johnny.R']#
print list[:]
print list[1:]
print list[1:4]
print list[:4]
print list[::3]
