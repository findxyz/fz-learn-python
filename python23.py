class MyDecorator(object):
    def __init__(self, fn):
        print 'inside MyDecorator.__init__()'
        self._fn = fn

    def __call__(self):
        print 'inside MyDecorator.__call__()'
        self._fn()
        print 'MyDecorator decorates func name is: %s' % self._fn.__name__

@MyDecorator
def MyFunc():
    print 'This is a func'

print 'MyDecorator is decorating a func'

MyFunc()