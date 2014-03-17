# -*- coding: utf-8 -*-
class Student(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25

s = Student()
print s.age()

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list

class XChain(object):
    def __init__(self, attr=''):
        self._attr = attr

    def __getattr__(self, attr):
        print 'self._attr: %s, attr: %s' % (self._attr, attr)
        return XChain('%s/%s' % (self._attr, attr))
        
    def __str__(self):
        return self._attr
        
    def __call__(self, arg0=''):
        print '__call__ %s(%s)' % (self._attr, arg0)
        return XChain('%s/%s' % (self._attr, arg0))
# 1.创建 A = XChain(),调用__init__方法进行初始化,此时 A 的self._attr=''
# 2.当 A 调用一个没有的属性users时,会根据__getattr__(self, attr)
#   创建一个新的 B = XChain('/users'),此时 B 的self._attr='/users'
# 3.通过__call__(self, arg0)进行instance()自身式的调用,返回一个新的 C = XChain('/users/abc'), 此时 C 的self._attr='/users/abc'
# 4.同2步骤创建一个新的 D = XChain('/users/abc/repos'),此时 D 的self._attr='users/abc/repos'
# 5.由于覆盖了原始的__str__(self)方法,所以最终的效果就是/users/:user/repos
print XChain().users('abc').repos('ddd').status.timeline()