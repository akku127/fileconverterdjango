# Generated by Django 3.1 on 2021-06-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210613_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordfile',
            name='pdf',
            field=models.FileField(null=True, upload_to='docxs'),
        ),
    ]