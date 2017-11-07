from django import template
from django.shortcuts import render
from pantry.models import Pantry
from PIL import Image

register = template.Library()

@register.inclusion_tag
def pantryImage():
        myPantry = Pantry.objects.get(name="myPantry")
        fileUrl = myPantry.createImage("/home/oscar/Pictures/pantryImages/")
        return response

