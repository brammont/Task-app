# Generated by Django 4.2.4 on 2023-08-27 09:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Tasks",
            new_name="Task",
        ),
    ]
