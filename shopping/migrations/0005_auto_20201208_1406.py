# Generated by Django 3.1.3 on 2020-12-08 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
