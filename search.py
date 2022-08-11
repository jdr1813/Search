import os
import shutil
import pandas as pd

def findFile(name, path):
    print("*******************************************")
    print("\n\n\nlooking for filename " + name + "\n" )
    for root, subdirectories, files in os.walk(path):
        for file in files:
            if name.lower() in file.lower():
                finalPath = os.path.join(root, file)
                print("found file name at " + finalPath)
                return finalPath
    print(name + " not found")

def copyAndPasteFile(copyFolderPath, pasteFolderPath, fileList):
    badFiles = []
    goodFiles = []
    for file in fileList:
        try:
            filepath = findFile(file, copyFolderPath)
            shutil.copy(filepath, pasteFolderPath)
            goodFiles.append(file)
        except:
            badFiles.append(file)

    print("\n\n\nHere is a list of all of the files that weren't found but were in the excel sheet \n")

    for badFile in badFiles:
        print(badFile)
    print("There were " + str(len(badFiles)) + " files NOT found")

    print("\n\n\nHere is a list of all of the files that WERE found\n")

    for goodFile in goodFiles:
        print(goodFile)
    print("There were " + str(len(goodFiles)) + " files found")


def main():

    # For some reason on mac when you drag the folder in and it gets the path it has ' this character in the front and back of the string and it was causing it not to work.

    copyFolderPath = input(
        "Copy and paste the path of the folder you want to copy here: ").strip()
    copyFolderPath = copyFolderPath.replace("'", "")

    pasteFolderPath = input(
        "Copy and paste the path of the folder you want to paste those into here: ")
    pasteFolderPath = pasteFolderPath.replace("'", "").strip()

    neededFiles = input(
        "Copy and paste the path of the excel file you want to upload. The file MUST be in csv format: ")
    neededFiles = neededFiles.replace("'", "").strip()

    try:
        neededFiles = pd.read_csv(neededFiles)
        fileList = neededFiles[neededFiles.columns[0]].tolist()
    except:
        print("Not a valid csv file - Note format should be for example, E:\Folder/csvFileName")

    try:
        copyAndPasteFile(copyFolderPath, pasteFolderPath, fileList)
    except:
        print("Something wrong with the file path...")


main()
