"""Food sessions schema"""

import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql import GraphQLError

from .models import FoodSession
from waitress.items.models import SharedItem
from waitress.items.schema import SharedItemType
from waitress.users.decorators import check_user_in_session
from waitress.users.models import SessionUser
from waitress.users.schema import SessionUserType


class FoodSessionType(DjangoObjectType):
    """Food Session object for GraphQL"""
    class Meta:
        model = FoodSession


class Query(graphene.ObjectType):
    """Query Object for users Schema"""
    session_items = graphene.List(SharedItemType, required=True)

    @login_required
    @check_user_in_session
    def resolve_session_items(self, info, session_user, **kwargs):
        food_session = session_user.food_session
        return SharedItem.objects.filter(food_session=food_session)


class CreateFoodSession(graphene.Mutation):
    """Mutation that creates a session"""
    food_session = graphene.Field(FoodSessionType)

    class Arguments:
        """Args that are allowed in mutation"""
        name = graphene.String(required=True)

    @login_required
    def mutate(self, info, name):
        """Creates an item"""
        admin = info.context.user
        session_exists = FoodSession.objects.filter(
            admin=admin, is_active=True
        ).exists()
        if session_exists:
            raise GraphQLError('You already have an active session.')
        food_session = FoodSession.objects.create(
            name=name,
            admin=admin,
            is_active=True
        )
        SessionUser.objects.create(
            user=admin, food_session=food_session, is_active=True
        )
        return CreateFoodSession(food_session=food_session)


class EnterToSession(graphene.Mutation):
    """Mutation that adds a user to a session"""
    session_user = graphene.Field(SessionUserType)

    class Arguments:
        """Args that are allowed in mutation"""
        session_id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, session_id):
        """Adds a user to a food session"""
        user = info.context.user
        session_queryset = FoodSession.objects.filter(pk=session_id)
        if not session_queryset.exists():
            raise GraphQLError("The session you are trying to enter doesn't exists.")
        user_in_session = SessionUser.objects.filter(
            user=user,
            is_active=True
        ).exists()
        if user_in_session:
            raise GraphQLError('You already are in an active session.')
        food_session = session_queryset.get()
        session_user = SessionUser.objects.create(
            user=user, food_session=food_session, is_active=True
        )
        return EnterToSession(session_user=session_user)


class Mutation:
    """Mutation object for sessions app"""
    create_food_session = CreateFoodSession.Field()
    enter_to_session = EnterToSession.Field()
