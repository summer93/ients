# Generated by Django 2.0 on 2018-01-04 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20180104_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storeform',
            old_name='add_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='storeform',
            old_name='mod_date',
            new_name='modified_date',
        ),
    ]