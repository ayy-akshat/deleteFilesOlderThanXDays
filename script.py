import time
import os
import shutil

fp = "[file path here]"

d = 30 # older than this amount of days then delete the file

def deleteFilesOlderThanTimeInFolder(folderPath, days=30):
    if (os.path.exists(folderPath)):
        print("path exists")
        filenameList = os.listdir(folderPath)
        for filename in filenameList:
            if (os.path.isdir(folderPath + "/" + filename)):
                print("going into folder " + filename + "    {")
                deleteFilesOlderThanTimeInFolder(folderPath + "/" + filename)
                print("    }")
            else:
                print("file: " + filename)
                filestats = os.stat(folderPath + "/" + filename)
                fileCreation = filestats.st_birthtime
                now = time.time()
                fileLife = now - fileCreation
                fileLifeInDays = fileLife/(60*60*24)
                print("file: " + filename + "\n        has existed for " + str(fileLifeInDays) + " days")
                if (fileLifeInDays > days):
                    print("removing " + filename + "because " + str(fileLifeInDays) + " days old        (path: " + folderPath + "/" + filename + ")")
                    os.remove(folderPath + "/" + filename)
                time.time()
    else:
        print("path %s does not exist"%(folderPath))


deleteFilesOlderThanTimeInFolder(fp, d)