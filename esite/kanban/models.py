import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.core.models import Page
from wagtail.core import blocks
from datetime import timedelta
from esite.colorfield.fields import ColorField
from wagtail.core.fields import StreamField
from .blocks import TagChooserBlock

from esite.api.helpers import register_streamfield_block

from esite.api.models import (
    GraphQLForeignKey,
    GraphQLField,
    GraphQLStreamfield,
    GraphQLImage,
    GraphQLString,
    GraphQLCollection,
    GraphQLEmbed,
    GraphQLSnippet,
    GraphQLBoolean,
    GraphQLSnippet,
)


#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.


class Kanban(models.Model):
    kanban_id = models.CharField(primary_key=True, max_length=36)
    kanban_title = models.CharField(max_length=16)

    graphql_fields = [
        GraphQLString('kanban_id'),
        GraphQLString('kanban_title'),
    ]

    main_content_panels = [
        #FieldPanel('kanban_id'),
        FieldPanel('kanban_title'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(main_content_panels, heading='Main'),
    ])

    # custom save function
    def save(self, *args, **kwargs):
        if not self.kanban_id:
            self.kanban_id = str(uuid.uuid4())

        super(Kanban, self).save(*args, **kwargs)

    def __str__(self):
        return self.kanban_title


class KanbanLane(models.Model):
    kanban_lane_id = models.CharField(primary_key=True, max_length=36)
    kanban_lane_title = models.CharField(max_length=16)
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE)

    graphql_fields = [
        GraphQLString('kanban_lane_id'),
        GraphQLString('kanban_lane_title'),
    ]

    main_content_panels = [
        #FieldPanel('kanban_lane_id'),
        FieldPanel('kanban_lane_title'),
        FieldPanel('kanban'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(main_content_panels, heading='Main'),
    ])

    # custom save function
    def save(self, *args, **kwargs):
        if not self.kanban_lane_id:
            self.kanban_lane_id = str(uuid.uuid4())

        super(KanbanLane, self).save(*args, **kwargs)

    def __str__(self):
        return self.kanban_lane_title


class KanbanTag(models.Model):
    kanban_tag_id = models.CharField(primary_key=True, max_length=36)
    kanban_tag_name = models.CharField(max_length=128)
    kanban_tag_icon = models.CharField(max_length=128)
    kanban_tag_color = ColorField()

    graphql_fields = [
        GraphQLString('kanban_tag_id'),
        GraphQLString('kanban_tag_name'),
        GraphQLString('kanban_tag_icon'),
        GraphQLString('kanban_tag_color'),
    ]

    main_content_panels = [
        #FieldPanel('kanban_tag_id'),
        FieldPanel('kanban_tag_name'),
        FieldPanel('kanban_tag_icon'),
        FieldPanel('kanban_tag_color'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(main_content_panels, heading='Main'),
    ])

    # custom save function
    def save(self, *args, **kwargs):
        if not self.kanban_tag_id:
            self.kanban_tag_id = str(uuid.uuid4())

        super(KanbanTag, self).save(*args, **kwargs)

    def __str__(self):
        return self.kanban_tag_name


class KanbanCard(models.Model):
    kanban_card_id = models.CharField(primary_key=True, max_length=36)
    kanban_card_title = models.CharField(max_length=16)
    kanban_card_description = models.CharField(max_length=256)
    kanban_lane = models.ForeignKey(KanbanLane, on_delete=models.CASCADE)
    kanban_tags = models.ManyToManyField(KanbanTag)

    graphql_fields = [
        GraphQLString('kanban_card_id'),
        GraphQLString('kanban_card_title'),
        GraphQLString('kanban_card_description'),
    ]

    main_content_panels = [
        #FieldPanel('kanban_card_id'),
        FieldPanel('kanban_card_title'),
        FieldPanel('kanban_card_description'),
    ]

    # custom save function
    def save(self, *args, **kwargs):
        if not self.kanban_card_id:
            self.kanban_card_id = str(uuid.uuid4())

        super(KanbanCard, self).save(*args, **kwargs)

    def __str__(self):
        return self.kanban_card_title
