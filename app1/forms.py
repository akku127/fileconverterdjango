from django import forms
from .models import WordFile, Jpgimage



class docxfileupload(forms.ModelForm):
    class Meta:
        model = WordFile
        fields = ['docxfile']

class imageform(forms.ModelForm):
    class Meta:
        model = Jpgimage
        fields = ['jpgfile']
