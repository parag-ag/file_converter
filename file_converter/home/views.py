from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document

def index(request):
     if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        name=request.FILES['document'].split('.')[0]+request.POST['format_output']
        print(name)
     form = DocumentForm()
     page_details={
     'title':'file converter: get freedom to convert file',
     'form': form,
     }
     return render(request,"home/index.html",page_details)
