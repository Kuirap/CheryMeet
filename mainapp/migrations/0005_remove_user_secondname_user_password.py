# Generated by Django 4.2.3 on 2023-07-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_user_secondname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='secondname',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
    ]
