# Generated by Django 3.0.5 on 2020-11-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requesthandler', '0003_auto_20201129_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapfile',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]
