# Generated by Django 2.2.17 on 2021-03-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("new_relic", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newrelicconfiguration",
            name="base_url",
            field=models.URLField(null=True),
        ),
    ]
