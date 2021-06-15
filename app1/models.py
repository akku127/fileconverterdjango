from django.db import models

from docx2pdf import convert
# Create your models here.

class WordFile(models.Model):
    docxfile = models.FileField(upload_to='docxs')
    pdf = models.FileField(upload_to='docxs', null=True)
    text = models.CharField(max_length=100, null=True)

class Jpgimage(models.Model):
    jpgfile = models.FileField(upload_to='images')

class Pngimage(models.Model):
    pngfile = models.FileField(upload_to='images')
