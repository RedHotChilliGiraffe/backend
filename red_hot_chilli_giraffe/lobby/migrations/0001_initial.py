# Generated by Django 4.1.7 on 2023-04-01 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(help_text='Enter theme of lobby', max_length=40)),
                ('messages', models.JSONField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('started', models.BooleanField(default=False)),
                ('host', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='host', to=settings.AUTH_USER_MODEL)),
                ('participant', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='participant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]