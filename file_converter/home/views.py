from django.shortcuts import render,redirect
from .forms import DocumentForm
from json2xml import json2xml

def index(request):
     if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            if request.POST.get('file_format') == 'json' and request.POST.get('format_output') == 'xml' :
                print("converting")
                request.FILES['document'].read()=jsontoxml(request.FILES['document'].read())
                print(request.FILES['document'].read())
            form.save()
            return redirect('index')
     else:
         form = DocumentForm()
     page_details={
     'title':'file converter: get freedom to convert file',
     'form': form
     }
     return render(request,"home/index.html",page_details)

def jsontoxml(data):
     data=json2xml.Json2xml(data).to_xml()
     return data
