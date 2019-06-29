from django.shortcuts import render,redirect
from .forms import DocumentForm
from json2xml import json2xml,readfromjson
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


def index(request):
     if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            if request.POST.get('file_format') == 'json' and request.POST.get('format_output') == 'xml' :
                print(jsontoxml(request.FILES['document'].name))


        return redirect('index')
     else:
         form = DocumentForm()
     page_details={
     'title':'file converter: get freedom to convert file',
     'form': form
     }
     return render(request,"home/index.html",page_details)

def jsontoxml(filename):
    data = readfromjson(MEDIA_ROOT+'/documents/'+filename)
    data_xml=json2xml.Json2xml(data).to_xml()
    url=MEDIA_ROOT+'/documents/'+os.path.splitext(filename)[0]+'.xml'
    rurl=os.path.splitext(filename)[0]+'.xml'
    with open(url, 'w+') as f:
        f.write(data_xml)
    os.remove(MEDIA_ROOT+'/documents/'+filename)
    return rurl
