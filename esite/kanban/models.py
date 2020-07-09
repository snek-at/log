import uuid
from django.http import HttpResponse
from django.db import models
from django.core.validators import RegexValidator
from wagtail.admin.edit_handlers import FieldPanel
from esite.colorfield.fields import ColorField
from wagtail.core.fields import StreamField
from .blocks import TagChooserBlock

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.


class Kanban(models.Model):
    kanban_title = models.CharField(max_length=16)
    kanban_id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.kanban_title


class KanbanLane(models.Model):
    kanban_lane_title = models.CharField(max_length=16)
    kanban_lane_id = models.AutoField(primary_key=True, editable=False)
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE)

    def __str__(self):
        return self.kanban_lane_title


class KanbanTag(models.Model):
    kanban_tag_name = models.CharField(max_length=128)
    kanban_tag_icon = models.CharField(max_length=128)
    kanban_tag_color = ColorField()
    kanban_tag_id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.kanban_tag_name


class KanbanCard(models.Model):
    kanban_card_title = models.CharField(max_length=16)
    kanban_card_id = models.AutoField(primary_key=True, editable=False)
    kanban_card_description = models.CharField(max_length=256)
    kanban_lane = models.ForeignKey(KanbanLane, on_delete=models.CASCADE)
    kanban_tags = models.ManyToManyField(KanbanTag)

    def __str__(self):
        return self.kanban_card_title
