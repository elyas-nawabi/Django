# Generated by Django 3.2.4 on 2021-09-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://unsplash.com/photos/MqT0asuoIcU', max_length=500),
        ),
    ]
