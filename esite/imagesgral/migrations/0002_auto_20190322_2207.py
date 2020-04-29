# Generated by Django 2.1.7 on 2019-03-22 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
        ('utils', '0001_initial'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='license',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='utils.LicenseSnippet'),
        ),
        migrations.AddField(
            model_name='customimage',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='customimage',
            name='uploaded_by_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user'),
        ),
        migrations.AlterUniqueTogether(
            name='rendition',
            unique_together={('image', 'filter_spec', 'focal_point_key')},
        ),
    ]
