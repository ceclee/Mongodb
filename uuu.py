
import re
try:
    a = re.compile(r'''(?P<liyang>ab)#this is group1
        cd
        (?P<dog>ef)''',re.X)
    l = a.search('abcdeffghiabcdef')
    # print(l)
    print(l.group())
    # print(l.lastgroup)
    # print(l.lastindex)
    # print(l.re)
    # print(l.endpos)
    # print(l.start())
    # print(l.group(2))
    # print(l.groupdict())
except AttributeError:
    print('powpow') 
    