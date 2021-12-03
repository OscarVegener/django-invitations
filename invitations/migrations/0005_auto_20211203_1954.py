from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0004_auto_20211016_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail address', unique=False),
        ),
    ]
