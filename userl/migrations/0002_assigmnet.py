# Generated by Django 3.2.8 on 2022-06-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='assigmnet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomCode', models.CharField(max_length=7)),
                ('UniqCode', models.CharField(max_length=10)),
                ('pdf', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('mark', models.CharField(max_length=200)),
                ('totalm', models.CharField(max_length=200)),
            ],
        ),
    ]