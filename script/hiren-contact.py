#!/usr/bin/env python

import pymongo , re ,os

def main():
    filelist = os.listdir('../sample/')
    for i in filelist:
        if i.endswith('.vcf'):
            fileContent = open('../sample/' + i )
            fileContent.read()



if __name__ == '__main__':
    main()