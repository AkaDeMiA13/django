# Generated by Django 2.1.5 on 2019-02-21 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='product',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='numder',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='history',
            name='owner',
        ),
        migrations.AddField(
            model_name='history',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
