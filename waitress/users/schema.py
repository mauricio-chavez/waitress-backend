"""Users schema"""

from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql import GraphQLError

from .decorators import check_user_in_session
from .models import SessionUser
from waitress.items.schema import PersonalItemType
from waitress.items.models import PersonalItem


class UserType(DjangoObjectType):
    """User object for GraphQL"""
    class Meta:
        model = get_user_model()


class SessionUserType(DjangoObjectType):
    """SessionUser object for GraphQL"""
    
    class Meta:
        model = SessionUser


class Query(graphene.ObjectType):
    """Query Object for users Schema"""
    user_items = graphene.List(PersonalItemType, required=True)

    @login_required
    @check_user_in_session
    def resolve_user_items(self, info, session_user, **kwargs):
        return PersonalItem.objects.filter(owner=session_user)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, email, **kwargs):
        user_exists = get_user_model().objects.filter(email=email).exists()
        if user_exists:
            raise GraphQLError('User already exists.')
        user = get_user_model().objects.create_user(email=email, **kwargs)

        return CreateUser(user=user)


class Mutation:
    """Mutation object for users schema"""
    create_user = CreateUser.Field()
