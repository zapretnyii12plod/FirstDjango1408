# Generated by Django 4.2.4 on 2023-08-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_snippet_user_alter_snippet_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='private',
            field=models.IntegerField(default=0),
        ),
    ]
