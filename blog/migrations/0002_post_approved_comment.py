# Generated by Django 2.2.15 on 2020-08-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
