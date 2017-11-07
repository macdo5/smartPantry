from __future__ import print_function
from django.db import models
from django.utils import timezone
import sys
import os.path
import datetime
from PIL import Image

class Pantry(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)
    columns = models.IntegerField() # the number of columns in the 2D array of images
    rows = models.IntegerField()    # the number of rows in the 2D array of images
    completeImage = models.ImageField(null=True, blank=True, upload_to='media') # stores a picture of the complete pantry 
    
    def update(self):
        # this is where all images have to be updated (or maybe that belongs to PantryImage?)
        self.last_update = timezone.now()
        self.save()
    
    def __str__(self):
        return self.name

    def directoryExists(self, dirPath):
        exists = os.path.exists(dirPath)
        return exists

    def constructFileUrl(self, dirPath, row, column):
        return dirPath + str(row) + "_" + str(column) + ".jpg"

    def allPicturesReadable(self, dirPath):
        # check every image in the grid
        for column in range(self.columns):
            for row in range(self.rows):
                # build the full file url
                fileUrl = self.constructFileUrl(dirPath, row, column)
                if not os.path.isfile(fileUrl): 
                    return False # if the file does not exist, return false (error: not all files exist)
                if not os.access(fileUrl, os.R_OK): 
                    return False # if the user running the script does not have read access, return false (error: not all files readable)
        # if everey file checks out, return true
        return True

    def createImage(self, dirPath):
        fileUrl = self.constructFileUrl(dirPath, 0, 0)
        tempImage = Image.open(fileUrl)
        tempImageSize = tempImage.size
        newCompleteImageSize = (tempImageSize[0] * self.columns, tempImageSize[1] * self.rows)

        newCompleteImage = Image.new('RGB', newCompleteImageSize)
        # begin stitching all the images together, starting from top left image and working across the row
        # each row creates a new image made from pictures stitched together horizontally.
        # at the end of the row, the new image is appended vertically to the final image.
        for column in range(self.columns):
            for row in range(self.rows):
                fileUrl = self.constructFileUrl(dirPath, row, column)
                tempImage = Image.open(fileUrl)
                location = (column * tempImageSize[0], row * tempImageSize[1])
                newCompleteImage.paste(tempImage, location)
        now = datetime.datetime.now()
        strNow = str(now) + ".jpg"
        self.completeImage = newCompleteImage
        self.save()
        path = os.getcwd() + "/" + strNow
        return path
