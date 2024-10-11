# Generated by Django 5.0.7 on 2024-10-11 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0150_alter_cahierdecours_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cahierdecours',
            name='classe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.classe'),
        ),
        migrations.AlterField(
            model_name='cahierdecours',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.teacher'),
        ),
    ]
