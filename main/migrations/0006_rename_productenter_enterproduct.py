# Generated by Django 5.0.1 on 2024-02-07 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_productenter'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductEnter',
            new_name='EnterProduct',
        ),
    ]