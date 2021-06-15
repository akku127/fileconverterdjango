from django.contrib import admin
from .models import WordFile, Jpgimage, Pngimage
# Register your models here.
admin.site.register(WordFile)
admin.site.register(Jpgimage)
admin.site.register(Pngimage)
