# Generated by Django 3.1.6 on 2022-04-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga_main', '0010_auto_20220417_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yogaclass',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
