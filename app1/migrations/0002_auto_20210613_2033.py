# Generated by Django 3.1 on 2021-06-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordfile',
            name='docxfile',
            field=models.FileField(upload_to='media'),
        ),
    ]
