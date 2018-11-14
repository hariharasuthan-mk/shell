import os
import sys
#print("hello from python start")
#print("hello from python end")

dir1     = []
file1    = []
rootDir = sys.argv[1]

def getlistdir_file(rootDir):
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        #print('Found directory: %s' % dirName)
        dir1.append(dirName)
        for filename in fileList:
            filepath = rootDir + filename
            #print('Found files: %s' % filepath)
            file1.append(filepath)
    mergedlist_file_dir = dir1 + file1
    print(mergedlist_file_dir)
getlistdir_file(sys.argv[1])
