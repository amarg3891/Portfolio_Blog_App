# Generated by Django 3.1.5 on 2021-02-03 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0004_auto_20210203_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ImageField(upload_to='images/'),
        ),
    ]