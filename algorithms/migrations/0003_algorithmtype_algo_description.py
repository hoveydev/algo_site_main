# Generated by Django 3.2.11 on 2022-01-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0002_algorithmtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithmtype',
            name='algo_description',
            field=models.TextField(default='placeholder', max_length=2000),
            preserve_default=False,
        ),
    ]
