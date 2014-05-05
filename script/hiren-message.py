__author__ = 'prism'
#Date : May 2 , 2014 . Hiren is Missing for 1 month
#Just for messages !
#!/usr/bin/env python

import pymongo, re, os, shutil

client = pymongo.MongoClient()
db = client['Hiren-Phone']
collection = db['Message']


def database(number, filename, message, date, timer, boxtype):
    duplicate = collection.find_one({'Number': number, 'Message': message, 'Date': date, 'Time': timer})
    if not duplicate:
        data = {'Number': number,
                'Message': message,
                'Date': date,
                'Time': timer,
                'Box Type': boxtype,
                'File Name': filename}
        collection.insert(data, safe=True)
        print 'Data Inserted ;) Hiren ! '
    else:
        print 'Duplicate message'


def main():
    filelist = os.listdir('../sample/')
    for i in filelist:
        if i.endswith('.vmg'):
            filecontent = open('../sample/' + i)
            number = re.search(r'[TEL:+]\d+\n', filecontent.read().decode('utf-16'))
            filecontent.seek(0, 0)  # Reset pointer
            timer = re.search(r'\d\d:\d\d:\d\d', filecontent.read().decode('utf-16'))
            filecontent.seek(0, 0)
            date = re.search(r'[Date]:[\d\.]+', filecontent.read().decode('utf-16'))
            filecontent.seek(0, 0)
            tempmesg = re.search(r'\d\d:\d\d:\d\d\n[\s\w\d:)><%^&*-@!#\t\/{}.]+', filecontent.read().decode('utf-16'))
            message = tempmesg.group().strip('END:VBODY\nEND:VENV\nEND:VENV\nEND:VMSG')[9:]
            filecontent.seek(0, 0)
            #Check message box type
            boxA = re.search(r'DRAFT', filecontent.read().decode('utf-16'))
            if boxA:
                boxtype = 'Draft'
            filecontent.seek(0, 0)
            if re.search(r'DELIVER', filecontent.read().decode('utf-16')):
                boxtype = 'Inbox'
            filecontent.seek(0, 0)
            if re.search(r'SUBMIT', filecontent.read().decode('utf-16')):
                boxtype = 'Sent'
            #Move sorted files to different folder
            if not os.path.exists('../sample/finishedMessage/'):
                os.mkdir('../sample/finishedMessage/')
            shutil.move('../../sample/' + i, '../../sample/finishedMessage/' + i)
            filecontent.close()
            database(number.group()[:-1], i, message, date.group().lstrip('e:'), timer.group(), boxtype)

if __name__ == '__main__':
    main()