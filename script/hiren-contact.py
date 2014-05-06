#Date : May 1 , 2014 . Hiren is Missing for 1 month
#Just for contacts
#!/usr/bin/env python


import pymongo, re, os, shutil, time

client = pymongo.MongoClient()
db = client['Hiren-Phone']
collection = db['Contacts']


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
                          {"$set": {'Another Name': duplicate['Another Name'] + '  ' + name}},
                          safe=True
        )
        print str(name) + ' is updated'


def main():
    filelist = os.listdir('../sample/')
    for i in filelist:
        counter = 0
        if i.endswith('.vcf'):
            fileContent = open('../sample/' + i)
            number = re.findall(r'[^VOICE:][\d\*\+\#]+', fileContent.read())
            fileContent.seek(0, 0)
            for lines in fileContent.readlines():
                if counter == 2:
                    if lines.startswith('N;ENCODING'):  # N;ENCODING=QUOTED-PRINTABLE:
                        name = lines[28:-1]
                        database(name, number[-1])
                    else:
                        name = re.search(r'[^N:][\d\w\s]+', lines)
                        #print i
                        database(name.group()[:-2], number[-1])
                counter = counter + 1
            fileContent.close()
            if not os.path.exists('../sample/finishedContact/'):
                os.mkdir('../sample/finishedContact/')
            shutil.move('../sample/' + i, '../sample/finishedContact/' + i)
            #if not name.group() is None or phone.group() is None:



if __name__ == '__main__':
    main()

