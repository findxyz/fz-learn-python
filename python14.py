# decorator
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kw):
            print 'call %s %s()' % (text, func.__name__)
            return func(*args, **kw)
        return wapper
    return decorator

@log('execute')
def now():
    print '2014-03-09'

f = now
print f.__name__
f()

