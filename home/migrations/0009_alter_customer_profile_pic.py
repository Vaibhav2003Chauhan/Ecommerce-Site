# Generated by Django 4.2.1 on 2023-07-22 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='PHOTO.jpg', null=True, upload_to=''),
        ),
    ]
