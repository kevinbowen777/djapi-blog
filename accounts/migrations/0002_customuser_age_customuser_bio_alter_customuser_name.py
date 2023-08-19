# Generated by Django 4.0.7 on 2022-08-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="age",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="bio",
            field=models.TextField(blank=True, verbose_name="Bio"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Name of User"
            ),
        ),
    ]
