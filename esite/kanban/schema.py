from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

import graphene
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql.execution.base import ResolveInfo
from graphql_jwt.decorators import login_required, permission_required, staff_member_required, superuser_required

from .models import Kanban, KanbanLane, KanbanCard, KanbanTag
from esite.api.registry import registry

# Create your user related graphql schemes here.

class GetKanbans(graphene.ObjectType):
    get_all_kanbans = graphene.List(registry.models[Kanban], token=graphene.String())

    @login_required
    def resolve_kanbans(self, info, **_kwargs):
        # To list all events
        return Kanban.objects.all()

class GetKanbanCache(graphene.ObjectType):
    get_kanban_cache = graphene.Field(registry.models[Kanban], token=graphene.String())

    @login_required
    def resolve_kanban_cache(self, info, **_kwargs):

        kanban = Kanban.objects.get(kanban_id=f"{kanban_id}")

        kanban.kanban_cache = kanban_cache

        kanban.save()

        return GetKanbanCache(kanban=kanban)

class SaveKanbanCache(graphene.Mutation):
    kanban = graphene.Field(registry.models[Kanban])

    class Arguments:
        token = graphene.String(required=False)
        kanban_id = graphene.String(required=True)
        kanban_cache = graphene.String(required=True)

    @login_required
    def mutate(self, info, token, kanban_id, kanban_cache):

        kanban = Kanban.objects.get(kanban_id=f"{kanban_id}")

        kanban.kanban_cache = kanban_cache

        kanban.save()

        return SaveKanbanCache(kanban=kanban)
