# Generated by Django 5.0.7 on 2024-10-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0014_rename_date_depot_projet_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='file',
            field=models.FileField(null=True, upload_to='media/projet'),
        ),
    ]
