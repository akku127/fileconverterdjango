# Generated by Django 3.1 on 2021-06-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_wordfile_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordfile',
            name='text',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
