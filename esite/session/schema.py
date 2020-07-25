from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

import graphene
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql.execution.base import ResolveInfo
from graphql_jwt.decorators import login_required, permission_required, staff_member_required, superuser_required

from .models import Session
from esite.api.registry import registry

# Create your user related graphql schemes here.

class Query(graphene.ObjectType):
    sessions = graphene.List(registry.models[Session], token=graphene.String())

    @login_required
    def resolve_sessions(self, info, **_kwargs):
        # To list all events
        return Session.objects.all()

class SaveSessionCache(graphene.Mutation):
    session = graphene.Field(registry.models[Session])

    class Arguments:
        token = graphene.String(required=False)
        session_id = graphene.String(required=True)
        session_cache = graphene.String(required=True)

    @login_required
    def mutate(self, info, token, session_id, session_cache):

        session = Session.objects.get(session_id=f"{session_id}")

        session.session_cache = session_cache

        session.save()

        return SaveSessionCache(session=session)

class SessionCheckAttendance(graphene.Mutation):
    session = graphene.Field(registry.models[Session])

    class Arguments:
        token = graphene.String(required=False)
        session_id = graphene.String(required=True)
        session_attendee_name = graphene.String(required=True)

    @login_required
    def mutate(self, info, token, session_id, session_attendee_name):

        session = Session.objects.get(session_id=f"{session_id}")

        for index, attendee in enumerate(session.session_attendees.stream_data):
            if attendee["value"]["attendee_name"] == session_attendee_name:
                session.session_attendees.stream_data[index]["value"]["attendee_attendance"] = True

        session.save()

        return SaveSessionCache(session=session)

class SessionAddAttendee(graphene.Mutation):
    session = graphene.Field(registry.models[Session])

    class Arguments:
        token = graphene.String(required=False)
        session_id = graphene.String(required=True)
        session_attendee = GenericScalar(required=True)

    @login_required
    def mutate(self, info, token, session_id, session_attendee):

        session = Session.objects.get(session_id=f"{session_id}")

        for attendee in session.session_attendees.stream_data:
            if attendee["value"]["attendee_name"] == session_attendee["attendee_name"]:
                raise GraphQLError('That attendee already exists')

        session.session_attendees.stream_data.append({'type': 'se_attendee', 'value': session_attendee})

        session.save()

        return SaveSessionCache(session=session)

class SessionRemoveAttendee(graphene.Mutation):
    session = graphene.Field(registry.models[Session])

    class Arguments:
        token = graphene.String(required=False)
        session_id = graphene.String(required=True)
        session_attendee_name = graphene.String(required=True)

    @login_required
    def mutate(self, info, token, session_id, session_attendee_name):

        session = Session.objects.get(session_id=f"{session_id}")

        session.session_attendees.stream_data=[attendee for attendee in session.session_attendees.stream_data if not (attendee["value"]["attendee_name"] == session_attendee_name)]

        session.save()

        return SaveSessionCache(session=session)

class SaveSessionTable(graphene.Mutation):
    session = graphene.Field(registry.models[Session])

    class Arguments:
        token = graphene.String(required=False)
        session_id = graphene.String(required=True)
        session_name = graphene.String(required=False)
        session_scope = graphene.String(required=False)
        session_from = graphene.String(required=False)
        session_to = graphene.String(required=False)
        session_room = graphene.String(required=False)
        session_max_attendees = graphene.String(required=False)
        session_current_attendees = graphene.String(required=False)
        session_presentators = graphene.String(required=False)
        session_attendees = graphene.String(required=False)
        session_cache = graphene.String(required=False)

    @login_required
    def mutate(self, info, token, session_id, session_name, session_scope, session_from, session_to, session_room, session_max_attendees, session_current_attendees, session_presentators, session_attendees, session_cache):

        session = Session.objects.get(session_id=f"{session_id}")

        session_obj.session_name = session_name
        session_obj.session_scope = session_scope
        session_obj.session_from = session_from
        session_obj.session_to = session_to
        session_obj.session_room = session_room
        session_obj.session_max_attendees = session_max_attendees
        session_obj.session_current_attendees = session_current_attendees 
        session_obj.session_presentators = session_presentators
        session_obj.session_attendees = session_attendees
        session_obj.session_cache = session_cache

        session.save()

        return SaveSessionTable(session=session)