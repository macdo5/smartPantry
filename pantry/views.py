from django.shortcuts import render
from .models import Pantry

# Create your views here. 
def main(request):
        myPantry = Pantry.objects.get(name="myPantry")
        myPantry.createImage("/home/oscar/Pictures/pantryImages/")
        return render(request, 'pantry/main.html', {'myPantry': myPantry})