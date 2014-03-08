# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
a = u'哈哈'
b = a
a = '2014-03-05'
print 'Hi, your word is %s , and today is %s' % (b, a)

print u'中文'