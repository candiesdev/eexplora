# Generated by Django 4.1 on 2023-04-08 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
