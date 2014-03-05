# -*- coding: utf-8 -*-
import sys
type = sys.getdefaultencoding()
print 'sysdefaultencoding is %s' % type
a = '哈哈'.decode('utf-8').encode('gb2312')
b = a
a = '2014-03-05'
print 'Hi, your word is %s , and today is %s' % (b, a)
