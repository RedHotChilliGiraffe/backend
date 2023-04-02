# Generated by Django 4.1.7 on 2023-04-02 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lobby', '0002_alter_lobby_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobby',
            name='participant',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
    ]
