# Generated by Django 4.1.3 on 2023-01-19 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_useraccprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccprofile',
            name='image',
            field=models.ImageField(upload_to='users_images/'),
        ),
    ]
