# Generated by Django 2.2.7 on 2019-12-02 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_app', '0002_auto_20191112_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='description',
            new_name='comment_description',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='comment_title',
        ),
    ]