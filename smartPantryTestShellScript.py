from pantry.models import Pantry
myPantry = Pantry.objects.get(name="myPantry")
myPantry.createImage("/home/oscar/Pictures/pantryImages/")
print("name: " + myPantry.completeImage.name)
print("path: " + myPantry.completeImage.path)
print("url: " + myPantry.completeImage.url)
print(myPantry.completeImage)