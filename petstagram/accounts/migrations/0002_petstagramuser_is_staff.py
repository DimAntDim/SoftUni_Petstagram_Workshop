# Generated by Django 3.2.5 on 2021-07-22 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petstagramuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
