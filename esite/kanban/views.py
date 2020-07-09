from django import forms
from django.shortcuts import render
from django.http import JsonResponse
from generic_chooser.views import ModelChooserViewSet
from django.utils.translation import ugettext_lazy as _
from .models import KanbanTag


def kanbanboard(request, site_id=None):
    return render(request, 'kanban/kanbanboard.html')


def getData(request):
    return JsonResponse({'foo': 'bar'})


class TagForm(forms.ModelForm):
    class Meta:
        model = KanbanTag
        fields = ['kanban_tag_name', 'kanban_tag_icon', 'kanban_tag_color']


class TagChooserViewSet(ModelChooserViewSet):
    icon = 'pilcrow'
    model = KanbanTag
    page_title = _("Choose a Tag")
    per_page = 10
    form_class = TagForm
