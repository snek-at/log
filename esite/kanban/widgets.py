from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from generic_chooser.widgets import AdminChooser
from .models import KanbanTag


class TagChooser(AdminChooser):
    choose_one_text = _('Choose a Tag')
    model = KanbanTag
    choose_modal_url_name = 'tag_chooser:choose'