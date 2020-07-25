# -*- coding: utf-8 -*-
from django.db import migrations


def create_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    Image = apps.get_model('wagtailimages.Image')
    HomePage = apps.get_model('projekttage.ProjekttagePage')

    # Delete the default homepage
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create initial images
    Image.objects.create(
        id=1,
        title='unnamed.jpg',
        file='init_images/projekttage/unnamed.jpg',
        width=243,
        height=512,
        file_size=68076,
        collection_id=1,
        file_hash='7c949247d2a28b454f8ecb57ea0a5c432bddba31',
    )

    Image.objects.create(
        id=2,
        title='1500x500.png',
        file='init_images/projekttage/1500x500.png',
        width=1500,
        height=500,
        file_size=1912975,
        collection_id=1,
        file_hash='77b6bac1fc400563f45b9a6505a2663111ace8dc',
    )

    Image.objects.create(
        id=3,
        title='26285351.jpg',
        file='init_images/projekttage/26285351.jpg',
        width=400,
        height=400,
        file_size=13904,
        collection_id=1,
        file_hash='e345a318b3067b083871f0b90f03776e6932c8a9',
    )

    # Create content type for homepage model
    homepage_content_type, __ = ContentType.objects.get_or_create(
        model='projekttagepage', app_label='projekttage')

    # Create a initial homepage
    homepage = HomePage.objects.create(
        title="Projekttage",
        draft_title="Projekttage",
        slug='home',
        content_type=homepage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
        headers='''[
  {
    "type": "h_banner",
    "value": {
      "banner_head": "LAST WEEK Projekttage",
      "banner_subhead": "<p>Das Motto des heurigen Jahres ist &quot;DevOps &amp; Security&quot;. In zahlreichen Vorträgen und Workshops möchten wir unser Wissen zu diesem Themenkomplex austauschen und vertiefen. In gemütlichem Ambiente finden wir Zeit für Diskussionen und das Knüpfen von neuen Netzwerken finden.</p>",
      "banner_image": 2
    },
    "id": "8d272b27-fbe2-4b2e-81fa-0b89ea4a84a8"
  }
]''',
        sections='''[
  {
    "type": "s_info",
    "value": {
      "info_head": "Linux Wochen",
      "info_paragraph": "<h3>Tux on Tour</h3><p>Der Pinguin macht 2020 wieder die Österreich Rundfahrt. Wie in den letzten Jahren sind die Linuxwochen eine Veranstaltung, die weit über Linux hinaus geht und den Open Source Gedanken in all seinen Facetten repräsentiert.</p><p><b>DevOps und Security</b></p><p>Unter diesem Motto treffen sich Vertreter aus Wirtschaft, Bildung und der Linux-Gemeinde zum Wissensaustausch und knüpfen neue Netzwerke.</p>",
      "info_image": 3,
      "info_image_position": "right"
    },
    "id": "473a04c2-ef8e-46e0-98c6-4fd5cdccaa38"
  }
]''',
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(
        hostname='localhost', root_page=homepage, is_default_site=True)


def remove_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    HomePage = apps.get_model('home.HomePage')

    # Delete the default homepage
    # Page and Site objects CASCADE
    HomePage.objects.filter(slug='home', depth=2).delete()

    # Delete content type for homepage model
    ContentType.objects.filter(model='homepage', app_label='home').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_initial'),
        ('projekttage', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_homepage, remove_homepage),
    ]