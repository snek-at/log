# Generated by Django 2.2.9 on 2020-06-17 16:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import esite.session.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('test', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('session_name', models.CharField(blank=True, max_length=32, null=True)),
                ('session_scope', models.CharField(blank=True, max_length=256, null=True)),
                ('session_from', models.DateTimeField(blank=True, null=True)),
                ('session_to', models.DateTimeField(blank=True, null=True)),
                ('session_duration', models.DurationField(blank=True, null=True, validators=[esite.session.models.min_duration_validator])),
                ('session_room', models.CharField(blank=True, max_length=32, null=True)),
                ('session_max_attendees', models.PositiveIntegerField(default=16)),
                ('session_current_attendees', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9000, message='The Field session_current_attendees must not exceed session_max_attendees.')])),
                ('session_presentators', wagtail.core.fields.StreamField([('se_presentator', wagtail.core.blocks.StructBlock([('presentator_name', wagtail.core.blocks.CharBlock(help_text='Name of the presentator', null=True, required=True)), ('presentator_email', wagtail.core.blocks.EmailBlock(help_text='Important! Format ci@s.co', null=True, required=True)), ('presentator_link', wagtail.core.blocks.URLBlock(help_text='Important! Format https://www.domain.tld/xyz', null=True, required=True))], icon='fa-id-badge', null=True))], null=True)),
                ('session_attendees', wagtail.core.fields.StreamField([('se_attendee', wagtail.core.blocks.StructBlock([('attendee_name', wagtail.core.blocks.CharBlock(help_text='Name of the attendee', null=True, required=False)), ('attendee_email', wagtail.core.blocks.EmailBlock(help_text='Important! Format ci@s.co', null=True, required=False)), ('attendee_attendance', wagtail.core.blocks.BooleanBlock(default=False, help_text='Whether the attendee was attending or not', null=False, required=False)), ('attendee_cache', wagtail.core.blocks.TextBlock(help_text='Other information', null=True, required=False))], icon='fa-credit-card', null=True))], blank=True, null=True)),
                ('session_cache', models.TextField(blank=True, null=True)),
                ('session_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
    ]
