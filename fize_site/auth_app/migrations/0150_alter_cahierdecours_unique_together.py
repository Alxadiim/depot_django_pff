# Generated by Django 5.0.7 on 2024-10-11 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0149_alter_cahierdecours_duree_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cahierdecours',
            unique_together=set(),
        ),
    ]
