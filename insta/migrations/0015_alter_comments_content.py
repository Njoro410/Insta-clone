# Generated by Django 4.0.3 on 2022-04-05 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0014_remove_comments_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(),
        ),
    ]