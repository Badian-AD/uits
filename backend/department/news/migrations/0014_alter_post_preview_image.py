# Generated by Django 4.2.5 on 2024-02-24 12:17

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_alter_post_preview_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='photos/%Y/%m/%d', verbose_name='Превью фото'),
        ),
    ]