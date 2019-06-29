from django.db import models
from json2xml import json2xml,readfromjson

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
    document = models.FileField(upload_to='documents/')

    def save(self, **kwargs):
        file = self.document.path
        file_format_now=self.file_format
        file_format_change_to=self.format_output

        if file_format_now == 'json' and file_format_change_to == 'xml' :
            print(file)
            data =  readfromjson(file)
            print(json2xml.Json2xml(data).to_xml())



        super().save()
