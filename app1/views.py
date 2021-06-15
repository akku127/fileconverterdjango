from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from .models import WordFile, Jpgimage, Pngimage
from docx2pdf import convert
from .forms import docxfileupload, imageform, pngform
import pythoncom
from PIL import Image

import os
import glob


def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer


def index(request):
    print(request)
    success = False
    docxform = docxfileupload()
    jpgform = imageform()
    pngforms = pngform()
    context = {'docxform': docxform, 'success': success, 'jpgform': jpgform, 'pngform': pngforms}
    return render(request, 'app1/index.html', context)


def converter1(request):
    pythoncom.CoInitialize()
    print('inside docx converter')
    if not get_referer(request):
        raise Http404
    file = WordFile.objects.latest('id')
    file_path = file.docxfile.url[1:]
    print('file path:  ->->->   ')
    print(file_path)
    convert(file_path)
    file_last = file.docxfile.url[:-4]
    print('file_last')
    print(file_last)
    pdf_url = 'http://e0932e8bc9f4.ngrok.io' + file_last + "pdf"
    print('pdf_url')
    print(pdf_url)
    context = {'url': pdf_url}
    return render(request, 'app1/wait.html', context)


def docxtopdf(request):
    if request.method == 'POST':
        print(request.method)
        form = docxfileupload(request.POST, request.FILES)
        file_name = request.FILES['docxfile'].name
        print('filename:')
        print(file_name)
        file_type = file_name[-4:]
        print(file_type)
        if file_type == 'docx':
            if form.is_valid():
                form.save()
                success = True
                return redirect('convertdocx')
        else:
            messages.info(request, 'Wrong filetype provided')
            return redirect('index')
    else:
        return Http404


def converter2(request):
    pythoncom.CoInitialize()
    print('inside jpg converter')
    file = Jpgimage.objects.latest('id')
    file_path = file.jpgfile.url[1:]
    print('file path:  ->->->   ')
    print(file_path)
    pngname = file_path[:-3] + 'png'
    print(pngname)
    im1 = Image.open(file_path)
    im1.save(pngname)
    png_url = 'http://e0932e8bc9f4.ngrok.io/' + pngname
    print(png_url)
    context = {'url': png_url}
    return render(request, 'app1/wait.html', context)


def jpgtopng(request):
    if request.method == 'POST':
        form = imageform(request.POST, request.FILES)
        file_name = request.FILES['jpgfile'].name
        print('file name: ')
        print(file_name)
        file_type = file_name[-3:]
        print('file type: ')
        print(file_type)
        if file_type == 'jpg':
            if form.is_valid():
                form.save()
                return redirect('convertjpg')
        else:
            messages.info(request, 'wrong file type provided')
            return redirect('index')
    else:
        return Http404

def pngtojpg(request):
    if request.method == 'POST':
        form = pngform(request.POST, request.FILES)
        file_name = request.FILES['pngfile'].name
        print('file name: ')
        print(file_name)
        file_type = file_name[-3:]
        print('file type: ')
        print(file_type)
        if file_type == 'png':
            if form.is_valid():
                form.save()
                return redirect('convertpng')
        else:
            messages.info(request, 'wrong file type provided')
            return redirect('index')
    else:
        return Http404

def converter3(request):
    pythoncom.CoInitialize()
    print('inside png converter')
    file = Pngimage.objects.latest('id')
    file_path = file.pngfile.url[1:]
    print('file path -> -> ->')
    print(file_path)
    img = Image.open(file_path)
    print("The size of the image before conversion : ", end="")
    print(os.path.getsize(file_path))

    rgb_img = img.convert("RGB")
    jpgname = file_path[:-3] + 'jpg'
    rgb_img.save(jpgname)
    print("The size of the image after conversion : ", end="")
    print(os.path.getsize(jpgname))
    jpgurl = 'http://e0932e8bc9f4.ngrok.io/' + jpgname
    print(jpgurl)
    context = {'url': jpgurl}
    return render(request, 'app1/wait.html',  context)

def wait(request):
    return render(request, 'app1/wait.html')
