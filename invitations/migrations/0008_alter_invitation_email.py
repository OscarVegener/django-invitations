# Generated by Django 3.2.9 on 2021-12-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0007_alter_invitation_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail address'),
        ),
    ]
