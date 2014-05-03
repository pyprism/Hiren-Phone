__author__ = 'prism'

import re , os

f = open('../sample/0724 Mithila.vmg')

#regexp = re.compile(r'(?P<Phone>VOICE:[\d]+)?' r'(?P<Name>[^\w]N:[\d\s\w$].+)?')
#matchObj = re.match( r'\+\d+', f.read())

#matchObj = regexp.search(f.read())

#print f.read()
#print "Phone" , matchObj.group('Phone')
#print "Name" , matchObj.group('Name')




#print f.read().decode('utf-16')

#name = re.compile(r'[^\w]N:[\d\s\w].+')
#name = re.compile(r'N')

# x = re.search( r'[^N:][\d\w]+' , 'N:Afroza')
#
# print x.group(0)

number = re.search(r'[TEL:+]\d+\n' , f.read().decode('utf-16'))
print number.group()



#date = re.findall(r'[Date]:[\d\.]+' , f.read().decode('utf-16'))

#print date[0].lstrip('e:')

# regexp = re.compile(r'(?P<number>[TEL:+]\d+\n)')
# m = regexp.search(f.read().decode('utf-16'))
#
# print m.group('number')
# print m.group('date')
f.close()

