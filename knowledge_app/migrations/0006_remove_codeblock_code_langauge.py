# Generated by Django 2.2.7 on 2019-12-03 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_app', '0005_codeblock_code_langauge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codeblock',
            name='code_langauge',
        ),
    ]