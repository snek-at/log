import graphene
from graphene_django import DjangoObjectType
from wagtailmedia.models import Media
from django.conf import settings
# graphql_jwt
from graphql_jwt.decorators import login_required, permission_required, staff_member_required, superuser_required

class MediaObjectType(DjangoObjectType):
    class Meta:
        model = Media
        exclude_fields = ("tags",)

    @login_required
    def resolve_file(self, info, **kwargs):
        if self.file.url[0] == "/":
            return settings.BASE_URL + self.file.url
        return self.file.url
