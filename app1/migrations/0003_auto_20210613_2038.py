# Generated by Django 3.1 on 2021-06-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210613_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordfile',
            name='docxfile',
            field=models.FileField(upload_to='docxs'),
        ),
    ]
