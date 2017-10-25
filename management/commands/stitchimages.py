from __future__ import print_function
import sys
from PIL import Image

# The sys.argv object is an array of arguments passed to the script, where the name of the script is
# always the first object.
rows = int(sys.argv[1])
columns = int(sys.argv[2])
tempImage = Image.open(sys.argv[3])
tempImageSize = tempImage.size
completeImageSize = (tempImageSize[0] * rows, tempImageSize[1] * columns)

completeImage = Image.new('RGB', completeImageSize)
# begin stitching all the images together, starting from top left image and working across the row
# each row creates a new image made from pictures stitched together horizontally.
# at the end of the row, the new image is appended vertically to the final image.
for row in range(rows):
    for column in range(columns):
        tempImage = Image.open(sys.argv[3 + row + column])
        location = (row * tempImageSize[0], column * tempImageSize[1])
        completeImage.paste(tempImage, location)
completeImage.save("complete.png")

