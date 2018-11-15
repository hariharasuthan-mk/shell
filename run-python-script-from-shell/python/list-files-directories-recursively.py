import os
import sys

dir1     = []
file1    = []
rootDir = sys.argv[1]

def getlistdir_file(rootDir):
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        dir1.append(dirName)
        for filename in fileList:
            filepath = rootDir + filename
            file1.append(filepath)
    mergedlist_file_dir = dir1 + file1
    print(mergedlist_file_dir)
    
getlistdir_file(sys.argv[1])
