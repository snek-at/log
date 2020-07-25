from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import Session


# Register your registration related models here.

class SessionAdmin(ModelAdmin):
    model = Session
    menu_label = "Session"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    # Listed in the registration overview
    list_filter = ('session_name', 'session_scope', 'session_from',
                    'session_to', 'session_room')
    list_display = ('session_name', 'session_scope', 'session_from',
                    'session_to', 'session_room')
    search_fields = ('session_id', 'session_name', 'session_scope',
                     'session_from', 'session_to', 'session_room')


modeladmin_register(SessionAdmin)
