# Generated by Django 3.0.3 on 2022-02-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourApp', '0002_auto_20220203_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinations',
            name='longitude',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='longitude',
            field=models.CharField(max_length=250),
        ),
    ]
