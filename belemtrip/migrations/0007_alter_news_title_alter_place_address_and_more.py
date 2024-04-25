# Generated by Django 4.2.11 on 2024-04-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("belemtrip", "0006_remove_touristspotcategory_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Título"),
        ),
        migrations.AlterField(
            model_name="place",
            name="address",
            field=models.CharField(max_length=255, verbose_name="Endereço"),
        ),
        migrations.AlterField(
            model_name="restaurantcategory",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="touristspotcategory",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Nome"),
        ),
    ]