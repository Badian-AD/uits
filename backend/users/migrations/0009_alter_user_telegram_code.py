# Generated by Django 4.2.5 on 2024-05-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_telegram_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_code',
            field=models.CharField(editable=False, max_length=12, unique=True),
        ),
    ]