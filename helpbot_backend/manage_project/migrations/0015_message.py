# Generated by Django 4.2.4 on 2023-10-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage_project", "0014_alter_project_secretkey"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created At")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated At")),
                ("content", models.CharField(blank=True, max_length=50, null=True)),
                ("sender", models.CharField(blank=True, max_length=100, null=True)),
                ("receiver", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
