# Generated by Django 4.2.4 on 2023-08-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_snippet_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='private',
            field=models.IntegerField(choices=[('1', 'Private'), ('0', 'Public')], default=0),
        ),
    ]