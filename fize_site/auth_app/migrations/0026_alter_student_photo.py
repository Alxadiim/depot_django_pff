# Generated by Django 5.1.3 on 2024-11-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0025_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
