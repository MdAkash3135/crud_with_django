# Generated by Django 4.2.6 on 2023-11-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
