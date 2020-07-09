from __future__ import absolute_import, unicode_literals
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import kanbanboard, getData

urlpatterns = [
    path('kanbanboard/', kanbanboard, name='kanban_board'),
    path('kanbanboard/<int:site_id>/', kanbanboard, name='kanban_site_board'),
    path('kanbanboard/all', getData, name='kanban_board_all'),
]