# Generated by Django 3.2 on 2022-01-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0005_auto_20220118_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='backlink_company',
        ),
        migrations.AlterField(
            model_name='invitation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]