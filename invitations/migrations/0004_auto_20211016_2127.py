from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0003_auto_20151126_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.INVITATIONS_COMPANY_MODEL),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
