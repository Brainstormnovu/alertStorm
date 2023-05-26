# Generated by Django 4.2.1 on 2023-05-26 20:50

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_notification_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'In-App'), ('2', 'Push'), ('3', 'Email'), ('4', 'Chat'), ('5', 'SMS')], max_length=5),
        ),
    ]