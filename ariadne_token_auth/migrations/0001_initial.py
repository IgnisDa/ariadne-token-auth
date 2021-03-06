# Generated by Django 3.1.7 on 2021-02-23 03:01

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
            name='AuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time this token was created at.')),
                ('token_string', models.TextField(editable=False, help_text='The token that will be used for login.')),
                ('user', models.OneToOneField(help_text='The user that this token was created for.', on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
