# Generated by Django 4.2.4 on 2023-08-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_color_remove_item_count_item_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]