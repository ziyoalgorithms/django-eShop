# Generated by Django 4.1.3 on 2023-01-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=0, max_length=13),
            preserve_default=False,
        ),
    ]
