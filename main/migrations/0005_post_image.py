# Generated by Django 3.1.1 on 2020-09-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_image'),
        ),
    ]
