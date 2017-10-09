from django.db import models
from django.utils import timezone

class Pantry(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)
    columns = models.IntegerField() # the number of columns in the 2D array of images
    rows = models.IntegerField()    # the number of rows in the 2D array of images
    
    def update(self):
        # this is where all images have to be updated (or maybe that belongs to PantryImage?)
        self.last_update = timezone.now()
        self.save()
    
    def __str__(self):
        return self.name
    

# from https://stackoverflow.com/questions/17672945
# from https://stackoverflow.com/questions/537593
def pantry_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'pantry_{0}/{1}'.format(instance.pantry.id, filename)

class PantryImage(models.Model):
    pantry = models.ForeignKey(Pantry, related_name='images', on_delete=models.CASCADE, blank=False) # a PantryImage belongs to a single pantry.
    image = models.ImageField(upload_to='pantry_image_path', blank=True) # stores the image file
    column = models.IntegerField() # the location in columns the PantryImage belongs
    row = models.IntegerField()    # the location in rows the PantryImage belongs


class WeightedItem(models.Model):
    pantry = models.ForeignKey(Pantry, blank=False) # a WeightedItem belongs to a single pantry.
    itemName = models.CharField(max_length=200)
    grams = models.IntegerField() # the weight in grams of the item.
