# Generated by Django 4.0.3 on 2022-03-26 23:31

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='alternativas',
            field=jsonfield.fields.JSONField(),
        ),
    ]
