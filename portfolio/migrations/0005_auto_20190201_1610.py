# Generated by Django 2.1.5 on 2019-02-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20190201_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
