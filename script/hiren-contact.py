#Date : May 1 , 2014 . Hiren is Missing for 1 month
#Just for contacts
#!/usr/bin/env python


import pymongo , re ,os,shutil ,time

def Database(name,number):
    client = pymongo.MongoClient()
    db = client['Hiren-Phone']
    collection = db['Contacts']
    duplicate = collection.find_one({'Number' : number})
    if not duplicate:
        data = { 'Name' : name ,
             'Number' : number ,
             'Another Name' : '' ,
             'Time' : time.strftime('%d-%m-%Y' )}
        collection.insert(data)
        print str(name).upper() + ' Is Added'
    elif duplicate['Name'] == name:
        print str(name) + ' is already exist'
    else:
        collection.update({
            "_id" : duplicate["_id"],
            'Another Name' : duplicate['Another Name'] + ', ' + name
        })
        print str(name) + ' is updated'


def main():
    filelist = os.listdir('../sample/')
    for i in filelist:
        counter = 0
        if i.endswith('.vcf'):
            fileContent = open('../sample/' + i )
            for i in fileContent.readlines():
                if counter == 2:
                    name = re.search(r'[^N:][\d\w\s]+' , i)
                elif counter == 3:
                    phone = re.search(r'[^VOICE:][\d\*\+\#]+' , i)
                else:pass
                counter = counter + 1
            fileContent.close()
            if not os.path.exists('../sample/finalContact/'):
                os.mkdir('../sample/finalContact/')
                os.chdir("../sample/finalContact/")
            else:
                os.chdir("../sample/finalContact/")
            shutil.move('../sample/' + i , '../sample/finalContact/' + i)
            Database(name.group(),phone.group())




if __name__ == '__main__':
    main()

