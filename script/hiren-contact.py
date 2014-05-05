#Date : May 1 , 2014 . Hiren is Missing for 1 month
#Just for contacts
#!/usr/bin/env python


import pymongo, re, os, shutil, time

client = pymongo.MongoClient()
db = client['Hiren-Phone']
collection = db['Contacts']


def filemove(name,location,moveornot):
    if not os.path.exists('../sample/finishedContact/'):
        os.mkdir('../sample/finishedContact/')
    if not os.path.exists('../sample/duplicateContact/'):
        os.mkdir('../sample/duplicateContact/')
    if not moveornot:
        shutil.move('../sample/' + name, '../sample/finishedContact/' + name)


def database(name, number):
    duplicate = collection.find_one({'Number': number})
    if not duplicate:
        data = {'Name': name,
                'Number': number,
                'Another Name': '',
                'Time': time.strftime('%d-%m-%Y')}
        collection.insert(data, safe=True)
        print str(name).upper() + ' Is Added'
    elif duplicate['Name'] == name:
        print str(name) + ' is already exist'
    else:
        collection.update({"_id": duplicate["_id"]},
                          {'Another Name': duplicate['Another Name'] + '  ' + name},
                          upsert=False
        )
        print str(name) + ' is updated'


def main():
    filelist = os.listdir('../sample/')
    for i in filelist:
        counter = 0
        moveornot = ""
        if i.endswith('.vcf'):
            fileContent = open('../sample/' + i)
            for lines in fileContent.readlines():
                if counter == 2:
                    if lines.startswith('N;ENCODING'):
                        print 'Special Case detected ' + i  # N;ENCODING=QUOTED-PRINTABLE:
                        moveornot = True
                    else:
                        name = re.search(r'[^N:][\d\w\s]+', lines)
                elif counter == 3:
                    phone = re.search(r'[^VOICE:][\d\*\+\#]+', lines)
                counter = counter + 1
            fileContent.close()
            database(name.group()[:-2], phone.group())


if __name__ == '__main__':
    main()

