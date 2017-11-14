from django.shortcuts import render
from .models import Pantry
import os

# Create your views here. 
def main(request):
        myPantry = Pantry.objects.get(name="myPantry") # get the pantry called myPantry
	home_dir = os.getenv("HOME")	# get the user home directory
	pantry_image_dir = home_dir + "/Pictures/pantryImages/"	# create the pantry images file url: ~/Pictures/pantryImages
	# if it doesn't exist, make it.
	if not os.path.exists(pantry_image_dir):
    		os.makedirs(pantry_image_dir)
	# create the images in the file.
        myPantry.createImage(pantry_image_dir)
        return render(request, 'pantry/main.html', {'myPantry': myPantry})
