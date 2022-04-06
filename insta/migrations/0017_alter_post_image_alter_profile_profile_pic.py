# Generated by Django 4.0.3 on 2022-04-05 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0016_alter_post_image_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/avatar.png', upload_to='profile_pics'),
        ),
    ]