# Generated by Django 4.1.3 on 2022-12-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag", name="caption", field=models.CharField(max_length=50),
        ),
    ]