# decorator
import functools

def log(func_txt):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kw):
            print 'begin call'
            print func_txt
            func(*args, **kw)
            print 'end call'
        return wapper

    def decorator2():
        @functools.wraps(func_txt)
        def wapper2(*args, **kw):
            print 'begin call'
            func_txt(*args, **kw)
            print 'end call'
        return wapper2

    if hasattr(func_txt, '__call__'):
        return decorator2()
    else:
        return decorator

@log('execute')
def now():
    print '2014-03-09'

now()

@log
def now2():
    print '2014-03-10'

now2()
