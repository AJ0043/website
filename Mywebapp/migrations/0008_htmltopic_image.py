# Generated by Django 5.1.4 on 2025-03-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mywebapp', '0007_htmltopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='htmltopic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='html_topics/'),
        ),
    ]
