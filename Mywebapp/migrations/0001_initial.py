# Generated by Django 5.1.4 on 2024-12-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=200)),
                ('Business', models.CharField(max_length=200)),
                ('Service', models.CharField(max_length=200)),
                ('Message', models.TextField()),
            ],
        ),
    ]
