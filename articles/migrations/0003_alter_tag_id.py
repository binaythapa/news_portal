# Generated by Django 4.2.10 on 2024-02-09 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_alter_category_id_category_unique_name_within_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]