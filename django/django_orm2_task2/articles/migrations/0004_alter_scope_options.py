# Generated by Django 5.1 on 2024-08-28 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_tag_alter_article_options_scope_article_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['main_tag'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
