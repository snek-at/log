from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

# Register your registration related models here.

from .models import Kanban, KanbanLane, KanbanCard, KanbanTag


class KanbanBoards(ModelAdmin):
    model = Kanban
    menu_label = "Kanban"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False


class KanbanLanes(ModelAdmin):
    model = KanbanLane
    menu_label = "Kanban Lanes"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False


class KanbanCards(ModelAdmin):
    model = KanbanCard
    menu_label = "Kanban Cards"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False


class KanbanTags(ModelAdmin):
    model = KanbanTag
    menu_label = "Kanban Tags"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False


class KanbanAdmin(ModelAdminGroup):
    menu_label = "Kanban Management"
    menu_icon = "group"
    menu_order = 110
    add_to_settings_menu = False
    exclude_from_explorer = False
    items = (KanbanBoards, KanbanLanes, KanbanCards, KanbanTags)


modeladmin_register(KanbanAdmin)
