# Generated by Django 3.2 on 2024-04-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20240422_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_name',
        ),
        migrations.AddField(
            model_name='book',
            name='cover_type',
            field=models.CharField(blank=True, choices=[('hardback', 'Hardback'), ('paperback', 'Paperback'), ('special', 'Special')], max_length=20, null=True),
        ),
    ]
