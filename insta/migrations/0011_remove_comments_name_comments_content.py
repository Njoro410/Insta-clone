# Generated by Django 4.0.3 on 2022-04-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0010_comments_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='name',
        ),
        migrations.AddField(
            model_name='comments',
            name='content',
            field=models.TextField(default='Comment'),
        ),
    ]