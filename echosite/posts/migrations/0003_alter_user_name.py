# Generated by Django 4.2.4 on 2023-09-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='Richie Chungus', max_length=60),
        ),
    ]