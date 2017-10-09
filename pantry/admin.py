from django.contrib import admin
from .models import Pantry, PantryImage, WeightedItem

admin.site.register(Pantry)
admin.site.register(PantryImage)
admin.site.register(WeightedItem)
#https://stackoverflow.com/questions/16307307/django-admin-show-image-from-imagefield
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)
