__author__ = 'prism'

import re

f = open('../sample/Afroza.vcf')

#regexp = re.compile(r'(?P<Phone>VOICE:[\d]+)?' r'(?P<Name>[^\w]N:[\d\s\w$].+)?')
#matchObj = re.match( r'\+\d+', f.read())

#matchObj = regexp.search(f.read())

#print f.read()
#print "Phone" , matchObj.group('Phone')
#print "Name" , matchObj.group('Name')



counter = 0
for i in f.readlines():
    if counter == 2:
        name = re.search(r'[^N:][\d\w]+' , i)
    elif counter == 3:
        phone = re.search(r'[^VOICE:][\d]+' , i)
    else:
        pass
    counter = counter + 1
print name.group()
print phone.group()

#name = re.compile(r'[^\w]N:[\d\s\w].+')
#name = re.compile(r'N')

# x = re.search( r'[^N:][\d\w]+' , 'N:Afroza')
#
# print x.group(0)