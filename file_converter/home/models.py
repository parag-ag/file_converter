from django.db import models
from django.conf import settings
import os
from django.core.files import File
from json2xml import json2xml,readfromjson
from django.core.files.base import ContentFile

in_format = (
   ('xml', 'xml'),
   ('json', 'json'),
   ('pdf', 'pdf'),
 )

format_want =  (
    ('xml', 'xml'),
    ('json', 'json'),
    ('pdf', 'pdf'),
  )


class Document(models.Model):
    file_format=models.CharField(max_length=9, choices=in_format, default='1')
    format_output=models.CharField(max_length=9, choices=format_want, default='1')
    document = models.FileField(upload_to="documents/")

    def save(self, **kwargs):
        path=settings.MEDIA_ROOT
        file_format_now=self.file_format
        file_format_change_to=self.format_output
        super().save()
        file_name = self.document.name
        print(file_name)
        file = path+'/'+file_name
        print(file)
        name=file.split('.')[0]
        print(name)
        if file_format_now == 'json' and file_format_change_to == 'xml' :
            data=readfromjson(file)
            with open(file, 'w') as f:
                 myfile = File(f)
                 myfile.write(json2xml.Json2xml(data).to_xml())
            myfile.closed
            os.rename(file,name+'.xml')
