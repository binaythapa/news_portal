# Generated by Django 4.2.10 on 2024-02-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_alter_tag_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
