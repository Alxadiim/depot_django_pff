# Generated by Django 5.1.3 on 2024-11-13 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0026_alter_student_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='salle',
            name='administrateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.administrateur'),
        ),
    ]
