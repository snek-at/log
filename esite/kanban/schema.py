from django.contrib.auth import get_user_model
import json
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, permission_required, staff_member_required, superuser_required

from wagtail.core.models import Page

from esite.user.models import User
from esite.profile.models import ProfilePage
from esite.customer.models import Customer
from esite.registration.schema import UserType

from .models import Kanban, KanbanLane, KanbanCard, KanbanTag
# Create your registration related graphql schemes here.

#class UserType(DjangoObjectType):
#    class Meta:
#        model = User
#        exclude_fields = ['password']


class KanbanType(DjangoObjectType):
    class Meta:
        model = Kanban


class CacheKanban(graphene.Mutation):
    kanban = graphene.Field(KanbanType)

    class Arguments:
        token = graphene.String(required=False)
        kanban_id = graphene.String(required=True)

    @login_required
    def mutate(self, info, token, kanban_id):
        #kanban = Kanban.objects.all()

        #user.platform_data = platform_data
        #user.save()
        kanban = Kanban.objects.get(kanban_id=kanban_id)

        #kanban_page.kanban_data = kanban_data

        #profile_page.save_revision().publish()

        return CacheKanban(kanban=kanban)


class Query(graphene.ObjectType):
    kanbans = graphene.List(KanbanType)

    def resolve_kanbans(self, info):
        # To list all users
        return Kanban.objects.all()