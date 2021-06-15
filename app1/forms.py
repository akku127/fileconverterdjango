from django import forms
from .models import WordFile, Jpgimage, Pngimage



class docxfileupload(forms.ModelForm):
    class Meta:
        model = WordFile
        fields = ['docxfile']

class imageform(forms.ModelForm):
    class Meta:
        model = Jpgimage
        fields = ['jpgfile']

class pngform(forms.ModelForm):
    class Meta:
        model = Pngimage
        fields = ['pngfile']
