# Generated by Django 3.2.4 on 2021-11-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_auto_20211114_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, default='static/assets/img/post-bg.jpg', null=True, upload_to='images/'),
        ),
    ]