# Generated by Django 4.2.11 on 2024-04-24 22:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("belemtrip", "0005_alter_event_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="touristspotcategory",
            name="phone",
        ),
    ]