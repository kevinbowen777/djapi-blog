# Generated by Django 4.2.1 on 2023-05-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_customuser_country_customuser_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="age",
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]