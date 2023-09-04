# Generated by Django 4.2.4 on 2023-09-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_user_name'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('name', 'picture'), name='unique_name_picture'),
        ),
    ]
