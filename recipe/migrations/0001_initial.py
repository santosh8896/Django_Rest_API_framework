# Generated by Django 3.1.2 on 2022-05-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time_minutes', models.IntegerField()),
                ('ingredients', models.CharField(max_length=255)),
            ],
        ),
    ]