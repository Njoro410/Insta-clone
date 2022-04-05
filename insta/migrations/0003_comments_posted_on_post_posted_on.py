# Generated by Django 4.0.3 on 2022-04-04 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_post_followers_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]