from django import template
from django.shortcuts import render
from pantry.models import Pantry
from PIL import Image

register = template.Library()

@register.filter
def pantryImage():
        myPantry = Pantry.objects.get(name="myPantry")
        fileUrl = myPantry.createImage("/home/oscar/Pictures/pantryImages/")
        pantryImage = Image.open(fileUrl)
        response = HttpResponse(mimetype="image/jpg")
        pantryImage.save(response, "JPG")
        return response

