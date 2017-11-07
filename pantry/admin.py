from django.contrib import admin
from .models import Pantry

admin.site.register(Pantry)
#https://stackoverflow.com/questions/16307307/django-admin-show-image-from-imagefield
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)
