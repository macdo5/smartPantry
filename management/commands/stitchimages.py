from __future__ import print_function
import sys
import os.path
import datetime
from PIL import Image

def createImage(dirPath, rows, columns):
    fileUrl = constructFileUrl(dirPath, 0, 0)
    tempImage = Image.open(fileUrl)
    tempImageSize = tempImage.size
    completeImageSize = (tempImageSize[0] * columns, tempImageSize[1] * rows)

    completeImage = Image.new('RGB', completeImageSize)
    # begin stitching all the images together, starting from top left image and working across the row
    # each row creates a new image made from pictures stitched together horizontally.
    # at the end of the row, the new image is appended vertically to the final image.
    for column in range(columns):
        for row in range(rows):
            fileUrl = constructFileUrl(dirPath, row, column)
            tempImage = Image.open(fileUrl)
            location = (column * tempImageSize[0], row * tempImageSize[1])
            completeImage.paste(tempImage, location)
    now = datetime.datetime.now()
    strNow = str(now) + ".jpg"
    completeImage.save(strNow)

def directoryExists(dirPath):
    exists = os.path.exists(dirPath)
    return exists

def allPicturesReadable(dirPath, rows, columns):
    # check every image in the grid
    for column in range(columns):
        for row in range(rows):
            # build the full file url
            fileUrl = constructFileUrl(dirPath, row, column)
            if not os.path.isfile(fileUrl): 
                return False # if the file does not exist, return false (error: not all files exist)
            if not os.access(fileUrl, os.R_OK): 
                return False # if the user running the script does not have read access, return false (error: not all files readable)
    # if everey file checks out, return true
    return True

def constructFileUrl(dirPath, row, column):
    return dirPath + str(row) + "_" + str(column) + ".jpg"

# The sys.argv object is an array of arguments passed to the script, where the name of the script is
# always the first object.
rows = 1 #int(sys.argv[1])
columns = 10 #int(sys.argv[2])
dirPath = "/home/oscar/Pictures/pantryImages/" #sys.argv[3]
# check if the user has added a slash on the end of the directory path argument. If not, add one.
if dirPath[-1:] != "/": dirPath += "/"
# convert ~ and ~user of the dirPath into $HOME
dirPath = os.path.expanduser(dirPath)
if directoryExists(dirPath):
    if allPicturesReadable(dirPath, rows, columns):
        createImage(dirPath, rows, columns)
    else: print("Not all pictures are readable")
else: print("directory does not exist")
