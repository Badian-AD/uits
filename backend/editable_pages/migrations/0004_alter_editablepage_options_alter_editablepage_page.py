# Generated by Django 4.2.5 on 2024-05-08 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editable_pages', '0003_alter_editablepage_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editablepage',
            options={'verbose_name': 'редактируемая страница', 'verbose_name_plural': 'редактируемые страницы'},
        ),
        migrations.AlterField(
            model_name='editablepage',
            name='page',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Идентификатор страницы'),
        ),
    ]