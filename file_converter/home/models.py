from django.db import models


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
