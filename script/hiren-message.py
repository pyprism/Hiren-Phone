__author__ = 'prism'
#Date : May 2 , 2014 . Hiren is Missing for 1 month
#Just for messages !
#!/usr/bin/env python

import pymongo,re,os,shutil,time

client = pymongo.MongoClient()
db = client['Hiren-Phone']
collection = db['Message']


def database(number,filename,message,date,time,boxtype):
    pass


def main():
    filelist = os.listdir('../sample/')
    for i in filelist:
        if i.endswith('.vmg'):
            filecontent = open('../sample/' + i)
            number = re.search(r'[TEL:+]\d+\n', filecontent.read().decode('utf-16'))

            filecontent.close()