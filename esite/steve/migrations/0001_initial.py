# Generated by Django 2.2.9 on 2020-07-09 04:43

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='StevePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('city', models.CharField(max_length=255, null=True)),
                ('zip_code', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('telephone', models.CharField(max_length=255, null=True)),
                ('telefax', models.CharField(max_length=255, null=True)),
                ('vat_number', models.CharField(max_length=255, null=True)),
                ('whatsapp_telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('whatsapp_contactline', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_id', models.CharField(max_length=255, null=True)),
                ('court_of_registry', models.CharField(max_length=255, null=True)),
                ('place_of_registry', models.CharField(max_length=255, null=True)),
                ('trade_register_number', models.CharField(max_length=255, null=True)),
                ('ownership', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('copyrightholder', models.CharField(max_length=255, null=True)),
                ('about', wagtail.core.fields.RichTextField(null=True)),
                ('privacy', wagtail.core.fields.RichTextField(null=True)),
                ('sociallinks', wagtail.core.fields.StreamField([('link', wagtail.core.blocks.URLBlock(help_text='Important! Format https://www.domain.tld/xyz'))])),
                ('sections', wagtail.core.fields.StreamField([('s_news', wagtail.core.blocks.StructBlock([('news_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='Bold header text', null=True)), ('news_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', help_text='News paragraph', null=True))], blank=False, icon='group', null=True)), ('code', wagtail.core.blocks.RawHTMLBlock(blank=True, classname='full', icon='code', null=True))], null=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]