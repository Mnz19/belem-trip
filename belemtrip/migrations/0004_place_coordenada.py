# Generated by Django 4.2.11 on 2024-04-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("belemtrip", "0003_alter_event_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="place",
            name="coordenada",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Coordenadas"
            ),
        ),
    ]
