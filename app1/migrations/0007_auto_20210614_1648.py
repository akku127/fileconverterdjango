# Generated by Django 3.1 on 2021-06-14 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='file',
            new_name='jpgfile',
        ),
    ]
