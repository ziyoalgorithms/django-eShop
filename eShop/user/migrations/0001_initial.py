# Generated by Django 4.1.3 on 2022-11-23 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User Account',
                'verbose_name_plural': 'Users Accounts',
            },
        ),
        migrations.CreateModel(
            name='UserAccProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('ERKAK', 'Erkak'), ('AYOL', 'Ayol')], max_length=5)),
                ('country', models.CharField(choices=[('SAMARQAND', 'Samarqand'), ('JIZZAH', 'Jizzah'), ('SURXONDARYO', 'Surxondaryo'), ('QASHQADARYO', 'Qashqadaryo'), ('SIRDARYO', 'Sirdaryo'), ('TOSHKENT', 'Toshkent'), ('NAVOIY', 'Navoiy'), ('NAMANGAN', 'Namangan'), ('ANDIJON', 'Andijon'), ('FARGONA', "Farg'ona"), ('XORAZM', 'Xorazm'), ('NUKUS', 'Nukus')], max_length=12)),
                ('address_line', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'Users Profiles',
            },
        ),
    ]