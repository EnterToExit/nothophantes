# Generated by Django 5.0.4 on 2024-04-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_remove_user_id_alter_user_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
