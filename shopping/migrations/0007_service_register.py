# Generated by Django 3.1.3 on 2021-02-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_auto_20201213_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='service_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('landmark', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('machine_name', models.CharField(max_length=30)),
                ('machine_model', models.CharField(max_length=20)),
                ('machine_Complaint', models.CharField(max_length=50)),
            ],
        ),
    ]
