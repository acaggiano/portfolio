# Generated by Django 2.1.5 on 2019-03-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20190201_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='address',
            field=models.URLField(blank=True),
        ),
    ]
