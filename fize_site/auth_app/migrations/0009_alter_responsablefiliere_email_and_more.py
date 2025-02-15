# Generated by Django 5.0.7 on 2024-10-19 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0008_remove_paiement_comptable_oberver_paiement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsablefiliere',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='responsablefiliere',
            name='num_tel',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='responsablefiliere',
            name='profession',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
