# Generated by Django 2.2.2 on 2019-06-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='format',
        ),
        migrations.AddField(
            model_name='document',
            name='file_format',
            field=models.CharField(choices=[('xml', 'xml'), ('json', 'json'), ('pdf', 'pdf')], default='1', max_length=9),
        ),
        migrations.AddField(
            model_name='document',
            name='format_output',
            field=models.CharField(choices=[('xml', 'xml'), ('json', 'json'), ('pdf', 'pdf')], default='1', max_length=9),
        ),
    ]
