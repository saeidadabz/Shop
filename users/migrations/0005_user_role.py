# Generated by Django 4.2 on 2024-11-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('vendor', 'Vendor'), ('driver', 'Driver')], max_length=10, null=True),
        ),
    ]
