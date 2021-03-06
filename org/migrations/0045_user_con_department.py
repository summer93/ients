# Generated by Django 2.0 on 2018-03-01 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0044_remove_user_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Con_Department',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Department', verbose_name='部门')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'ordering': ['Department__Company'],
            },
        ),
    ]
